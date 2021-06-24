import requests
from bs4 import BeautifulSoup

baseUrl = "https://job.jobnet.dk/CV/FindWork?Offset=0&SortValue=BestMatch&SearchString="
jobQuery = input("What job would you like to search for? ")
searchUrl = "https://www.jobindex.dk/jobsoegning?q=" + jobQuery

page = requests.get(searchUrl)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='result_list_box')

job_elems = results.find_all('div', class_='jobsearch-result')

for job_elem in job_elems:
    job_content = job_elem.find('div', class_='PaidJob-inner')

    job_title = job_content.find_all('a')[1].find('b')
    job_title = str(job_title)[3:-4]

    job_company_info = str(job_content.find('p'))
    job_company_info_part1 = job_company_info[ job_company_info.find('<b>') + 3 : job_company_info.find('</b>') ]
    job_company_info_part2 = job_company_info[ job_company_info.find('</b>') + 8 : -4 ]

    job_company_info = job_company_info_part1 + job_company_info_part2

    job_rating = str(job_elem.find(class_="sr-only"))
    
    if job_rating == 'None':
        job_rating = "Not Specified"
    else:
        job_rating = job_rating[ job_rating.find("sr-only") + 9 : -7 ]

    
    print("----------NY ANSØGNING----------" + '\n')
    print("Job titel: " + job_title)
    print("Firma information: " + job_company_info)
    print("Rating: " + job_rating + '\n')
    print("--------------------------------")
    print('\n')



