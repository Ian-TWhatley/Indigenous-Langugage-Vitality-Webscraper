from modules.module import EthnoDataFrame
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest

@pytest.fixture
def rawdataframe():
    return pd.DataFrame([{
                        'Language':'Guaraní',
                        'Number of speakers':'6,500,000',
                        'Official Recognition':'Argentina (North), Bolivia, Brazil, Paraguay',
                        'Area(s) Language is spoken': 'Argentina (North), Bolivia (West), Brazil(South), Paraguay'
                    },
                    {
                        'Language':'Southern Quechua',
                        'Number of speakers':'5,000,000',
                        'Official Recognition':'Argentina, Bolivia, Chile, Peru',
                        'Area(s) Language is spoken': 'Argentina (North), Bolivia, Chile (North), Peru'
                    },
                    {
                        'Language':'Nahuatl',
                        'Number of speakers':'1,700,000',
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
    
    # Format countries
    data.format_countries(['Areas', 'Official Recognition'])

    return data

def test_fixture_works(rawdataframe):
    assert_frame_equal(rawdataframe, pd.DataFrame(
                    [{
                        'Language':'Guaraní',
                        'Number of speakers':'6,500,000',
                        'Official Recognition':'Argentina (North), Bolivia, Brazil, Paraguay',
                        'Area(s) Language is spoken': 'Argentina (North), Bolivia (West), Brazil(South), Paraguay'
                    },
                    {
                        'Language':'Southern Quechua',
                        'Number of speakers':'5,000,000',
                        'Official Recognition':'Argentina, Bolivia, Chile, Peru',
                        'Area(s) Language is spoken': 'Argentina (North), Bolivia, Chile (North), Peru'
                    },
                    {
                        'Language':'Nahuatl',
                        'Number of speakers':'1,700,000',
                        'Official Recognition':'Mexico',
                        'Area(s) Language is spoken': 'Mexico (Central)'
                    }
                    ])
    )

def test_numbers_are_int(rawdataframe):
    data = dataframe(rawdataframe)
    assert data.Number[0] == 6500000

df = EthnoDataFrame([{
                    'Language':'Guaraní',
                    'Number of speakers':'6,500,000',
                    'Official Recognition':'Argentina (North), Bolivia, Brazil, Paraguay',
                    'Area(s) Language is spoken': 'Argentina (North), Bolivia (West), Brazil(South), Paraguay'
                },
                {
                    'Language':'Southern Quechua',
                    'Number of speakers':'5,000,000',
                    'Official Recognition':'Argentina, Bolivia, Chile, Peru',
                    'Area(s) Language is spoken': 'Argentina (North), Bolivia, Chile (North), Peru'
                },
                {
                    'Language':'Nahuatl',
                    'Number of speakers':'1,700,000',
                    'Official Recognition':'Mexico',
                    'Area(s) Language is spoken': 'Mexico (Central)'
                }
                ])
dataframe(df)
print('bruh')