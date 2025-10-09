import json
import random

class QuizEngine:
    def __init__(self, question_file):
        with open(question_file, "r") as file:
            self.questions = json.load(file)
        random.shuffle(self.questions)
        self.current = 0
        self.score = 0

    def get_next_question(self):
        if self.current < 10:
            return self.questions[self.current]
        return None

    def check_answer(self, selected):
        correct = self.questions[self.current]["answer"]
        explanation = self.questions[self.current]["explanation"]
        if selected == correct:
            self.score += 1
            result = True
        else:
            result = False
        self.current += 1
        return result, correct, explanation