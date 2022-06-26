"""
Class: Controller
Responsibilites:
- control microphone useage (on and off when key words detected in microphone class)
- create scraper instance after key word detected from microphone
- create text to speech instance using scraper data

"""

from Scraper import *
from TTS import *
from UserListener import *

class Controller:

    def __init__(self):
        '''
        initilizer for controller
        '''
        self.query = None #query gotten from UserListener and used in Scraper
        self._state = 0 #state of controller: 0 = waiting for start, 1 = start detected + listening for input, 2 = scrape + get urls, 3 = speak url + header to user, 4 = user input, 5 = go in to url and read body
        self.urls = None #list of urls created from scraper, used in text to speech
        self.listen = UserListener()
        self.scrape = Scrape(self.urls)
        self.speak = TTS(self.urls)

    def update(self):
        '''
        updates the controller + terminates when user says 'stop'
        '''
        self.determineState()

        if self.listen.isstop():
            return


    def determineState(self):
        '''
        determines state of controller
        '''
        if self._state == 0:
            if self.listen.isstart() == True:
                self._state = 1
        elif self._state == 1:
            self.record()
        elif self._state == 2:
            self.scraping()
        elif self._state == 3:
            self.feedback()
        elif self._state == 4:
            self.questionUser()
        elif self._state == 5:
            self.readbody()

    def record(self):
        '''
        sets users input into query
        '''
        self.listen.userlisten()
        self.query = self.listen.stream()
        self._state = 2

    def scraping(self):
        '''
        uses query varible from state 1 to create list of urls and headers
        '''
        self.scrape.createURL()
        self.scrape.read
        self.urls = self.scrape.search_urls(10)
        self._state = 3

    def feedback(self):
        '''
        speaks first url and header to user, inciments list index by 1
        '''
        self.speak.utter()
        self.speak.advance()
        self._state = 4

    def questionUser(self):
        '''
        asks user if they want to go into the url
        if yes, reads body of desired url
        if no, goes reads next url
        '''
        self.speak.question()
        if self.listen.YesorNO(): #if user says Yes (return True) move to state 5, if no (False) go back to state 3 to reach next url + ask again
            self._state = 5
        else:
            self._state = 3

    def readbody(self):
        '''
        reads body of the desired url
        '''
        self.speak.push(self.speak.getBodyofURL()) #implement getting body
        self.speak.utter() #need method to read last in list to get the body or one that clears dockett before the push
