from bs4 import BeautifulSoup
import requests
import pandas

url = 'https://www.flipkart.com/search?q=mobile+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phone%7CMobiles&requestId=5dde892f-43ae-4735-a96b-1bd927bcfef6'

header = ({'useragent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' , 'Accept-Language':'en-US,en;q=0.5' })

webpage = requests.get(url,headers = header)

soup = BeautifulSoup(webpage.content,'html.parser')

# soup

# name=soup.find_all('div',class_="_4rR01T")

products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
apps = []                #List to store supported apps
os = []                  #List to store operating system
hd = []                  #List to store resolution
sound = []               #List to store sound output
processors=[]

for data in soup.find_all('div', class_="_2kHMtA"):
    names=data.find('div', attrs={'class':'_4rR01T'})
    price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=data.find('div', attrs={'class':'_3LWZlK'})
    specification = data.find('div', attrs={'class':'fMghEO'})
    for each in specification:
            col=each.find_all('li', attrs={'class':'rgWa7D'})
            app =col[0].text
            os_ = col[1].text
            hd_ = col[2].text
            sound_ = col[3].text
            processors_=col[4].text
    products.append(names.text) # Add product name to list
    prices.append(price.text) # Add price to list
    apps.append(app)# Add supported apps specifications to list
    os.append(os_) # Add operating system specifications to list
    hd.append(hd_) # Add resolution specifications to list
    sound.append(sound_) # Add sound specifications to list
    ratings.append(rating.text)   #Add rating specifications to list
    processors.append(processors_)

import pandas as pd
df=pd.DataFrame({'Product Name':products,'Memory':apps,'Battery':sound,'Display':os,"Camera":hd,'Price':prices,'Rating':ratings})
df.to_csv("Filpkart_data.csv")