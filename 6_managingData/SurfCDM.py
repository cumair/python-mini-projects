'''

What are the 25 most common words on the CDM website? Write python code to answer this question.

'''


from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
response = urlopen("https://www.cdm.depaul.edu")
html = response.read().decode()


#**************************************************************************************
class MyHTMLParser(HTMLParser):
    'HTML doc parser that counts words into a dictionary'
    
    def __init__(self):
        'initializes the parser and dict'

        HTMLParser.__init__(self)
        self.dicT = {}
        self.hide = False            


    def handle_starttag(self, tag, attrs):                      
        'Start tag handler'

        if tag in ('style', 'script'):
            self.hide = True


    def handle_endtag(self, tag):
        'End tag handler'

        if tag in ('style', 'script'):
            self.hide = False


    def handle_data(self, data):
        'Arbitrary text data handler'
        
        if self.hide == False:

            lst = data.split()
            for word in lst:

                if word in self.dicT and word.isalpha() == True:        #isalpha returns “True” if all characters in the string are alphabets
                    self.dicT[word] += 1

                elif word not in self.dicT and word.isalpha() == True:
                    self.dicT[word] = 1


#**************************************************************************************
class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'

        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format'

        if tag == 'a':
            
            for attr in attrs:
                
                if attr[0] == 'href':
                    #construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    
                    if absolute[:4] == 'http':                      #collect HTTP URLs
                        self.links.append(absolute)
                        
    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'

        return self.links
    

#**************************************************************************************
visited = set()                                                     #initialize visited to an empty set

def crawl2(url):
    '''a recursive web crawler that calls analyze()
       on every visited web page'''

    #add url to set of visited pages
    global visited                                                  #warns the programmer 
    visited.add(url)

    #analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)

    #recursively continue crawl from every link in links
    for link in links:

        #follow link only if not visited
        if link not in visited and link[0:26] == "https://www.cdm.depaul.edu":

            try:
                crawl2(link)
                
            except:
                pass

#**************************************************************************************
def mostCommon(links):
    'finds 25 most common words'

    obj = MyHTMLParser()

    for link in links:
        
        response = urlopen(link)
        html = response.read().decode()
        obj.feed(html)

    for w in range(25):
        
        num = max(obj.dicT, key = obj.dicT.get)

        print('{} appears {} times.'.format(num, obj.dicT[num]))
        del obj.dicT[num]


#**************************************************************************************
def analyze(url):
    
    print('\n\nVisiting', url)                                      #for testing

    #obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()                                     #get list of links

    lst = []

    for link in urls:
        
        if link[0:26] == "https://www.cdm.depaul.edu":
            lst.append(link)

    return lst


#**************************************************************************************

crawl2("https://www.cdm.depaul.edu")
mostCommon(visited)
