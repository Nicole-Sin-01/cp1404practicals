"""
CP1404/CP5632 Practical
Modify Existing GUI Program

"""

from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print('greet')
        # Update the label text using input from the TextInput field
        input_text = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {input_text}"

    def handle_clear(self):
        # Clear the input text and the output label
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'

BoxLayoutDemo().run()
