from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
import random
from kivy.core.text import LabelBase
from kivy.graphics import Color, Rectangle

# Register the font
LabelBase.register(name='Roboto', fn_regular=r"C:\Users\DELL\PycharmProjects\pythonProject2\定位定级+应用2\JiZiJingDianWeiTiJianFan\JiZiJingDianWeiTiJianFan-Shan(GEETYPE-WeiTiGBT-Flash)-2.ttf")


class OptionBox(BoxLayout):
    def __init__(self, **kwargs):
        super(OptionBox, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0.75, 0.79, 1)  # Pink color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class RandomChooserApp(App):
    def build(self):
        self.options = []  # List to store options
        self.current_animation = None  # Variable to store current animation

        layout = BoxLayout(orientation='vertical')

        # Input box for entering options
        self.input_box = TextInput(hint_text='输入选项', size_hint=(1, 0.2), font_name='Roboto')
        layout.add_widget(self.input_box)

        # Button to add options
        add_button = CustomButton(text='添加选项', size_hint=(1, 0.2), font_name='Roboto')
        add_button.bind(on_press=self.add_option)
        layout.add_widget(add_button)

        # Button for random selection
        choose_button = CustomButton(text='随机选择', size_hint=(1, 0.2), font_name='Roboto')
        choose_button.bind(on_press=self.choose_random)
        layout.add_widget(choose_button)

        # ScrollView to display options with blue background
        self.scroll_view = ScrollView(size_hint=(1, 0.4))
        with self.scroll_view.canvas.before:
            Color(0, 0, 1, 1)  # Blue color
            self.bg_rect = Rectangle(size=self.scroll_view.size, pos=self.scroll_view.pos)
        self.options_layout = BoxLayout(size_hint_y=None, orientation='horizontal')
        self.options_layout.bind(minimum_height=self.options_layout.setter('height'))
        self.scroll_view.add_widget(self.options_layout)
        layout.add_widget(self.scroll_view)

        # Label to display the chosen option
        self.result_label = Label(text='随机选项会显示在这里', font_name='Roboto')
        layout.add_widget(self.result_label)

        return layout

    def add_option(self, instance):
        option = self.input_box.text.strip()
        if option:
            self.options.append(option)
            option_layout = OptionBox(size_hint_y=None, height=40)
            option_label = Label(text=option, font_name='Roboto')
            option_layout.add_widget(option_label)
            self.options_layout.add_widget(option_layout)
            self.input_box.text = ''

    def choose_random(self, instance):
        if self.options:
            if self.current_animation:
                self.current_animation.cancel_all(self.current_animation.widget)

            chosen_index = random.randint(0, len(self.options) - 1)
            chosen_option = self.options[chosen_index]
            containers = self.options_layout.children[::-1]
            chosen_container = containers[chosen_index]

            # Create and start the new animation
            anim = Animation(r=1, g=0, b=0, duration=0.5) + Animation(r=1, g=1, b=1, duration=0.5)
            anim.repeat = True
            anim.start(chosen_container.bg_color)
            self.current_animation = anim

            self.result_label.text = f'选择的选项: {chosen_option}'
        else:
            self.result_label.text = '没有选项可供选择'


if __name__ == '__main__':
    RandomChooserApp().run()
