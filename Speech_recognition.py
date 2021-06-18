#!/usr/bin/python

import sys
import os
import speech_recognition as sr

#path = sys.argv[1]
#LANG = sys.argv[2]

ScriptName =  os.path.basename(sys.argv[0])

def RecognizerFunction():
    # Check if path exits
    #if os.path.exists(path):

    recognizer = sr.Recognizer()

    ''' recording the sound '''

    #with sr.AudioFile("./speech.wav") as source:
    with sr.AudioFile(sys.argv[1]) as source:
        recorded_audio = recognizer.listen(source)
        print("Done recording")

    ''' Recorgnizing the Audio '''
    try:
        print ('Voice recognition in progress..')
        text = recognizer.recognize_google(
                recorded_audio, 
                #language="en-US"
                language="sys.argv[2]"
            )
        print("Decoded Text : {}".format(text))

    except Exception as ex:
        print(ex)

NbrArges = len(sys.argv)
if NbrArges == 3:
    RecognizerFunction()
else:
    print ('\n' +ScriptName+ ' <inputfile> <Language>')
    print ('\n  -> language list : en_US, fr_FR, ar_AE..\n')
    sys.exit()

