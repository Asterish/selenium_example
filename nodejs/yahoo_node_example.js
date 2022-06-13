const {Builder, By, Key} = require('selenium-webdriver');

(async function openFirefoxTest() {
  try {
    let driver = await new Builder().forBrowser('firefox').build();
    await driver.get('https://www.yahoo.com');
    await driver.findElement(By.name('p')).sendKeys('seleniumhq' + Key.RETURN);
    await sleep(5000)
    await driver.quit();
  } catch (error) {
    console.log(error)
  }
})();

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
