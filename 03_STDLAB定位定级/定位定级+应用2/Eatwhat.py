from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import random
from kivy.core.text import LabelBase
LabelBase.register(name='Roboto', fn_regular=r"C:\Users\DELL\PycharmProjects\pythonProject2\定位定级+应用2\JiZiJingDianWeiTiJianFan\JiZiJingDianWeiTiJianFan-Shan(GEETYPE-WeiTiGBT-Flash)-2.ttf")
class RandomChooserApp(App):
    def build(self):
        self.options = []  # 用于存储选项的列表

        layout = BoxLayout(orientation='vertical')

        # 输入框，用于输入选项
        self.input_box = TextInput(hint_text='输入选项', size_hint=(1, 0.2), font_name='Roboto')
        layout.add_widget(self.input_box)

        # 添加选项的按钮
        add_button = Button(text='添加选项', size_hint=(1, 0.2), font_name='Roboto')
        add_button.bind(on_press=self.add_option)
        layout.add_widget(add_button)

        # 随机选择的按钮
        choose_button = Button(text='随机选择', size_hint=(1, 0.2), font_name='Roboto')
        choose_button.bind(on_press=self.choose_random)
        layout.add_widget(choose_button)

        # 显示选中选项的标签
        self.result_label = Label(text='随机选项会显示在这里', font_name='Roboto')
        layout.add_widget(self.result_label)

        return layout

    def add_option(self, instance):
        option = self.input_box.text.strip()
        if option:
            self.options.append(option)
            self.input_box.text = ''  # 清空输入框

    def choose_random(self, instance):
        if self.options:
            chosen_option = random.choice(self.options)
            self.result_label.text = f'选择的选项: {chosen_option}'
        else:
            self.result_label.text = '没有选项可供选择'


if __name__ == '__main__':
    RandomChooserApp().run()
