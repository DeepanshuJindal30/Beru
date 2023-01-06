# Beru

Beru is a personal voice assistant designed to help users streamline their daily tasks and access information quickly and easily. With Beru, users can simply speak their requests or commands, and Beru will respond with the requested information or perform the desired action.

The script starts by importing the necessary libraries:

1. **datetime** is imported for manipulating dates and times.

2. **pyttsx3** is imported for converting text to speech.

3. **speech_recognition** is imported for performing speech recognition (transcribing spoken words into text).

4. **pyaudio** is imported for working with audio streams.

5. The script initializes the text-to-speech engine using **pyttsx3** and sets various properties such as the voice to use and the speaking rate.

6. The **speak(text)** function is defined to convert the given text into speech using the pyttsx3 library.

7. The **take()** function is defined to record audio from the microphone, transcribe it into text using the speech_recognition library, and return the transcribed text. If there is an error during transcription, the function prompts the user to enter their command manually.

8. The **Greetings()** function is defined to greet the user based on the current time and tell the user the current time. The function uses the datetime library to get the current time and then uses pyttsx3 to speak the greeting and the current time.

9. The script defines the Introduction string, which contains a message introducing the script.

10. The script calls the **Greetings()** function to greet the user and enters a loop where it continually waits for the user to speak a command.

11. If the user says **"go back"**, the loop breaks and the script ends.

13. If the user says **"none"**, the loop continues without doing anything. Otherwise, the script speaks the command back to the user using the speak(text) function.
