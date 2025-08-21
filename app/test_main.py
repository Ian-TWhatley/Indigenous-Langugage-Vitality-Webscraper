from modules.module import EthnoDataFrame
import pandas as pd
import pytest

@pytest.fixture
def rawdataframe():
    pd.DataFrame([{
                        'Language':'Guaraní',
                        'Number':'6,500,000',
                        'Official Recognition':'Argentina (North), Bolivia, Brazil, Paraguay',
                        'Area(s) Language is spoken': 'Argentina (North), Bolivia (West), Brazil(South), Paraguay'
                    },
                    {
                        'Language':'Southern Quechua',
                        'Number':'5,000,000',
                        'Official Recognition':'Argentina, Bolivia, Chile, Peru',
                        'Area(s) Language is spoken': 'Argentina (North), Bolivia, Chile (North), Peru'
                    },
                    {
                        'Language':'Nahuatl',
                        'Number':'1,700,000',
                        'Official Recognition':'Mexico',
                        'Area(s) Language is spoken': 'Mexico (Central)'
                    }
                    ])

def dataframe(df):

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

def test_numbers_are_int(dataframe):
    assert dataframe.Numbers[0] == 6500000

df = EthnoDataFrame([{
                    'Language':'Guaraní',
                    'Number':'6,500,000',
                    'Official Recognition':'Argentina (North), Bolivia, Brazil, Paraguay',
                    'Area(s) Language is spoken': 'Argentina (North), Bolivia (West), Brazil(South), Paraguay'
                },
                {
                    'Language':'Southern Quechua',
                    'Number':'5,000,000',
                    'Official Recognition':'Argentina, Bolivia, Chile, Peru',
                    'Area(s) Language is spoken': 'Argentina (North), Bolivia, Chile (North), Peru'
                },
                {
                    'Language':'Nahuatl',
                    'Number':'1,700,000',
                    'Official Recognition':'Mexico',
                    'Area(s) Language is spoken': 'Mexico (Central)'
                }
                ])

df = dataframe(df)
print('bruh')