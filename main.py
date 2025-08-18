from bs4 import BeautifulSoup
import pandas as pd
import requests
import wikipedia
from tqdm import tqdm
import geopandas as gpd
import matplotlib.pyplot as plt
# req: lxml

def get_wiki(x,html=False):
    'get a wikipedia page from the title of an html snippet'
    if html:
        return wikipedia.WikipediaPage(x.get('title'))
    else:
        return wikipedia.page(x.get('title'))
    
def get_table(url_link):
    content = requests.get(url_link).text
    soup = BeautifulSoup(content,'html.parser')
    table = soup.find_all('table', 'wikitable')

    df= pd.read_html(str(table))
    df=pd.DataFrame(df[0])
    return df, soup

def format_numbers(data):
    '''
    Removes zeroes, formats numbers, and turns them into strungs
    '''
    for num in data.Number:
        test = any(ele not in ['1','2','3','4','5','6','7','8','9','0'] for ele in list(num))
        if test == True:
            print(list(data.Number).index(num))
    # For now, manually rename
    data.Number[91] = '10500'

    # Remove zeros
    data = data[data.Number != '0']
    data.Number = data.Number.astype(int)

    return data

def format_areas(data):

    countries = ['Argentina','Bolivia','Brazil','Canada','Chile','Colombia','Costa Rica',
                'Ecuador','El Salvador','French Guiana','Guatemala','Honduras',
                'Mexico','Nicaragua','Panama','Paraguay','Peru','Suriname',
                'United States','US','Uruguay','Venezuela']

    for i in range(len(data.Areas)):
        temp_ct = [country for country in countries if country in data.Areas[i]]
        data.Areas[i] = temp_ct

    for i in range(len(data.Areas)):
        for j in range(len(data.Areas[i])):
            if data.Areas[i][j] == 'US':
                data.Areas[i][j] = 'United States'

df, soup = get_table(url_link="https://en.wikipedia.org/wiki/Indigenous_languages_of_the_Americas")
df = df.drop('Source',axis=1)

# Rename Column for Ease
data = df.rename(columns={'Number of speakers':'Number'})
data = data.rename(columns={'Area(s) Language is spoken':'Areas'})

# Format numbers
data.Number = data.Number.apply(lambda x: x.split(' ', 1)[0].replace(',',''))

data = format_numbers(data)

#  Format areas

format_areas(data)

print(data)