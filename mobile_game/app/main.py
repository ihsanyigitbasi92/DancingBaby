from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from game import Game

class MobileGameApp(App):
    def build(self):
        self.game = Game()
        layout = BoxLayout(orientation='vertical')
        self.score_label = Label(text="Score: 0")
        start_button = Button(text="Start/Restart")
        start_button.bind(on_press=self.start_game)
        layout.add_widget(self.score_label)
        layout.add_widget(start_button)
        return layout

    def start_game(self, instance):
        self.game.start()
        self.update_score()

    def update_score(self):
        self.score_label.text = f"Score: {self.game.score}"

if __name__ == '__main__':
    MobileGameApp().run()
