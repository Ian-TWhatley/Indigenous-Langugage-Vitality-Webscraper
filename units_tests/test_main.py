from main import EthnoDataFrame, get_table, get_wiki
import pytest

@pytest.fixture
def rawdataframe():
    EthnoDataFrame([{
                        'Language':'Guaraní',
                        'Number':'6,500,000',
                        'Official Recognition':'Argentina (North), Bolivia, Brazil, Paraguay',
                        'Area(s) Spoken': 'Argentina (North), Bolivia (West), Brazil(South), Paraguay'
                    },
                    {
                        'Language':'Southern Quechua',
                        'Number':'5,000,000',
                        'Official Recognition':'Argentina, Bolivia, Chile, Peru',
                        'Area(s) Spoken': 'Argentina (North), Bolivia, Chile (North), Peru'
                    },
                    {
                        'Language':'Nahuatl',
                        'Number':'1,700,000',
                        'Official Recognition':'Mexico',
                        'Area(s) Spoken': 'Mexico (Central)'
                    }
                    ])

@pytest.fixture
def dataframe(rawdataframe):
    df = rawdataframe()

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
