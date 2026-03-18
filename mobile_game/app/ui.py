from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class GameUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.score_label = Label(text="Score: 0")
        self.start_button = Button(text="Start/Restart")
        self.add_widget(self.score_label)
        self.add_widget(self.start_button)

    def update_score(self, score):
        self.score_label.text = f"Score: {score}"
