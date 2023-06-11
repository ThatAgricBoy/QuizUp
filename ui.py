from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from data import fetch_question_data
from question_model import Question
from quiz_brain import QuizBrain


class QuizInterface(BoxLayout):

    def __init__(self, question_bank, **kwargs):
        super(QuizInterface, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.quiz = QuizBrain(question_bank)
        self.cols = 2

        self.score_label = Label(text="Score: 0", color=(1, 1, 1, 1), halign='right', valign='top',
                                 text_size=(None, None), size_hint=(1, 1), height="48dp")
        self.add_widget(self.score_label)

        self.question_layout = GridLayout(cols=1, size_hint=(1, 0.7))
        self.add_widget(self.question_layout)

        self.question_text = Label(text="Some Question Text", color=(1, 1, 1, 1), halign='center', valign='middle',
                                   text_size=(self.width, None), size_hint_y=None)
        self.question_layout.add_widget(self.question_text)

        button_layout = GridLayout(cols=2, size_hint=(1, None), height="48dp")
        self.add_widget(button_layout)

        true_button = Button(text="True", background_color=(0, 0, 1, 1))
        true_button.bind(on_press=self.true_pressed)
        button_layout.add_widget(true_button)

        false_button = Button(text="False", background_color=(1, 0, 0, 1))
        false_button.bind(on_press=self.false_pressed)
        button_layout.add_widget(false_button)

        self.play_again_button = Button(text="Play Again", background_color=(0, 1, 0, 1))
        self.play_again_button.bind(on_press=self.play_again_pressed)
        self.play_again_button.opacity = 0  # Hide the button initially
        button_layout.add_widget(self.play_again_button)

        self.get_next_question()

    def get_next_question(self, *args):
        self.question_layout.background_color = (1, 1, 1, 1)  # Reset background color
        if self.quiz.still_has_questions():
            self.score_label.text = f"Score: {self.quiz.score}"
            self.question_text.text = self.quiz.next_question()
            self.play_again_button.opacity = 0  # Hide the button
        else:
            self.question_text.text = "You've reached the end of the quiz."
            self.play_again_button.opacity = 1  # Show the button
            self.quiz.score = 0  # Reset the score to zero

    # Reset answer feedback
        self.question_layout.background_color = (1, 1, 1, 1)  # Reset background color

    def true_pressed(self, *args):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self, *args):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.question_layout.background_color = (0, 1, 0, 1)
        else:
            self.question_layout.background_color = (1, 0, 0, 1)
        Clock.schedule_once(self.get_next_question, 1)

    def reset_quiz(self):
        self.quiz.score = 0
        self.quiz.question_number = 0
        question_data = fetch_question_data()
        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        self.quiz.question_list = question_bank
        self.get_next_question()

    def play_again_pressed(self, *args):
        self.reset_quiz()


class QuizApp(App):
    def build(self):
        question_data = fetch_question_data()  # Fetch new question data
        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)

        return QuizInterface(question_bank=question_bank)
