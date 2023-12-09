import requests
from bs4 import BeautifulSoup
from plotly import offline



x=1
quotes=[]

while x <= 10:
    url = 'https://quotes.toscrape.com/page/'
    page_num = str(x)

    url = url + page_num + '/'


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.title.text)

    quotes += soup.findAll('div', class_='quote')
    x+=1


#author quote count
quote_count = {}

for quote in quotes:
    authors = quote.findAll('small', class_='author')
    for author in authors:
        author= author.string.lstrip('>')
        
        if author in quote_count:
            quote_count[author] += 1
        else:
            quote_count[author] = 1

print(f'Author Statistics')
print(f'The author with the most quotes is {max(quote_count, key=quote_count.get)} with {max(quote_count.values())} quotes\n')
print(f'The author with the least quotes is {min(quote_count, key=quote_count.get)} with {min(quote_count.values())} quote(s)\n')


#length of quotes
quote_lengths = {}
quote_chars = 0
num_of_quotes = 0
for quote in quotes:
    quote_list = quote.findAll('span', class_ = 'text')
    for quote in quote_list:

        quote = quote.string.lstrip('>')
        
        quote_length = len(quote)
        quote_lengths[quote_length] = quote
        quote_chars += quote_length
        num_of_quotes +=1
shortest_quote = quote_lengths[min(quote_lengths)]
longest_quote = quote_lengths[max(quote_lengths)]


average_length = quote_chars/num_of_quotes
print(f'Quote Analysis')
print(f'The average number of characters in a quote is {average_length}\n')
print(f'The shortest quote is {shortest_quote} with {min(quote_lengths)} characters.\n')
print(f'The longest quote is {longest_quote} with {max(quote_lengths)} characters.\n')



#Tag Analysis

tag_count = {}
for quote in quotes:
    tags = quote.findAll('a', class_='tag')
    for tag in tags:
        tag = tag.string.lstrip('>')
        if tag in tag_count:
            tag_count[tag] += 1
        else:
            tag_count[tag] = 1


print('Tag Analysis')
print(f'The most popular tag is {max(tag_count, key=tag_count.get)} with {max(tag_count.values())} uses.\n')
print(f'The total amount of tags on the site is {len(tag_count)}\n')

#plotly

top_authors = sorted(quote_count.items(), key= lambda x:x[1], reverse=True)[:10]
author_names, author_quotes = zip(*top_authors)

author_data = [{
                'type':'bar', 
                'x':author_names,
                'y':author_quotes}]

author_format = {'title':'Top 10 Authors based on No. of Quotes', 'xaxis':{'title':'Author'}, 
                 'yaxis':{'title':'No. of Quotes'}}

chart1 = {'data': author_data, 'layout':author_format}
offline.plot(chart1, filename='author_quotes.html')

top_tags = sorted(tag_count.items(), key=lambda x:x[1], reverse=True)[:10]
tag_name, tag_count = zip(*top_tags)

tag_data = [
    {'type':'bar', 
     'x':tag_name,
     'y':tag_count}
]

tag_format = {
    'title':'Top 10 Tags',
    'xaxis':{'title':'Tag'},
    'yaxis':{'title': 'No. of Tags'}}

chart2 = {'data': tag_data, 'layout':tag_format}
offline.plot(chart2, filename = 'top_tags.html')


        

    

