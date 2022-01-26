from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path=r'./chromedriver')
driver.get("https://www.discourse.org/")
elem = driver.find_element_by_link_text('Demo')
elem.click()
driver.switch_to.window(driver.window_handles[1])

lenOfPage = driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False

while(match == False):
    lastCount = lenOfPage
    sleep(3)
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True

lock = driver.find_elements_by_class_name('locked')
great_title = ""
max_view = 0
for i in lock:
    tr = i.find_element_by_xpath('./../../../../..')
    title = tr.find_element_by_class_name('raw-link').text
    views = int(tr.find_element_by_class_name('views').text)
    if views > max_view:
        great_title = title
        max_view = views
    try:
        category = tr.find_element_by_class_name('category-name').text
    except Exception as e:
        category = 'category not found'
    print(f"Title: '{title}'\nCategory: {category}\nViews: {views}\n")
print(
    f"The title: '{great_title}' has the greater number of views: {max_view}")

# sleep(10)
driver.close()
