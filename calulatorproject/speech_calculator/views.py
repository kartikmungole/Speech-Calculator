from django.shortcuts import render
import speech_recognition as sr
import pyttsx3

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Error: Division by zero"

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.4)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language="en-US")
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Sorry, the service is unavailable."

def calculator_view(request):
    if request.method == "POST":
        operation = request.POST.get('operation')
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        
        operations = {
            "addition": add,
            "subtraction": subtract,
            "multiplication": multiply,
            "division": division
        }
        
        if operation in operations:
            result = operations[operation](num1, num2)
            speak(f"The result of {operation} is {result}")
            return render(request, 'index.html', {'result': result})
        else:
            return render(request, 'index.html', {'error': 'Invalid operation'})
    
    return render(request, 'index.html')

