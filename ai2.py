from tkinter import Tk, Label, PhotoImage, FLAT, Button
import speech_recognition as sr
import pyttsx3
import sympy as sp
from PIL import ImageTk, Image

root = Tk()
root.title("Calculator")
root.maxsize(400, 360)
root.geometry("400x360")

image = Image.open("bgx1.png")
resize_image = image.resize((750, 420))
img = ImageTk.PhotoImage(resize_image)

label6 = Label(image=img)
label6.image = img
label6.pack()

mic_img = Image.open("micx.png")
photo = ImageTk.PhotoImage(mic_img)
mic_img_label = Label(image=photo, bg='#040405')
mic_img_label.image = photo
mic_img_label.place(x=173, y=200)

r = sr.Recognizer()
my_mic_device = sr.Microphone(device_index=1)

with my_mic_device as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    r.energy_threshold = 1000

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def calculate(event=None):
    with my_mic_device as source:
        print("Say what you want to calculate....")
        audio = r.listen(source)

    my_string = r.recognize_google(audio)
    my_string = my_string.replace("x", "*")  # Replace "x" with "*"
    my_string = my_string.replace("mod", "%")  # Replace "mod" with "%"
    my_string = my_string.replace("Mod", "%")  # Replace "mod" with "%"

    print(my_string)

    try:
        expr = sp.sympify(my_string)  # Parse the expression
        result = expr.evalf()  # Evaluate the expression with a float result
        result_formatted = f"{result:.2f}"  # Format result with two decimal places
        print(result_formatted)
        engine.say("The result is " + result_formatted)
    except sp.SympifyError:
        print("Invalid expression")
        engine.say("Sorry, I couldn't understand the expression.")

    engine.runAndWait()



mic_img_label.bind('<Button-1>', calculate)

root.mainloop()
