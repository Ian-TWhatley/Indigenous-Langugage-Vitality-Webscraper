from bs4 import BeautifulSoup
import pandas as pd
import requests
import wikipedia
# req: lxml

class EthnoSeries(pd.Series):
    @property
    def _constructor(self):
        return EthnoSeries
    
    @property
    def _constructor_expanddim(self):
        return EthnoDataFrame

class EthnoDataFrame(pd.DataFrame):
    '''
    Modified DataFrame containing ethnographic information and langauges speakers

    Methods:
     - format_numbers 
     - format_countries
    '''
    @property
    def _constructor(self):
        return EthnoDataFrame
    
    @property
    def _constructor_sliced(self):
        return EthnoSeries
    
    # Methods
    def format_numbers(self):
        "Removes zeroes, formats numbers, and turns them into strungs"
        self.Number = self.Number.apply(lambda x: x.split(' ', 1)[0].replace(',',''))

        for num in self.Number:
            test = any(ele not in ['1','2','3','4','5','6','7','8','9','0'] for ele in list(num))
            if test == True:
                print(list(self.Number).index(num))
        # For now, manually rename
        self.loc[91,'Number'] = '10500'

        # Remove zeros
        self = self[self.Number != '0']
        self = self[self.Number != 0]

        # This is all non-functional for now
        # for i in range(len(self.Number)):
        #     self.loc[i,'Number'] = int(self.loc[i,'Number'])

    def format_countries(self, columns:str):
        for col in columns:
            self[col] = self[col].fillna('None')

            countries = ['Argentina','Bolivia','Brazil','Canada','Chile','Colombia','Costa Rica',
                        'Ecuador','El Salvador','French Guiana','Guatemala','Honduras',
                        'Mexico','Nicaragua','Panama','Paraguay','Peru','Suriname',
                        'United States','US','Uruguay','Venezuela', 'None']

            for i in range(len(self[col])):
                temp_ct = [country for country in countries if country in self[col][i]]
                if temp_ct == []:
                    temp_ct.append('None')
                self[col][i] = temp_ct
                        

            for i in range(len(self[col])):
                for j in range(len(self[col][i])):
                    if self[col][i][j] == 'US':
                        self[col][i][j] = 'United States'

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

def run():
    df, soup = get_table(url_link="https://en.wikipedia.org/wiki/Indigenous_languages_of_the_Americas")
    df = df.drop('Source',axis=1)

    # Rename Column for Ease
    data = df.rename(columns={'Number of speakers':'Number'})
    data = data.rename(columns={'Area(s) Language is spoken':'Areas'})
    data = EthnoDataFrame(data)

    # Format numbers
    data.format_numbers()
    for row in data.Number:
        row = int(row)
    
    # Format countries
    data.format_countries(['Areas', 'Official Recognition'])

    return data


if __name__ == "__main__":
    print(run())