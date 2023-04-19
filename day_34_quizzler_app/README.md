# Quiz Game

Quizzler is a simple quiz game built using Python and the Open Trivia Database API. The game presents the user with a series of multiple-choice questions, and the user's score is calculated based on how many questions they answer correctly.

This project was created as part of the "100 Days of Code" course, which teaches learners how to build real-world applications using Python.

## Requirements

To run this project, you will need Python 3.x and the following packages:

- requests
- tkinter

You can install these packages using pip, the Python package manager. Here's the command to install both packages:
pip install requests html


## Technical Details

The program is written in Python and uses the Open Trivia DB API to generate a list of true or false questions. The program is split into four files:

- main.py: The main entry point of the program. This file creates the question bank, quiz brain, and quiz interface objects.
- question_model.py: Defines the Question class, which represents a single true or false question.
- quiz_brain.py: Defines the QuizBrain class, which keeps track of the user's score and the current question.
- ui.py: Defines the QuizInterface class, which displays the current question and handles user input.

The QuizInterface class uses the tkinter module to create a graphical user interface.
It displays the current question as text and provides two buttons for the user to select "True" or "False".
After the user selects an answer, the program will provide feedback as to whether the answer was correct or not, and then move on to the next question.

### How to Play

When you run the main.py file, Quizzler will fetch 10 questions from the Open Trivia Database API and present them to the user.
The user can answer each question by clicking on either the "True" or "False" button.


## USAGE

Once the application is running, simply answer the true/false questions presented to you. 
The application will provide immediate feedback on the correctness of each answer. 
Once all questions have been answered, the final score will be displayed.

## CREDITS

This project was created as part of the "100 Days of Code" course by Angela Yu.
The course teaches learners how to build real-world applications using Python.

The questions in this game were sourced from the Open Trivia Database API. 
The API provides a free, open-source database of trivia questions that can be used in any application.

