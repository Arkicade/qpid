import requests
from bs4 import BeautifulSoup

urls = ["https://wealthygorilla.com/good-night-texts/", 
"https://rendezvousmag.com/good-night-texts-for-her/",
"https://www.adobe.com/express/discover/messages/text/good-night",
"https://therightmessages.com/goodnight-texts-for-girlfriend/",
"https://www.happierhuman.com/night-messages-her/",
"https://liveboldandbloom.com/10/relationships/goodnight-texts-her",
"https://www.poemsandoccasions.com/good-night-text-for-her/",
"https://nextluxury.com/mens-lifestyle-advice/goodnight-texts-for-her/",
"https://www.mantelligence.com/good-night-text-for-her/"
]
## create a file night_text_scrape to put goodnight messages into which can be filtered out separately
## to just give night_text.txt
file = open("night_text_scrape.txt", "a")
commentend = "<|endoftext|>"
keywords = ["night", "goodnight", "good night", "love", "sleep", "asleep", "dream", "sweet", "tonight"]
punctuation = [' ', '.', ',', '!', '?']


#### getting text from the each url
for url in urls:
    page = requests.get(url)
    content = page.text 

    soup = BeautifulSoup(content, 'html.parser')
    text = soup.find_all('p')
    for t in text:
        line = t.getText()
        ## assuming that they number the goodnight texts in the blog so a digit is at the front
        ## or if there is a keyword listed in case the blog does not number the samples
        if line[:1].isdigit() or any(word in line.lower() for word in keywords):
            #now to only accept characters that are either letters (isalpha)
            #or if the character is a key punctuation (space . , ! ?)
            line = ''.join([i for i in line if i.isalpha() or any(char in i for char in punctuation)])
            print(line)
            file.write(line+commentend+"\n")

file.close()
