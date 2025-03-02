class QuizBrain:

	def __init__(self, question_list):
		self.score = 0
		self.question_number = 0
		self.question_list = question_list

	#TODO: 1. asking the questions
	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		print(f"Q{self.question_number}. {current_question.text}")
		user_answer = input("    (True/False) : ")
		self.check_answer(user_answer, current_question.answer)


	#TODO: 2. checking if the answer was correct
	def check_answer(self, user_answer, correct_answer):
		print("\n")
		if user_answer.lower() == correct_answer.lower():
			self.score += 1
			print("You got it right !")
		else:
			print("That's wrong.")
		print(f"Correct answer : {correct_answer}")
		print(f"Current score  : {self.score}")
		print("\n")


	#TODO: 3. checking if we're at the end of the quiz
	def still_has_question(self):
		return self.question_number < len(self.question_list)
