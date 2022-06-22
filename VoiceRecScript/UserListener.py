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

        self.rec = sprec.Recognizer()
        self._mic = sprec.Microphone()
        self._stream = None

    def listen(self):
        '''
        Uses speech_recognition.listen() method to take input from _mic
        and stores it in stream

        "with mic as source"

        !! Implement try-except block to handle unrecognized speech !!
        '''
        pass

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