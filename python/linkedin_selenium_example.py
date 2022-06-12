from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pandas as pd
import time
import json

FILE_PATH_FOLDER = './results' # path to file

search_query = 'https://www.linkedin.com/jobs/search?keywords=chief financial officer'
browser = webdriver.Firefox()
job_details=[]

browser.get(search_query)
time.sleep(2)
job_list=browser.find_elements_by_xpath("//div[@class='base-search-card__info']")

for each_job in job_list:
    # Getting job info
    job_title = each_job.find_elements_by_xpath(".//h3[@class='base-search-card__title']")[0]
    job_company = each_job.find_elements_by_xpath(".//h4[@class='base-search-card__subtitle']")[0]
    job_location = each_job.find_elements_by_xpath(".//span[@class='job-search-card__location']")[0]
    job_publish_date = each_job.find_elements_by_xpath(".//time[@class='job-search-card__listdate']")[0]
    # Saving job info
    job_info = [job_title.text, job_company.text, job_location.text, job_publish_date.text, datetime.now()]
    # Saving into job_details
    job_details.append(job_info)

browser.quit()

job_details_df = pd.DataFrame(job_details)
job_details_df.columns = ['title', 'company', 'location', 'publish_date', 'timestamp']
job_details_df.to_csv('results.csv', index=False)
print(job_details_df)
