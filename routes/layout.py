from fasthtml.common import (
    H1,
    Div,
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
            H1(
                "NRCT",
                cls="text-5xl font-bold text-center text-white"
            ),
            cls="bg-surface-10 p-12 items-center content-center shadow-lg"
        ),
        Div(
            content,
            cls="p-8 md:p-12 bg-surface-5"
        ),
        cls="min-h-screen bg-surface-0 text-white font-rubik"
    )
