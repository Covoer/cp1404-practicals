from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometersApp(App):
    km_output = StringProperty()

    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles):
        try:
            miles = float(miles)
            kilometers = miles * 1.60934
            self.km_output = f"{kilometers:.2f} km"
        except ValueError:
            self.km_output = "Invalid input"

    def handle_increment(self, current_miles, increment):
        try:
            miles = float(current_miles) + increment
            self.root.ids.input_miles.text = str(miles)
        except ValueError:
            self.root.ids.input_miles.text = '0'


MilesToKilometersApp().run()
