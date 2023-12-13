import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
 
Job_titles =[]
Job_skills =[]
Company_name =[]
Loction_name =[]
links = []

#2nd step use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

#3nd step save page content 
scr = result.content
#print(scr)

#4nd step create soup obj to parse content
soup = BeautifulSoup(scr ,"html.parser")
#print(soup)

#5nd step find the elements containing info we need 
#Job titles , Job skills , company names , location names
Job_titless = soup.find_all("h2",{"class":"css-m604qf"} ) 
Company_namee = soup.find_all("a",{"class":"css-17s97q8"})
Loction_namee = soup.find_all("span",{"class":"css-5wys0k"})
Job_skillss = soup.find_all("div",{"class":"css-y4udm8"})

#6nd step loop over returned lists to extract needed info into other lists
for i in range(len(Job_titless)):
    Job_titles.append(Job_titless[i].text)
    links.append(Job_titless[i].find("a").attrs["href"])
    Job_skills.append(Job_skillss[i].text)
    Company_name.append(Company_namee[i].text)
    Loction_name.append(Loction_namee[i].text)
# print(Company_name ,Loction_name )
# print(Job_titles , Job_skills)  

#7nd step create csv file and file with values
file_list = [Job_titles , Company_name , Loction_name ,Job_skills , links ]
exported = zip_longest(*file_list)

with open("C:\\Users\\ososa\\OneDrive\\Documents\\jobs.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job_titel" , "Company_name" , "Location" , "Skills" , "links" ])
    wr.writerows(exported)
