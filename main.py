from kivy.app import App
from kivy.config import Config


class RecorderApp(App):
    pass


if __name__ == '__main__':
    Config.set('graphics', 'width', 960)
    Config.set('graphics', 'height', 540)

    RecorderApp().run()
