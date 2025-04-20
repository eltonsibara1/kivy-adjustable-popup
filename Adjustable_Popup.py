from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock

Builder.load_string('''
<CustomPopup>:
    padding: dp(10)
    spacing: dp(10)
    title:"• Terms and Condition •"
    title_align:"center"
    title_color:1,1,1,1
    #title_font:"font/bold_black_emoji.ttf"
    title_size:"18sp"
    auto_dismiss: False
    size_hint:0.7, None
    separator_height: 0
    background_color:(0.1145, 0.6353, 0.2196, 0.98)
    radius:[16,16,16,16]

    ScrollView:
        do_scroll_y:True
        size_hint_y:1
        BoxLayout:
            id: grid
            orientation: "vertical"
            spacing: dp(10)
            padding: dp(10)
            size_hint_y: None
            height: self.minimum_height
                    
            Label:
                id: lab
                text: "By signing up for [b][color=#FF0000]Afri Dating App[/color][/b], you agree to our [color=#00C9A7]Terms & Conditions[/color], including guidelines on respectful communication, data privacy, and service policies; visit the app menu for full details."
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                color:1,1,1,1
                halign:"left"
                valign:"middle"
                markup:True
                pos_hint: {'center_x': 0.5,'center_y': 0.5}

            Button:
                text: 'Capture 1'
                size_hint:1,None
                height: dp(48)

            Button:
                text: 'Capture 2'
                size_hint:1,None
                height: dp(48)
            
            # Add more buttons as needed
            # ...
''')

class CustomPopup(Popup):
    def __init__(self, **kwargs):
        super(CustomPopup, self).__init__(**kwargs)
        self.bind(on_open=self.adjust_popup_size)
        self.ids.grid.bind(minimum_height=self.adjust_popup_size)
        self.ids.grid.bind(minimum_width=self.adjust_popup_size)

    def adjust_popup_size(self, *args):
        max_height = Window.height * 0.8  # 80% of screen height
        self.height = min(self.ids.grid.height + dp(20) + dp(60), max_height)
        self.width = min(self.ids.grid.width + dp(20), Window.width * 0.8)  # Optional: 90% of screen width
        
class Kivy_Adjustable_Popup(BoxLayout):
    def open_pop(self):
        the_popup = CustomPopup()
        the_popup.open()

class KivyPopup(App):
    def build(self):
        return Kivy_Adjustable_Popup()

    def open_pop(self):
        the_popup = CustomPopup()
        the_popup.open()

    def on_start(self):
        self.open_pop()

KivyPopup().run()
