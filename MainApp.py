from kivy.config import Config
Config.set("graphics","width", 800)
Config.set("graphics","height", 500)
Config.set("graphics", "resizable", 0)
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")


if __name__ == "__main__":
    MainApp().run()