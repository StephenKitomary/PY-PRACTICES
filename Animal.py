# Initial list of questions, answers, and animals
questions = [
    "Does the animal you are thinking of have four legs?",
    "Is the animal you are thinking of large and gray?"
]

# Initial animals corresponding to answers for each question
animals = {
    (0, "yes"): {
        (1, "yes"): "elephant",
        (1, "no"): "cow"
    },
    (0, "no"): "fish"
}

def ask_yes_no(question):
    """Ask a yes or no question and return True for yes, False for no.
    If the user types 'list', print the known animals.
    If the user types 'dict' or 'questions', print the dictionary or list of questions for troubleshooting."""
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer == "list":
            print_known_animals(animals)
        elif answer == "dict":
            print("Current dictionary (animals):", animals)
        elif answer == "questions":
            print("Current list of questions:", questions)
        elif answer.startswith("y"):
            return True
        elif answer.startswith("n"):
            return False
        else:
            print("Please answer with 'yes', 'no', or 'list'.")

def print_known_animals(animals_dict):
    """Recursively prints all known animals in the dictionary."""
    known_animals = set()
    
    def find_animals(branch):
        if isinstance(branch, str):
            known_animals.add(branch)
        elif isinstance(branch, dict):
            for key in branch:
                find_animals(branch[key])

    find_animals(animals_dict)
    print("Known animals:", ", ".join(sorted(known_animals)))

def play_game():
    print("Hi! I'm an animal guesser.")
    print("Think of an animal, and I will try to guess it.")
    
    while True:
        # Start at the first question and follow the responses
        current_question_index = 0
        current_answers = animals
        parent_branch = None
        response_key = None
        
        while isinstance(current_answers, dict):
            # Ask the current question
            answer = ask_yes_no(questions[current_question_index])
            response_key = (current_question_index, "yes" if answer else "no")
            
            # Keep track of the parent branch and response key in case we need to modify it
            parent_branch = current_answers
            if response_key in current_answers:
                current_answers = current_answers[response_key]
                current_question_index += 1
            else:
                break
        
        # Final check: If we guessed correctly, celebrate; otherwise, learn new information
        if isinstance(current_answers, str):
            if ask_yes_no(f"Is your animal a {current_answers}?"):
                print("Yay! I guessed it!")
            else:
                learn_new_animal(parent_branch, response_key, current_answers)
        else:
            print("I couldn't guess the animal.")
        
        # Ask if the user wants to play again
        if not ask_yes_no("Would you like to play again?"):
            print("Thanks for playing!")
            break

def learn_new_animal(parent_branch, response_key, guessed_animal):
    """Learn a new animal if the guess was wrong."""
    new_animal = input("What was your animal? ").strip().lower()
    new_question = input(f"What question could distinguish {new_animal} from {guessed_animal}? ").strip()
    answer_for_new_animal = ask_yes_no(f"For a {new_animal}, would the answer to '{new_question}' be yes?")

    # Add the new question to the questions list
    questions.append(new_question)
    new_question_index = len(questions) - 1

    # Create a new branch for the new question with both the old and new animals as options
    parent_branch[response_key] = {
        (new_question_index, "yes" if answer_for_new_animal else "no"): new_animal,
        (new_question_index, "no" if answer_for_new_animal else "yes"): guessed_animal
    }
    print("Thank you! I've learned something new.")

# Start the game
play_game()
