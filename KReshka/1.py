import flet as ft


def main(page):
    count = 0
    txt = ft.Text("Кликов: 0")

    def click(e):
        nonlocal count
        count += 1
        txt.value = f"Кликов: {count}"
        page.update()

    page.add(
        txt,
        ft.ElevatedButton("Нажми", on_click=click)
    )


ft.app(main)