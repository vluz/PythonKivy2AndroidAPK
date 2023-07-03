from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard


class MainApp(App):


    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        Window.clearcolor = (0.071, 0.071, 0.071, 1)
        self.title = 'Calculator'
        main_layout = BoxLayout(orientation="vertical", padding=[10, 10, 10, 10], spacing=10)
        self.solution = TextInput(foreground_color=[0.267, 0.541, 1, 1], background_color=[0, 0, 0, 1], border=(0, 0, 0, 0),
                                  focus=False, multiline=False, readonly=True, halign="right", font_size=55)
        self.solution.bind(on_double_tap=self.on_double_tap)
        main_layout.add_widget(self.solution)
        buttons = [["7", "8", "9", "÷"],
                   ["4", "5", "6", "×"],
                   ["1", "2", "3", "−"],
                   [".", "0", "C", "+"],]
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=55, color=[0.502, 0.847, 1, 1], background_color=[0.38, 0.38, 0.38, 1])
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=55, color=[0.502, 0.847, 1, 1], background_color=[0.38, 0.38, 0.38, 1])
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        return main_layout


    def on_double_tap(self, instance):
        self.solution.select_all()
        Clipboard.copy(self.solution.text)


    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators


    def on_solution(self, instance):
        text = self.solution.text
        if text:
            exchange = {"÷": "/", "×": "*", "−": "-", "+": "+"}
            for char in exchange.keys():
                text = text.replace(char, exchange[char])
            try:
                solution = str(eval(text))
            except:
                solution = "ERROR"
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()
