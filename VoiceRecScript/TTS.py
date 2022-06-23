'''
Text to Speech
'''

import pyttsx3 as pt # better than google TTS because it's offline

class TTS:

    def advance(self):
        self._index = self._index + 1
    
    def __init__(self, list):
        '''
        Initializer
        Docket: the list of website titles to be said
        Voice: the pyttsx3 text to speech engine
        '''
        self._docket = list
        self._voice = pt.init()
        self._index = 0

    def push(self, thing_to_say):
        '''
        Adds something to say to the docket
        '''
        assert(isinstance(thing_to_say, str))
        self._docket.append(thing_to_say)

    def utter(self):
        '''
        Says the string at the _indexth index of _docket
        '''
        self._voice.say(self._docket[self._index])
        self._voice.runAndWait()



