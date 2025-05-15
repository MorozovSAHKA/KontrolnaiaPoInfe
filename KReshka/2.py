import flet as ft


def main(page):
    clicks = 0
    text = ft.Text("Кликов: 0")

    def click(e):
        nonlocal clicks
        clicks += 1
        text.value = f"Кликов: {clicks}"
        page.update()

    def reset(e):
        nonlocal clicks
        clicks = 0
        text.value = f"Кликов: {clicks}"
        page.update()

    page.add(
        text,
        ft.ElevatedButton("Нажми", on_click=click),
        ft.ElevatedButton("Сброс", on_click=reset)
    )


ft.app(main)