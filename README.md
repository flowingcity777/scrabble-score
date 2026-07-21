# Scrabble Score

## Overview

This project simulates a simplified Scrabble scoring system using Python.

The program builds a dictionary that maps each letter of the alphabet to its corresponding Scrabble point value, calculates the score of individual words, tracks player scores, and updates those scores as new words are played.

The project focuses on practicing dictionaries, dictionary comprehensions, loops, and reusable functions.

---

## Features

- Build a letter-to-point dictionary using a dictionary comprehension
- Calculate the score of any word
- Support uppercase and lowercase input
- Safely handle invalid characters using dictionary lookups
- Calculate each player's total score
- Update player scores when new words are played

---

## Technologies

- Python 3

---

## Concepts Practiced

- Dictionaries
- Dictionary comprehensions
- Functions
- Loops
- Lists
- String methods
- Iterating through dictionaries
- Data organization

---

## How It Works

### 1. Create a Scrabble dictionary

The program combines two lists (letters and point values) into a dictionary using `zip()` and a dictionary comprehension.

### 2. Score a word

Each character in a word is converted to uppercase and looked up in the dictionary. Invalid characters are safely ignored by assigning them zero points.

### 3. Calculate player scores

Each player's list of words is processed to calculate a total score.

### 4. Play a new word

The program allows a player to submit another word and automatically updates their score.

---

## Example Output

```text
Initial Scores:
{
    'player1': 29,
    'wordNerd': 32,
    'Lexi Con': 31,
    'Prof Reader': 25
}

player1 played HELLO.
Updated score: 37
```

---

## Skills Practiced

During this project I practiced:

- Working with dictionaries
- Building dictionary comprehensions
- Writing reusable functions
- Processing collections of data
- Updating dictionary values
- Using Python's built-in methods (`zip()`, `.items()`, `.get()`, `.upper()`)
- Organizing a small Python program

---

## What I Learned

This project strengthened my understanding of Python dictionaries and how they can be used to efficiently map data.

I also gained experience writing reusable functions, safely retrieving dictionary values with `.get()`, and organizing related data into nested dictionaries and lists.

---

## Future Improvements

Possible enhancements include:

- Validate player names before updating scores
- Display a leaderboard sorted by score
- Allow players to enter words interactively
- Support multiple rounds of play
- Save game results to a file
- Build a graphical user interface (GUI)

---

## About This Project

This project was completed as part of Codecademy's Python curriculum and enhanced with additional documentation, organization, and code review as part of my software development portfolio.
