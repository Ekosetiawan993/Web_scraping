import requests
from bs4 import BeautifulSoup

URL = "https://remote.co/remote-jobs/search/?search_keywords=Data+Scientist"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#result = soup.find(id="job_listings")
job_list = soup.find_all("li", class_="job_listings")

#print(type(job_list))

for job in job_list:
    title_element = job.find("h2", class_="position")
    company_element = job.find("strong", class_="company")
    
    print(title_element.text.strip())
    print(company_element.text.strip())
    
    print()