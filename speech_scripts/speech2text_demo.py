# import speech_recognition as sr

# # for index, name in enumerate(sr.Microphone.list_microphone_names()):
# #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`\n\n".format(index, name))

# r = sr.Recognizer()
# mic = sr.Microphone(device_index=8, sample_rate = 44100, chunk_size = 512)
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)

# r.recognize_google(audio)


import speech_recognition as sr

print("say something1")
r = sr.Recognizer()
print("say something2")
with sr.Microphone() as source:                # use the default microphone as the audio source
    r.adjust_for_ambient_noise(source)
    print("say something3")
    # listen for the first phrase and extract it into audio data
    audio = r.listen(source, timeout=5)

print("say something")
try:
    # recognize speech using Google Speech Recognition
    print("You said " + r.recognize_google(audio))
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
