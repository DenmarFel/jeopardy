# Jeopardy Game

## Demo
![](example.gif)

## Inspiration
For game night, our friend group wanted to play Jeopardy with our own questions. This mini project made game setup easy. Questions were written on an excel sheet which was then converted to a CSV file. This flask app automatically parses those questions from the CSV file to construct the Jeopardy board.

## Instructions
1. Enter your categories and questions in the Jeopardy_Template excel file
2. Convert the excel file to a CSV in uploads folder.
3. Setup flask app.

- On Mac/Linux: `export FLASK_APP=main.py`
- On Windows 10 Command Prompt: `set FLASK_APP=main.py`
- On Windows 10 Powershell: `$env:FLASK_APP = "main.py"`

4. Run Flask App: `flask run`
5. Go to http://localhost:5000/ and upload CSV from uploads folder.
6. Play! Try projecting your screen to a TV or projector for a more entertaining experience.
