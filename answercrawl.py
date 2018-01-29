import os
from bs4 import BeautifulSoup
from html5lib import html5parser
from selenium import webdriver
import time


'''
This function uses chrome driver to grab information from a page
rendered in Javascript. See chromedriver docs for how to install
and use. 
'''

def render_page(url):
    driver = webdriver.Chrome('C:/Code/chromedriver_win32/chromedriver')
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r

'''
This function takes the text of the elements you have search for and writes them to a text
file. In this example it was a series of questions.
'''
def write_to_file(site):
        with open('questions.txt', 'a+') as outfile:
            for k,v in enumerate(site):
                if k == 0: 
                    outfile.write('Question {} : '.format(number) + v.text + '\n')
                else:
                    outfile.write('\n'+v.text+'\n')
            outfile.write('-'*69)

base_url = 'YOUR_BASE_URL_HERE'

'''
Iterates through all additional pages of the base url. This will only work if the base url
is something like www.example.com/page-x. Otherwise you might need to change the way it loads.
Note this version of the web crawl uses chromdriver because the target page was rendered in 
JavaScript. If the target page is just plain html or rendered completely server side you can 
forget about using chromedriver and it will work just fine. 
'''
for number in range(193):
    number = number+1
    url = base_url+'{}'.format(number)
    r = render_page(url)
    soup = BeautifulSoup(r, 'html5lib')
    content = soup.find('div', {'class': 'entry-content'})
    text = content.find_all('p')
    write_to_file(text)

    
