# Voice-Activated Notepad and Dictionary App

This Python application provides a GUI-based voice-activated Notepad and dictionary tool. Users can choose to either dictate text, which is automatically typed into Notepad, or say a word to retrieve its definition. The program features automatic detection of speech, as well as timeouts for no input.

## Features

- **Option Selection Interface**: The GUI interface lets users select between two functions:
  - **Option 1**: Speech-to-text entry into Notepad.
  - **Option 2**: Voice-activated dictionary lookup.
- **Automatic Restart**: If no input is detected within a specified time frame, the program will restart to the initial options.
- **Enhanced Speech Recognition**: Captures speech input with up to 80% accuracy.
- **Timeout and Retry Handling**: Automatically closes and restarts upon prolonged silence to keep the app responsive.

## Usage
Upon running the application, you will be presented with the following options:
- **Option 1**: Save speech to a text file (Notepad): Dictate your speech, and it will be typed out in a new Notepad window.
- **Option 2**: Search the meaning of a word: Speak the word you want to search, and the app will retrieve its meaning.

The program also restarts automatically if no voice input is detected for a set period, ensuring it remains responsive.

## Troubleshooting

### Issue 1: Speech Recognition Accuracy
If the speech-to-text recognition is not capturing the speech correctly, make sure that:
- The microphone is working properly and has the correct input settings.
- The ambient noise is minimized.
- Speak clearly and at a moderate pace.

### Issue 2: No Response or Delay in Meaning Lookup
The delay in finding the meaning of a word may be due to the API or internet connection issues. If it takes too long, ensure:
- You have a stable internet connection.
- The dictionary API service is operational.

### Issue 3: Program Not Closing
If the program does not close after the timeout or fails to restart:
- Ensure that the program is not running in an infinite loop due to a manual input error.
- If the issue persists, try restarting the program manually.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

### How to Contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
