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

GO TO THE <A> (Hyperlink) TAG AND FIND ITS ACCOMPANYING <H3> (Heading)

need to use list instead of dictionary to maintain Google's result priority and valuation
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

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

    def geturl(self):
        '''
        Returns this Scraper's URL
        '''
        return self._url

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
        self._results = [] # a nested list
        self._titles = []
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

        qu = self._query.replace(' ', '+')
        return qu


    def read(self):
        '''
        Creates a BeautifulSoup object for this Scraper's URL
        '''

        req = Request(self._url, headers={'User-Agent': 'Mozilla/5.0'}) # https://stackoverflow.com/questions/16627227/problem-http-error-403-in-python-3-web-scraping
        page = urlopen(req)

        bytes = page.read()
        html = bytes.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        return soup

    def search_urls(self, num_results):
        '''
        Searches google using the search query
        Returns a nested list with the URL and the title
        '''

        cutoff = 0

        page = self.read().body

        all_links = page.find_all('a')
        for link in all_links:
            if cutoff < num_results:
                if link.has_attr('href') and not link.has_attr('class'): # take out the second part if we want the news "fluff"
                    if 'url?q=' in link.get('href'):
                        self._results.append(link.get('href'))
                        try:
                            title = link.find('h3')
                            self._titles.append(title.getText())
                        except:
                            pass
                        cutoff = cutoff + 1

    def clear(self):
        '''
        Clears the list
        '''

        self._results = []

if __name__ == "__main__":
    test_query = "obama"
    test = Scraper(test_query)
    test.search_urls(4)
    print(test._titles)
