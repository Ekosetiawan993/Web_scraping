import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
URL1 = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
page = requests.get(URL)
page1 = requests.get(URL1)

soup = BeautifulSoup(page.content, "html.parser")
soup1 = BeautifulSoup(page1.content, "html.parser")

result = soup.find(id="ResultsContainer")
job_elements = result.find_all("div", class_="card-content")

python_jobs = result.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
#print(result.prettify())
#print(page.text)

for job in python_jobs:
    print(job.text)
    '''title_element = job.find("h2", class_="title")
    company_element = job.find("h3", class_="company")
    location_element = job.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()'''