from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome(executable_path=r'./chromedriver')
driver.get("https://www.cesar.school")
action = ActionChains(driver)

menuSchool = driver.find_element_by_id('menu-item-15376')
action.move_to_element(menuSchool).perform()

blogOption = driver.find_element_by_xpath("//a[contains(text(),'Blog')]")
blogOption.click()

secondArticle = driver.find_element_by_xpath("//article[2]")
titleSecondArticle = secondArticle.find_element_by_tag_name('h2')
dateSecongArticle = secondArticle.find_element_by_tag_name('time')
dateSecongArticle = dateSecongArticle.text.replace("\n", " ")

thirdArticle = driver.find_element_by_xpath("//article[3]")
titleThirdArticle = thirdArticle.find_element_by_tag_name('h2')
authorThirdArticle = thirdArticle.find_element_by_class_name('author-name')

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

addressCesar = driver.find_element_by_xpath("//div[@class='onde']/p[1]")

print(f'Título do segundo post: {titleSecondArticle.text}')
print(f'Data do segundo post: {dateSecongArticle}')
print(f'Título do terceiro post: {titleThirdArticle.text}')
print(f'Autor do terceiro post: {authorThirdArticle.text}')
print(f'Endereço da School: {addressCesar.text}')

driver.close()
