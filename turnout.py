# importing requests
import requests
#import beautifulsoup
from bs4 import BeautifulSoup
#import pands
import pandas as pd
# get the content of website with requests
r = requests.get("https://en.wikipedia.org/wiki/2019_Indian_general_election")
# convert the request object into soup and parse it
soup = BeautifulSoup(r.content, 'html.parser')
# find all the tables in the dataframe
table = soup.find_all("table")
df = pd.read_html(str(table))
# now convert selected dataframe into excel
df[10].to_excel("turnout.xlsx")
