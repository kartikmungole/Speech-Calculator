## **Speech Calculator Using Django**
**Overview**:
The Speech Calculator is a Django-based web application that allows users to perform basic arithmetic operations using speech recognition and text-to-speech technologies. Users can interact with the application by speaking the desired operation and numbers, and the calculator will provide both visual and spoken feedback. It gives output in speech as well as it shows output on web page.


**Features**:
**Text-to-Speech**: The calculator speaks out the result of the calculations.
Basic Arithmetic Operations: Addition, Subtraction, Multiplication, and Division.
**Speech Recognition**: Perform calculations by speaking the desired operation and numbers.


**Requirements**:
* Python, 
* Django, 
* pyttsx3 library,
* speech_recognition library,


**Usage**:
Operation Input: Speak the operation you want to perform (e.g., "addition", "subtraction", "multiplication", "division").
Number Input: Speak the first and second numbers.
Result: The application will display the result on the webpage and speak it aloud.


**Example**:
Open the application.
Speak: "addition".
Speak: "5".
Speak: "3".
The application will display and say: "The result of addition is 8".


**Project Structure**:
* calculator/: Contains the Django app for the speech calculator.
* templates/calculator/: Contains HTML templates for the web interface.
* views.py: Contains the logic for handling speech recognition and arithmetic operations.
* urls.py: Maps URLs to views.
* requirements.txt: Lists the Python packages required to run the project.
