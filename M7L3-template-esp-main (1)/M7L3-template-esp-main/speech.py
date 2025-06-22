import speech_recognition as speech_recog

def speech_en():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-GB")
    
"""mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()
with mic as audio_file:
    print("habla porfavor:)")
    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)
    print("comvirtiendo voz a texto")
    print("tu dijiste :/"+ recog.recognize_google(audio, language="en-GB"))"""