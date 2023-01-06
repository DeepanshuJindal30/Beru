# Beru

The script starts by importing the necessary libraries:

datetime is imported for manipulating dates and times.

pyttsx3 is imported for converting text to speech.

speech_recognition is imported for performing speech recognition (transcribing spoken words into text).

pyaudio is imported for working with audio streams.

The script initializes the text-to-speech engine using pyttsx3 and sets various properties such as the voice to use and the speaking rate.

The speak(text) function is defined to convert the given text into speech using the pyttsx3 library.

The take() function is defined to record audio from the microphone, transcribe it into text using the speech_recognition library, and return the transcribed text. If there is an error during transcription, the function prompts the user to enter their command manually.

The Greetings() function is defined to greet the user based on the current time and tell the user the current time. The function uses the datetime library to get the current time and then uses pyttsx3 to speak the greeting and the current time.

The script defines the Introduction string, which contains a message introducing the script.

The script calls the Greetings() function to greet the user and enters a loop where it continually waits for the user to speak a command.

If the user says "go back", the loop breaks and the script ends.

If the user says "none", the loop continues without doing anything.

Otherwise, the script speaks the command back to the user using the speak(text) function.
