import speech_recognition
import speech_recognition as sr

reco = sr.Recognizer()

while True:
    try:

        with speech_recognition.Microphone() as mic:

            reco.adjust_for_ambient_noise(mic, duration=0.2)
            audio = reco.listen(mic)
            text = reco.recognize_google(audio, language="pt-BR")
            text = text.lower()

            print(f"Texto reconhecido: {text}")

    except speech_recognition.UnknownValueError():
        reco = speech_recognition.Recognizer()
        continue
