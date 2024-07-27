import json
import os

class QuizManager:
    def __init__(self):
        self.quizzes = {}
        self.load_quizzes()

    def load_quizzes(self):
        if os.path.exists('quizzes.json'):
            with open('quizzes.json', 'r') as file:
                self.quizzes = json.load(file)
    
    def save_quizzes(self):
        with open('quizzes.json', 'w') as file:
            json.dump(self.quizzes, file, indent=4)
    
    def create_quiz(self):
        quiz_name = input("\nEnter the name of the quiz: ")
        questions = []
        while True:
            question = input("\nEnter a question (or type 'done' to finish): ")
            if question.lower() == 'done':
                break
            options = []
            correct_option = None
            for i in range(4):
                option = input(f"Enter option {i + 1}: ")
                options.append(option)
            while correct_option not in [str(i + 1) for i in range(4)]:
                correct_option = input("\nEnter the correct option from (1-4): ")
            questions.append({
                'question': question,
                'options': options,
                'correct': int(correct_option) - 1
            })
        self.quizzes[quiz_name] = questions
        self.save_quizzes()
        print(f"\nQuiz '{quiz_name}' created successfully!")

    def list_quizzes(self):
        if not self.quizzes:
            print("\nNo quizzes available.")
        else:
            print("\nAvailable quizzes:")
            for i, quiz in enumerate(self.quizzes.keys(), 1):
                print(f"{i}. {quiz}")

    def take_quiz(self):
        self.list_quizzes()
        choice = int(input("\nSelect a quiz by number: "))
        quiz_name = list(self.quizzes.keys())[choice - 1]
        questions = self.quizzes[quiz_name]
        score = 0
        for i, q in enumerate(questions):
            print(f"\nQuestion {i + 1}: {q['question']}")
            for j, option in enumerate(q['options']):
                print(f"\n{j + 1}. {option}")
            answer = int(input("\nEnter the correct option from (1-4): "))
            if answer - 1 == q['correct']:
                print("\nCorrect!")
                score += 1
            else:
                print(f"\nWrong! The correct answer was: {q['options'][q['correct']]}")
        print(f"\nYou scored {score}/{len(questions)} on the quiz '{quiz_name}'.")

    def delete_quiz(self):
        self.list_quizzes()
        choice = int(input("Select a quiz to delete by number: "))
        quiz_name = list(self.quizzes.keys())[choice - 1]
        del self.quizzes[quiz_name]
        self.save_quizzes()
        print(f"\nQuiz '{quiz_name}' deleted successfully!")

def main():
    manager = QuizManager()
    while True:
        print("\nWelcome to the Online Quiz Platform!")
        print("\n1. Create a Quiz")
        print("2. Take a Quiz")
        print("3. List All Quizzes")
        print("4. Delete a Quiz")
        print("5. Exit\n")

        choice = input("Enter your choice: ")
        if choice == '1':
            manager.create_quiz()
        elif choice == '2':
            manager.take_quiz()
        elif choice == '3':
            manager.list_quizzes()
        elif choice == '4':
            manager.delete_quiz()
        elif choice == '5':
            print("\nGoodbye! 😀😀")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    
