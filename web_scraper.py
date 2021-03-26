from bs4 import BeautifulSoup
import requests

# BaseURL of Wikipedia.
URL = "https://en.wikipedia.org/wiki/"
# List of web searches.
Searches = ["Machine_learning", "Deep_learning", "Big_data", "Data_analysis",
            "Data_mining", "Neural_network", "Natural_language_processing", "Time_series"]

def database(URL, Searches):
    data_list = []
    for search in Searches:
        html_text = requests.get(f'''{URL}{search}''').text
        soup = BeautifulSoup(html_text, 'lxml')
        datas = soup.find_all('p')
        for data in datas:
            data_list.append(data.text)
    return data_list

Data = database(URL, Searches)
for data in Data:
    try:
        Data_File = open("Database.txt", "a")
        Data_File.writelines(Data)
    except:
        pass