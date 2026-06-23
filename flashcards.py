import json
import random

def load_cards(filename):
    with open(filename, "r") as f:
        return json.load(f)

def run_quiz(cards):
    random.shuffle(cards)
    score = 0

    print("\n Welcome to Flashcards! Type your answer or 'skip' to skip.\n")

    for i, card in enumerate(cards):
        print(f"Q{i+1}: {card['question']}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == "skip":
            print(f"  Skipped! Answer was: {card['answer']}\n")
        elif user_answer == card["answer"].lower():
            print("  Correct!\n")
            score += 1
        else:
            print(f"  Not quite. Answer was: {card['answer']}\n")

    print(f"Quiz complete! Score: {score}/{len(cards)}")

if __name__ == "__main__":
    cards = load_cards("cards.json")
    run_quiz(cards)