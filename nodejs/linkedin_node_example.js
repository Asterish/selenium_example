const {Builder, By, Key} = require('selenium-webdriver');

var query = 'https://www.linkedin.com/jobs/search?keywords=chief financial officer';
var job_details = [];

(async function openFirefoxTest() {
  try {
    let driver = await new Builder().forBrowser('firefox').build();

    await driver.get(query);
    await sleep(5000);

    let job_list = await driver.findElements(By.className('base-search-card__info'));

    for(let i=0;i<job_list.length;i++){
      let job_title = await job_list[i].findElement(By.className('base-search-card__title')).getText();
      let job_company = await job_list[i].findElement(By.className('base-search-card__subtitle')).getText();
      let job_location = await job_list[i].findElement(By.className('job-search-card__location')).getText();
      let job_publish_date = await job_list[i].findElement(By.tagName('time')).getAttribute('datetime');
      // Saving job info
      let job_info = [job_title, job_company, job_location, job_publish_date]
      // Saving into job_details
      job_details.push(job_info);
    }
    await sleep(5000);
    await driver.quit();
    console.table(job_details);
  } catch (error) {
    console.log(error);
  }
})();

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
