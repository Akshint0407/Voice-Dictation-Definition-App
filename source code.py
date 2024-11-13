import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import threading
import time
import sys
from PyDictionary import PyDictionary
import requests

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech-to-Text with Options")
        self.dictionary = PyDictionary()
        self.recognizer = sr.Recognizer()
        self.should_exit = False  # Flag to control the exit behavior
        self.setup_gui()

    def setup_gui(self):
        # Clear previous GUI components if restarting
        for widget in self.root.winfo_children():
            widget.destroy()

        # Instruction Label
        self.label = tk.Label(self.root, text="Choose an option:")
        self.label.pack(pady=10)

        # Option Buttons
        self.option1_button = tk.Button(self.root, text="1. Save speech to a text file (Notepad)", command=self.option1)
        self.option1_button.pack(pady=5)

        self.option2_button = tk.Button(self.root, text="2. Search the meaning of a word", command=self.option2)
        self.option2_button.pack(pady=5)

        # Close Button
        self.close_button = tk.Button(self.root, text="Close Program", command=self.close_program)
        self.close_button.pack(pady=5)

    def option1(self):
        # Start a thread for option 1 to avoid blocking the GUI
        threading.Thread(target=self.start_notepad_typing).start()

    def option2(self):
        # Start a thread for option 2 to avoid blocking the GUI
        threading.Thread(target=self.search_word_meaning).start()

    def start_notepad_typing(self):
        try:
            import pyautogui, subprocess
            subprocess.Popen("notepad.exe")
            time.sleep(1)
            print("Listening for speech to type in Notepad...")

            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                
                while not self.should_exit:
                    try:
                        audio = self.recognizer.listen(source, timeout=10)
                        text = self.recognizer.recognize_google(audio)
                        print(f"You said: {text}")
                        pyautogui.typewrite(text + "\n")
                    except sr.WaitTimeoutError:
                        print("No input detected for 5 seconds. Restarting...")
                        self.setup_gui()
                        break
                    except sr.UnknownValueError:
                        print("Could not understand the audio. Listening again...")

        except Exception as e:
            print(f"Error in Notepad typing: {e}")

    def search_word_meaning(self):
        try:
            with sr.Microphone() as source:
                print("Listening for a word to search its meaning...")
                self.recognizer.adjust_for_ambient_noise(source)
                
                while not self.should_exit:
                    try:
                        audio = self.recognizer.listen(source, timeout=10)
                        word = self.recognizer.recognize_google(audio)
                        print(f"Searching meaning for: {word}")
                        
                        # Get the meaning of the word
                        meaning = self.get_meaning(word)
                        if meaning:
                            messagebox.showinfo("Word Meaning", f"Meaning of '{word}': {meaning}")
                        else:
                            messagebox.showinfo("Word Meaning", f"Could not find the meaning for '{word}'.")

                    except sr.WaitTimeoutError:
                        print("No input detected. Restarting...")
                        self.setup_gui()
                        break
                    except sr.UnknownValueError:
                        print("Could not understand the audio. Restarting...")
                        self.setup_gui()
                        break

        except Exception as e:
            print(f"Error in word meaning search: {e}")

    def get_meaning(self, word):
        try:
            meaning = self.dictionary.meaning(word)
            if meaning:
                return "\n".join([f"{k}: {', '.join(v)}" for k, v in meaning.items()])
            return None
        except requests.RequestException as e:
            print(f"Network error: {e}")
            return "Network error. Please check your connection."

    def close_program(self):
        self.should_exit = True  # Set exit flag to true to terminate any ongoing processes
        self.root.destroy()
        sys.exit()  # Forcefully exit the program

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()
