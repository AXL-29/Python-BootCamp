class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.q_number = 0
        self.q_list = q_list

    def n_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        return user_answer, current_question

    def still_has_question(self):
        num_of_question = len(self.q_list)
        if self.q_number < num_of_question:
            return True
        else:
            return False

    def check_answer(self, user_answer, current_question):
        if user_answer == current_question.answer:
            self.score += 1
            print("You're right!")
        else:
            print("Sorry, it's wrong!")

        print(f"Your score {self.score}/{self.q_number}")
