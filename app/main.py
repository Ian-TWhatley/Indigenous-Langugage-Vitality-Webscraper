import pandas as pd
from modules.module import EthnoDataFrame, get_table
from IPython.display import HTML

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

    return data

def View(df):
    css = """<style>
    table { border-collapse: collapse; border: 3px solid #eee; }
    table tr th:first-child { background-color: #eeeeee; color: #333; font-weight: bold }
    table thead th { background-color: #eee; color: #000; }
    tr, th, td { border: 1px solid #ccc; border-width: 1px 0 0 1px; border-collapse: collapse;
    padding: 3px; font-family: monospace; font-size: 10px }</style>
    """
    s  = '<script type="text/Javascript">'
    s += 'var win = window.open("", "Title", "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=780, height=200, top="+(screen.height-400)+", left="+(screen.width-840));'
    s += 'win.document.body.innerHTML = \'' + (df.to_html() + css).replace("\n",'\\') + '\';'
    s += '</script>'
    return(HTML(s+css))

    View(df)

if __name__ == "__main__":
    data = run()
    View(data)