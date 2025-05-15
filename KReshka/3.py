import flet as ft
import os


def main(page):
    page.title = "Счётчик"
    page.window_width = 250
    page.window_height = 200

    os.makedirs("saves", exist_ok=True)

    try:
        with open("saves/counter.txt", "r") as f:
            count = int(f.read())
    except:
        count = 0

    txt = ft.Text(value=f"Кликов: {count}", size=20)

    def click(e):
        nonlocal count
        count += 123456789
        update_display()

    def reset(e):
        nonlocal count
        count = 0
        update_display()

    def save(e):
        with open("saves/counter.txt", "w") as f:
            f.write(str(count))
        txt.value = f"Сохранено: {count}"
        page.update()

    def update_display():
        txt.value = f"Кликов: {count}"
        page.update()

    page.add(
        txt,
        ft.Column([
            ft.ElevatedButton("Клик (+123456789)", on_click=click, width=200),
            ft.Row([
                ft.ElevatedButton("Сброс", on_click=reset, width=95),
                ft.ElevatedButton("Сохранить", on_click=save, width=95)
            ], spacing=10)
        ], spacing=10)
    )


ft.app(main)