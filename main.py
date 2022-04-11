from bs4 import BeautifulSoup
import requests

URL= 'https://www.reply.com/it/industries/energy-and-utilities/'

page = requests.get(URL)
soup = BeautifulSoup(page.content,'lxml')
divs = soup.findAll('div', class_='aux-content-box')
for div in divs:
    summary= div.find('h3', class_='summary')
    tipology = div.find('h4', class_='tipology')
    title = div.find('h2', class_='bigTitle')
    paragraph = div.find('p', class_='genericParagraph')

    if summary is not None:
        print("SUMMARY: "+summary.a.text)
    if tipology is not None:
        print("TIPOLOGY: "+tipology.a.text)
    if title is not None:
        print("TITLE: "+title.a.text)
    if paragraph is not None:
        print("DESCRIPTION: "+paragraph.text + "\n\n")
