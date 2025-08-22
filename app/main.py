import pandas as pd
from modules.module import EthnoDataFrame, get_table

def run():
    df, soup = get_table(url_link="https://en.wikipedia.org/wiki/Indigenous_languages_of_the_Americas")
    df = df.drop('Source',axis=1)

    # Rename Column for Ease
    data = df.rename(columns={'Number of speakers':'Number'})
    data = data.rename(columns={'Area(s) Language is spoken':'Areas'})
    data = EthnoDataFrame(data)

    # Format numbers
    data = data.format_numbers()
    
    # Format countries
    data = data.format_countries(['Areas', 'Official Recognition'])

    return data


if __name__ == "__main__":
    print(run())