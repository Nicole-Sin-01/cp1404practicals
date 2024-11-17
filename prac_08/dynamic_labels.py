"""
CP1404/CP5632 Practical
GUI program to handle dynamic labels
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    """App to demonstrate dynamic creation of labels based on a list of names"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Updated list with new items
        self.names = ["Apple", "Bottom", "Jeans", "Boots", "With", "The", "Fur"]

    def build(self):
        """Build the Kivy app"""
        self.title = "Dynamic Labels Demo"
        self.root = Builder.load_file('dynamic_labels.kv')

        # Dynamically create and add labels to the BoxLayout
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)  # Add the label to the BoxLayout

        return self.root

DynamicLabelsApp().run()
