import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://ebible.org/asv/JHN'


chapters = list(range(0,22))

random_chapter = random.choice(chapters)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

url = webpage +random_chapter +'.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()
		
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

page_verses = soup.findAll('div', class_='main')
print(page_verses)

for verses in page_verses:
    verse_list =  verses.text.split('.')
    
mychoice = random.choice(verse_list[:-5])

verse = f'Chapter: {random_chapter} Verse:{mychoice}'
print(verse)

import keys 
from twilio.rest import Client

TwilioNumber = '+18559976167'

myCellPhone = '+18322852232'

client = Client(keys.AccountSID, keys.authtoken)

textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body= verse)

print(textmessage.status)