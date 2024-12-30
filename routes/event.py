from dataclasses import dataclass

from fasthtml import common as fh

from components.button import button
from components.form import input
from components.icon_link import icon_link
from make_app import app, rt
from routes.layout import create_base_layout


@rt("/")
def get(request):
    content = fh.Div(),
    return create_base_layout(content)

fh.serve()
