# Flashy - A Spanish Flashcard App
Flashy is a simple Spanish flashcard application built using Python and the tkinter library. It allows users to learn Spanish vocabulary by presenting a Spanish word on one side of a flashcard, and the corresponding English translation on the other. Users can test their knowledge by clicking on one of two buttons - a "correct" button and a "wrong" button - and the application will automatically move on to the next flashcard.

## Features
* Randomly presents a Spanish word on one side of a flashcard, and the corresponding English translation on the other
* Users can test their knowledge by clicking on a "correct" or "wrong" button
* Automatically saves the list of words the user has not yet mastered, so they can continue to practice until they know them all
* If the user exits the application and comes back later, they can continue where they left off
## How to Use
### Prerequisites
Python 3.0 or higher
pandas library
### Installation
1. Clone this repository or download the ZIP file.
2. Install the pandas library using the following command:

``pip install pandas``

3. Navigate to the directory where you saved the code.
4. Run the following command to start the application:

``python flashcard.py``

5. Practice your Spanish vocabulary!
## Data
I used a list from Wikipedia of the 1000 most common words in Spanish, and I did the translation using the translation function in Google Sheets. The list of words and their English translations are stored in a CSV file.

## Credits
This project was completed as part of the "100 Days of Code" course. The course provided the basis for the application, which I then customized and added additional features to.
