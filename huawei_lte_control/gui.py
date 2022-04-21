from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton

from core import reboot_router


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        reboot_btn = MDFillRoundFlatButton(
            text='reboot',
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        reboot_btn.bind(on_press=lambda *args: reboot_router())
        screen.add_widget(reboot_btn)

        return screen


if __name__ == '__main__':
    MainApp().run()
