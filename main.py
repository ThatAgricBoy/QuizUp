from kivy.core.window import Window
from ui import QuizApp

minimum_width = 300
minimum_height = 500

Window.minimum_width = minimum_width
Window.minimum_height = minimum_height

quiz_app = QuizApp()
quiz_app.run()

if __name__ == '__main__':
    QuizApp().run()
