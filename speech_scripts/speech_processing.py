import pyttsx3
import speech_recognition as sr


class Speak(object):
    def __init__(self, text):
        self.text = text
        self.engine = pyttsx3.init()
        # pyttsx3.engine.Engine.setPropertyValue(pyttsx3.voice.Voice(gender='female', age=25))
        # engine= pyttsx3.voice.Voice(gender='female', age=25, id)
        # print(engine.getProperty('voices'))
        self.engine.setProperty('voice', 'english+f5')
        self._rate = self.engine.getProperty('rate')
        # volume = engine.getProperty('volume')
        # print(volume)
        self.engine.setProperty('rate', self._rate-60)
        self.engine.setProperty('volume', 1.4)

    @property
    def say(self):
        self.engine.say(self.text)
        self.engine.runAndWait()


class Recognise(object):
    def __init__(self):
        self.r = sr.Recognizer()

    @property
    def recognise(self):
        # use the default microphone as the audio source
        with sr.Microphone(7) as source:
            self.r.adjust_for_ambient_noise(source)
            # listen for the first phrase and extract it into audio data
            self.audio = self.r.listen(source, timeout=5)

        print('Listening...')
        try:
            # recognize speech using Google Speech Recognition
            print("You said:  " + self.r.recognize_google(self.audio))
        except LookupError:                            # speech is unintelligible
            print("Could not understand audio")


if __name__ == "__main__":
    sp = Speak("Hi Kartikey! How can I help you today?")
    sp.say()

    re = Recognise()
    re.recognise
