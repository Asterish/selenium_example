from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pandas as pd
import time
import json

#PROXY = "<HOST:PORT>"
#webdriver.DesiredCapabilities.FIREFOX['proxy'] = {"httpProxy": PROXY,"sslProxy": PROXY,"proxyType": "MANUAL",}

FILE_PATH_FOLDER = './results/' # path to file
FILENAME = 'results.csv'

query = 'https://www.linkedin.com/jobs/search?keywords=chief financial officer'
driver = webdriver.Firefox()
job_details=[]

driver.get(query)

total_jobs=driver.find_element_by_xpath('/html/body/div[1]/div/main/div/h1/span[1]').text
new_jobs=driver.find_element_by_xpath('/html/body/div[1]/div/main/div/h1/span[3]').text

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

job_list=driver.find_elements_by_xpath("//div[@class='base-search-card__info']")

for each_job in job_list:
    # Getting job info
    job_title = each_job.find_elements_by_xpath(".//h3[@class='base-search-card__title']")[0]
    job_company = each_job.find_elements_by_xpath(".//h4[@class='base-search-card__subtitle']")[0]
    job_location = each_job.find_elements_by_xpath(".//span[@class='job-search-card__location']")[0]
    job_publish_date = each_job.find_elements_by_xpath(".//div[@class='base-search-card__metadata']/time")[0]
    # Saving job info
    job_info = [job_title.text, job_company.text, job_location.text, job_publish_date.text, datetime.now()]
    # Saving into job_details
    job_details.append(job_info)

driver.quit()

job_details_df = pd.DataFrame(job_details)
job_details_df.columns = ['Title', 'Company', 'Location', 'Published Date', 'Timestamp']
job_details_df.to_csv(FILE_PATH_FOLDER + FILENAME, index=False)
print(f'Results Ready! Find them in:\n{FILE_PATH_FOLDER}{FILENAME}.\n\nJob Count:\n{total_jobs} Total {new_jobs}\n', job_details_df)
