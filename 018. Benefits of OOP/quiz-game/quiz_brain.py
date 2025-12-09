class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.q_number = 0
        self.q_list = q_list

    def still_has_question(self):
        num_of_question = len(self.q_list)
        if self.q_number < num_of_question:
            return True
        else:
            return False

    def n_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("\nYou're right!")
        else:
            print("\nSorry, it's wrong!")

        print(f"The correct answer was: {current_answer}")
        print(f"Your current score {self.score}/{self.q_number}\n")