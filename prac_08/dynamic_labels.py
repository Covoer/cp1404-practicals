from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels,kv')
        self.populate_names()
        return self.root

    def populate_names(self):
        names = ["Alice", "Bob", "Charlie", "Diana"]  # Your list of names
        for name in names:
            self.root.ids.main.add_widget(Label(text=name))


DynamicLabelsApp().run()
