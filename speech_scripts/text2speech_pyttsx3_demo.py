import pyttsx3

engine = pyttsx3.init()
engine.say('Hi Kartikey! How are you today?')
engine.runAndWait()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


voiceEngine = pyttsx3.init()

rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')

print(rate)
print(volume)
print(voice)

newVoiceRate = 50
while newVoiceRate <= 300:
    voiceEngine.setProperty('rate', newVoiceRate)
    voiceEngine.say('Testing different voice rates.')
    voiceEngine.runAndWait()
    newVoiceRate = newVoiceRate+50

voiceEngine.setProperty('rate', 125)

newVolume = 0.1
while newVolume <= 1:
    voiceEngine.setProperty('volume', newVolume)
    voiceEngine.say('Testing different voice volumes.')
    voiceEngine.runAndWait()
    newVolume = newVolume+0.3


engine = pyttsx3.init()
# pyttsx3.engine.Engine.setPropertyValue(pyttsx3.voice.Voice(gender='female', age=25))
# engine= pyttsx3.voice.Voice(gender='female', age=25, id)
# print(engine.getProperty('voices'))
engine.setProperty('voice', 'english+f5')
rate = engine.getProperty('rate')
# volume = engine.getProperty('volume')
# print(volume)
engine.setProperty('rate', rate-60)
engine.setProperty('volume', 1.4)
engine.say('Hi Kartikey! How can I help you today?')
engine.runAndWait()
