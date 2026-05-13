from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
import random
from kivy.animation import Animation
import numpy as np
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
# Register the font
import os  # 导入 os 模块
# 注册字体
from kivy.core.text import LabelBase
LabelBase.register(name='Roboto', fn_regular=r"C:\Users\DELL\PycharmProjects\pythonProject2\定位定级+应用2\JiZiJingDianWeiTiJianFan\JiZiJingDianWeiTiJianFan-Shan(GEETYPE-WeiTiGBT-Flash)-2.ttf")

class OptionBox(BoxLayout):
    def __init__(self, **kwargs):
        super(OptionBox, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg_color = Color(0.678, 0.847, 0.902, 1)  # 浅蓝色
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def set_background_color(self, color):
        self.bg_color.rgba = color


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

class EatWhatApp(App):
    def build(self):
        self.options = []  # List to store options and probabilities
        self.current_animation = None  # Variable to store current animation
        self.currently_animated_widget = None  # Variable to store the currently animated widget
        self.max_options_per_row = 5  # 每行最大选项数量
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Input layout for options and probabilities
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        # Input box for entering options
        self.input_box = TextInput(hint_text='输入店名', size_hint=(0.7, 1), font_name='Roboto')
        input_layout.add_widget(self.input_box)

        # Input box for entering probabilities
        self.probability_box = TextInput(hint_text='欲望(百分制)', size_hint=(0.3, 1), font_name='Roboto', input_filter='float')
        input_layout.add_widget(self.probability_box)

        layout.add_widget(input_layout)

        # Button to add options
        add_button = CustomButton(text='添加', size_hint_y=None, height=40, font_name='Roboto')
        add_button.bind(on_press=self.add_option)
        layout.add_widget(add_button)

        # Button for random selection
        choose_button = CustomButton(text='点这里看去哪吃', size_hint_y=None, height=50, font_name='Roboto')
        choose_button.bind(on_press=self.choose_random)
        layout.add_widget(choose_button)

        # Container for displaying options
        self.options_layout = GridLayout(cols=5, size_hint_y=None, row_default_height=40, row_force_default=True)
        layout.add_widget(self.options_layout)

        # Label to display the chosen option
        self.result_label = Label(text='今天去哪儿吃？', font_name='Roboto')
        layout.add_widget(self.result_label)

        self.load_options()

        return layout

    def add_option(self, instance):
        option = self.input_box.text.strip()
        probability_text = self.probability_box.text.strip()
        probability = float(probability_text) if probability_text else 1  # Default probability is 1

        if option:
            self.options.append((option, probability))

            option_layout = OptionBox(size_hint=(1, None), height=40)
            option_label = Label(text=option, font_name='Roboto', color=[0, 0, 0, 1])
            option_layout.add_widget(option_label)
            self.options_layout.add_widget(option_layout)

            # Adjust container height
            if len(self.options_layout.children) % 5 == 0:
                self.options_layout.height = 40 * (len(self.options_layout.children) // 5)

            self.input_box.text = ''
            self.probability_box.text = ''

    def choose_random(self, instance):
        if self.options:
            # Reset all option background colors
            for child in self.options_layout.children:
                if isinstance(child, OptionBox):
                    child.set_background_color((0.678, 0.847, 0.902, 1))  # Set to light blue
            options, probabilities = zip(*self.options)
            total = sum(probabilities)
            probabilities = [p / total for p in probabilities]  # Normalize probabilities
            chosen_option = np.random.choice(options, p=probabilities)
            chosen_option_layout = None
            for option_layout in self.options_layout.children[::-1]:  # 从最后一行开始
                if chosen_option in [child.text for child in option_layout.children]:
                    chosen_option_layout = option_layout
                    break
                    # If found, start animation
            if chosen_option_layout:
                if self.current_animation and self.currently_animated_widget:
                    self.current_animation.cancel_all(self.currently_animated_widget)

                anim = Animation(r=1, g=0.75, b=0.79, duration=0.5) + Animation(r=0.89, g=0.847, b=0.2,
                                              duration=1)
                anim.repeat = True
                anim.start(chosen_option_layout.bg_color)
                self.current_animation = anim
                self.currently_animated_widget = chosen_option_layout.bg_color

                self.result_label.text = f'去这儿吃：{chosen_option}'

        else:
            self.result_label.text = '没有地点可供选择'
    def _update_scroll_view_rect(self, instance, value):
        self.bg_rect.size = instance.size



    def on_stop(self):
        # 保存选项
        self.save_options()

    def check_options_folder(self):
        # 获取当前工作目录
        current_directory = os.getcwd()

        # 创建选项数据保存文件夹
        options_folder = os.path.join(current_directory, "options_data")

        if not os.path.exists(options_folder):
            os.makedirs(options_folder)

        # 设置选项数据文件的路径
        self.options_file = os.path.join(options_folder, "options.txt")

    def save_options(self):
        self.check_options_folder()

        with open(self.options_file, "w") as file:
            for option, probability in self.options:
                file.write(f"{option}:{probability}\n")

    def load_options(self):
        self.check_options_folder()

        if os.path.exists(self.options_file):
            with open(self.options_file, "r") as file:
                loaded_options = [line.strip() for line in file.readlines()]

            for entry in loaded_options:
                if ':' in entry:  # 确保格式正确
                    option, probability = entry.split(':', 1)
                    self.input_box.text = option
                    self.probability_box.text = probability
                    self.add_option(None)  # 添加选项
                    self.input_box.text = ''  # 清空输入框
                    self.probability_box.text = ''  # 清空概率输入框


if __name__ == '__main__':
    EatWhatApp().run()