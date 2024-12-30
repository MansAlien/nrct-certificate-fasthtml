from dataclasses import dataclass

from fasthtml.common import (
    A,
    Button,
    Div,
    Form,
    Input,
    Li,
    Span,
    Ul,
    serve,
)

from components.button import button
from components.form import input
from components.icon_link import icon_link
from make_app import app, rt
from models import Todo
from routes.layout import create_base_layout


@dataclass
class TodoForm:
    title: str

def list_item(item):
        return Li(
            Div(
                Div(
                    Span(item.title, cls="text-lg truncate max-w-sm block"),
                    Span(
                        "✓ Done" if item.done else "○ Pending",
                        cls=f"mx-8 text-sm {'text-green-400' if item.done else 'text-yellow-400'}"
                    ),
                    title=item.title,
                    cls="flex items-center justify-between flex-1"
                ),
                Div(
                    icon_link(href="#", get="/todos/{todo.id}/edit", target="closest div"),
                    icon_link(type="delete", href="#", delete=f"/todos/{item.id}", target="closest li", swap="outerHTML"),
                    cls="flex items-center border-l border-l-surface-50"
                ),
                cls="flex items-center justify-between p-4 mb-2 rounded-lg bg-surface-20"
            ),
            cls="list-none"
        )

@rt("/")
def get(request):
    db = request.state.db
    todos = db.query(Todo).all()
    
    todo_items = [ list_item(todo) for todo in todos ]

    form = Form(
        Div(
            input(id="title", name="title", holder="What needs to be done?"),
            button("Add Task", type="submit", color="primary", cls="whitespace-nowrap py-4 px-6 transition-all"),
            cls="flex gap-4 w-full"
        ),
        cls="w-full mb-8",
        hx_post="/",
        target_id="todo_list",
        hx_swap="beforeend"
    )

    content = Div(
        Div(
            form,
            cls="max-w-2xl mx-auto"
        ),
        Div(
            Ul(
                *todo_items,
                id="todo_list",
                cls="space-y-2 max-h-96 overflow-y-auto custom-scrollbar"
            ),
            cls="max-w-2xl mx-auto"
        ),
    ),
    return create_base_layout(content)

@rt("/", methods=["POST"])
def post(request, todo: TodoForm):
    db = request.state.db
    new_todo = Todo(title=todo.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    
    return list_item(new_todo)

@rt("/todos/{todo_id}", methods=["DELETE"])
def delete_todo(request, todo_id: int):
    db = request.state.db
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return ""

@rt("/todos/{todo_id}/edit", methods=["GET"])
def edit_todo_form(request, todo_id: int):
    db = request.state.db
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    return Div(
        Form(
            Div(
                Input(
                    name="title",
                    value=todo.title,
                    cls="""
                        border text-sm rounded-lg flex-1
                        p-2 bg-surface-20 border-surface-30
                        text-white focus:ring-blue-500 focus:border-blue-500
                        transition-all hover:bg-surface-30
                    """
                ),
                Button(
                    "Save",
                    cls="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all ml-2"
                ),
                cls="flex items-center"
            ),
            hx_put=f"/todos/{todo_id}",
            hx_target="closest div",
        ),
        cls="p-4 mb-2 rounded-lg bg-surface-20"
    )

@rt("/todos/{todo_id}", methods=["PUT"])
def update_todo(request, todo_id: int, todo: TodoForm):
    db = request.state.db
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db_todo.title = todo.title
        db.commit()
        return Div(
            Div(
                Span(todo.title, cls="text-lg"),
                Span(
                    "✓ Done" if db_todo.done else "○ Pending",
                    cls=f"ml-8 text-sm {'text-green-400' if db_todo.done else 'text-yellow-400'}"
                ),
                cls="flex items-center flex-1"
            ),
            Div(

                A(
                    "✎",
                    href="#",
                    cls="text-blue-400 hover:text-blue-300 text-xl transition-colors px-2",
                    hx_get=f"/todos/{todo_id}/edit",
                    hx_target="closest div"
                ),
                A(
                    "×",
                    href="#",
                    cls="text-red-400 hover:text-red-300 text-xl font-bold transition-colors px-2",
                    hx_delete=f"/todos/{todo_id}",
                    hx_target="closest li",
                    hx_swap="outerHTML"
                ),
                cls="flex items-center"
            ),
            cls="flex items-center justify-between p-4 mb-2 rounded-lg bg-surface-20 hover:bg-surface-30 transition-all"
        )
    return ""

serve()
