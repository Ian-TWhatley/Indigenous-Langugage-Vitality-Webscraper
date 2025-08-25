import pandas as pd
from modules.module import EthnoDataFrame, get_table
from IPython.display import HTML
import streamlit as st

def run():
    df, soup = get_table(url_link="https://en.wikipedia.org/wiki/Indigenous_languages_of_the_Americas")
    df = df.drop('Source',axis=1)

    # Rename Column for Ease
    data = df.rename(columns={'Number of speakers':'Number', 'Area(s) Language is spoken':'Areas'})

    # Turn into Ethnographic Data
    data = EthnoDataFrame(data)

    # Format numbers
    data = data.format_numbers()
    
    # Format countries
    data = data.format_countries(['Areas', 'Official Recognition'])

    return data, df

if __name__ == "__main__":
    data, df = run()
    data = pd.DataFrame(data)
    st.title("Native Languages of America")
    st.dataframe(data)