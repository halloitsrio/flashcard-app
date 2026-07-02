# CLI Flashcard Quiz App

A command-line flashcard application built in Python that loads question sets from JSON files, randomizes card order, and tracks your score across a session.

## Features
- Loads flashcard decks from JSON files — easy to add new topics
- Randomizes card order each session
- Tracks score and shows the correct answer on wrong/skipped cards
- Clean, interactive CLI interface

## Tech Stack
- Python 3
- JSON

## How to Run

1. Clone the repo:
      git clone https://github.com/halloitsrio/flashcard-app.git
      cd flashcard-app

2. Run the app:
      python flashcards.py

## Adding Your Own Cards
Open `cards.json` and add entries in this format:
```json
[
    {"question": "Your question here?", "answer": "Your answer here"}
]
```

## Example Session
Q1: What does CPU stand for?

Your answer: central processing unit

✓ Correct!
Q2: What is a loop in programming?

Your answer: skip

Skipped! Answer was: A block of code that repeats until a condition is met
Quiz complete! Score: 1/2

## What I Learned
- File I/O and JSON parsing in Python
- Modular program design
- Building interactive CLI tools
- Data structure design for extensibility
