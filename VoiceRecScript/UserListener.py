'''
UserListener class to parse user input using speech recognition APIs
'''

import speech_recognition as sprec

class UserListener:

    def stream(self):
        '''
        Returns the word stream of this UserListener
        '''
        return self._stream
    
    def __init__(self):
        '''
        Initializer
        '''

        self._rec = sprec.Recognizer()
        self._mic = sprec.Microphone()
        self._stream = None

    def userlisten(self):
        '''
        Uses speech_recognition.listen() method to take input from _mic
        and stores it in stream

        "with mic as source"

        !! Implement try-except block to handle unrecognized speech !!
        '''
        with self._mic as source:
            self._rec.adjust_for_ambient_noise(source)
            print("Speak:")
            audio = self._rec.listen(source)

            try:
                output = self._rec.recognize_google(audio)
                self._stream = output.lower()
            except sprec.UnknownValueError:
                print("Unrecognizable input")

    def isstart(self):
        '''
        Determines whether or not the command "start" was recently uttered
        '''
        pass

    def isstop(self):
        '''
        Determines whether or not the command "stop" was recently uttered
        '''
        pass

# FOR TESTING PURPOSES
# if __name__ == "__main__":
#     do = UserListener()
#     do.userlisten()
#     print(do.stream())