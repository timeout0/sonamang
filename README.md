### Flask Game App
Welcome to the Flask Game App! This project is a simple web application built using the Flask framework. It includes functionality for managing game difficulty levels, recording scores, and displaying leaderboards.

### Pages
+ Title Page: The last score and leaderboards for different difficulty levels.
+ Game Page: Gameplay.

### File Structure
app2.py: Main Flask application file.
templates/: Directory containing HTML templates.
home.html: HTML and title page scripts.
game.html: HTML and gameplay mechanics scripts.
scores1.txt, scores2.txt, scores3.txt: Text files storing scores for different difficulty levels.
lst1.txt, lst2.txt, lst3.txt: Text files containing word lists for different difficulty levels.

### Setup and Installation, prerequisites
+ Python 3.12 or greater
+ Flask 3.0.3 or greater

### Installation
+ Clone the repository
+ Use virtual environment if needed: python3 -m venv venv
+ Install Flask: pip install Flask

### Running the App
+ Run app2.py
+ Open your web browser and navigate to http://127.0.0.1:5000/ to view the application.

### Usage
# Homepage
+ Last Score: The last score is displayed at the top of the page.
+ Game Launch buttons: easy, middle and hard difficulty.
+ Scores: All scores are displayed at the bottom of the in a descending order.
# Game Page
+ The game asks to enter the displayed word.
+ If a player enters the displayed word incorrectly, then the player does not get a point.
+ If a player enters the displayed word correctly, then the player gets a point and the word is removed from the display.
+ After every X seconds the game adds another word to the display.
+ If the number of words on the display reaches four, then the game will end and the player will be directed to the home page. The player's last score will be displayed on the top of the page.

### License
+ This project is licensed under the MIT License.

Copyright (c) 2024 Henri Roger Luhala

Copyright (c) 2024 Oliver Sõmera

Copyright (c) 2024 Aleksander Nikitin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
