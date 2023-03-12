#importing the libraries needed 
from bs4 import BeautifulSoup
import requests 
import csv

#connecting to the government's website
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

#extracting the titles and descriptions of the articles form GOVUK's website
titles = soup.find_all("a", class_="gem-c-document-list__item-title")
descriptions = soup.find_all("p", attrs={"class": "gem-c-document-list__item-description"})

#Create list for the headers
headers = ["title", "description"]
 
#Open a new file to write to called ‘data.csv’
with open('data.csv', 'w', newline='') as csvfile:
    #Create a writer object with that file
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    #Loop through each element in titles and descriptions lists
    for i in range(len(titles)):
        #Create a new row with the title and description at that point in the loop
        row = [titles[i], descriptions[i]]
        writer.writerow(row)