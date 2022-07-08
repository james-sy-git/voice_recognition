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
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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

    def get_page(self):
        '''
        Returns this Scraper's URL
        '''
        return self._page

    def set_page(self, value):
        '''
        Changes which Google result page to be scraped
        '''
        # asserts here
        self._page = value

    def set_query(self, new_query):
        '''
        Inserts a new search query
        '''
        # asserts here
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

        self._query = query.strip() # safe get method from class UserListener
        self._page = 1
        try:
            self._results = self.get_results() # a list full of tuples or None
        
        except: # need 'URL not found error or something similar'
            self._results = []
            print('Search query could not find any results :/')


    def read(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

        url = "http://www.google.com/search?q=" + self._query + "&start=" + str((self._page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        return soup

    def get_results(self):
        results = []

        parsable = self.read()

        search = parsable.find_all('div', class_='yuRUbf')
        for h in search:
            if self._page == 1:
                if h.find_parents('div', {'jsname' : 'rozPHf'}) == []: # only applies the "people also ask" filter to 1st page of results
                    url = h.a.get('href')
                    title = h.find('h3').string
                    results.append((url, title))
            else:
                url = h.a.get('href')
                title = h.find('h3').string
                results.append({url : title})

        return results

    def clear(self):
        '''
        Clears the list
        '''

        self._results = []

# if __name__ == "__main__":
#     test_query = "barack obama"
#     test = Scraper(test_query)
#     print(test.results())
