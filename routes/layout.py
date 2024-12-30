from fasthtml.common import (
    H1,
    A,
    Div,
    Img,
    Style,
)


def create_base_layout(content):
    """
    Creates the base layout with common header and styling.
    Takes content as parameter to be inserted in the main content area.
    """
    return Div(
        Style("""
            .custom-scrollbar::-webkit-scrollbar {
                width: 6px;
            }
            .custom-scrollbar::-webkit-scrollbar-track {
                background: rgb(24, 24, 27);
                border-radius: 3px;
            }
            .custom-scrollbar::-webkit-scrollbar-thumb {
                background: rgb(39, 39, 42);
                border-radius: 3px;
            }
            .custom-scrollbar::-webkit-scrollbar-thumb:hover {
                background: rgb(63, 63, 70);
            }
        """),
        Div(
            Div(
                A(
                    "الصفحة الرئيسية",
                    href="#",
                    cls="text-lg mx-4 font-bold text-center text-white hover:underline"
                ),
                cls="pr-4"
            ),
            A(
                Img(width='190', src='./static/img/nrct-logo.png', cls='custom-logo'),
                href="/",
            ),
            cls="bg-surface-10 flex py-4 px-6 items-center justify-between shadow-lg"
        ),
        Div(
            content,
            cls="p-8 md:p-12 bg-surface-5"
        ),
        dir="rtl",
        cls="min-h-screen bg-surface-0 text-white font-rubik"
    )
