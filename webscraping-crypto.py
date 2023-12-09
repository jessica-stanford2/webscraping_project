from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers= headers)
webpage = urlopen(req).read()
		
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

crypto_data = soup.findAll('div',attrs={'class':'table-cell'})
names = soup.findAll('p', attrs={'class':'tit bold'})
symbols = soup.findAll('p', attrs={'class':'txt'})
name_value = 0
symbol_value = 1
rank = 1
currency_value = 2

for x in range(0,5):
    name = names[name_value].text
    symbol = symbols[symbol_value].text.replace('USD','')
    current_price = crypto_data[currency_value].text
    change = crypto_data[currency_value + 1].text
    change_formula = float(change.strip('+%'))
    current_price = float(current_price.replace(',',''))
    last_price = current_price*(1-(change_formula)*.01)

    print(f'Rank: {rank}')
    print(f'Currency name: {name}')
    print(f'Symbol: {symbol}')
    print(f'Current Price: ${float(current_price):,.2f}')
    print(f'% change in price last 24hrs: {change}')
    print(f'Last price: ${last_price:,.2f}')
    print()
    currency_value +=10
    rank += 1
    name_value += 1
    symbol_value += 2


    
    
    
    if name == 'Ethereum' and current_price > 2000:
        print(f'This is when Twilio would send a text message telling you that Ethereum is over $2000\n')

        '''
        import keys 
        from twilio.rest import Client

        TwilioNumber = '+18559976167'

        myCellPhone = '+18322852232'

        client = Client(keys.AccountSID, keys.authtoken)

        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, 
                        body= "The price for Ethereum is over $2,000! You should sell your shares!")
        '''
    input()