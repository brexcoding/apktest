import os ,sys

from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.resources import resource_add_path, resource_find
from kivymd.toast import toast


KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "bundle test app ."



    MDFloatLayout:

        MDRoundFlatIconButton:
            pos_hint: {"center_x": .5, "center_y": .5}
            text:'  press '
            icon: "logo2.png"
        
    
'''

class brexcoding_tts(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Builder.load_string(KV)


if __name__ == '__main__':
    try:
        if hasattr(sys, '_MEIPASS'):
            resource_add_path(os.path.join(sys._MEIPASS))
        app = brexcoding_tts()
        app.run()
    except Exception as e:
        print(e)
        input("Press enter.")



'''
PyInstaller   --icon logo.ico  hello.py
--onedir --noconsole

PyInstaller --onedir --add-data "logo.png:." --icon logo.ico  hello.py



'''
