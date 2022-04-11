from bs4 import BeautifulSoup
import requests

URL= 'https://www.tgcom24.mediaset.it/'

page = requests.get(URL)
soup = BeautifulSoup(page.content,'lxml')
elements = soup.findAll('ul', class_='dsrow')
for element in elements:
    titoloPiccolo= element.find('h4')
    titolo = element.find('h2')
    title = element.find('h2', class_='bigTitle')
    paragraph = element.find('p', class_='genericParagraph')

    if titoloPiccolo is not None:
        print("INTRO: "+titoloPiccolo.text.lstrip())
    if titolo is not None:
        print("TITOLO: "+titolo.text.lstrip())
