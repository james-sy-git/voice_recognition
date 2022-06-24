"""
Scraper -- takes user input and does a google search
Class: Scraper
Responsibilities:
- uses the search query(s) from the UserListener to compile a searchable URL
- stores the searchable URL
- stores URLs of all reachable pages (e.g. all the results from the first page)
Collaborations: UserListener, AssistantFrame

https://www.geeksforgeeks.org/performing-google-search-using-python-code/

https://stackoverflow.com/questions/11513624/python-google-search-scraper-with-beautifulsoup

GO TO THE <A> TAG AND FIND ITS ACCOMPANYING <H3>
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

class Scraper:
    '''
    The web scraper
    '''
    # Immutable attributes:
    # attribute _query:
    # invariant: _query is a string received from UserListener (desired search key words in google)

    # attribute _results:
    # invariant: _results is a nested list of the _url and heading scraped from desired query search
    
    #attribute _url:
    #invariant" _url is a string in correct https formatting using _query

    def set_query(self, new_query):
        '''
        Inserts a new search query
        '''

        self._query = new_query

    def results(self):
        '''
        Returns the dictionary of search result titles and URLs
        GOES TO TEXTTOSPEECH
        '''

        return self._results

    def __init__(self, query):
        '''
        Initializer
        '''

        self._query = query # safe get method from class UserListener
        self._results = {} # or None depending on how we do it
        self._url = self.createURL() # url used in search method created using speech to text input by user

    def createURL(self):
        '''
        Modifies self._url according to the search query
        THIS USES SELF._URL
        '''

        stub = 'https://www.google.com/search?q='

        search = stub + self.googlify()

        return search

    def googlify(self):
        '''
        Creates a string that can be attached to a stub
        ex. "Michelle Obama" becomes "Michelle+Obama"
        '''

        pass

    def read(self):
        '''
        reads a url
        '''

        page = urlopen(self._url)

        bytes = page.read()
        html = bytes.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        return soup

    def search_urls(self, num_results):
        '''
        Searches google using the search query
        Returns a dictionary with the title and the URL
        '''

        pass

    def clear(self):
        '''
        Clears the dictionary
        '''

        self._results = {}
