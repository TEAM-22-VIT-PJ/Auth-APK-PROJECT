from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size=(412,732)
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')
    def logger(self):
        self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
        global u_ser
        global passwd
        u_ser=self.root.ids.user.text
        passwd=self.root.ids.password.text
        print(u_ser,passwd)
    def clear(self):
        self.root.ids.welcome_label.text = "WELCOME"
        self.root.ids.user.text = ''
        self.root.ids.password.text = ""
    

MainApp().run()