from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


def scroll_page(driver):
    len_of_page = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while not match:
        last_count = len_of_page
        sleep(3)
        len_of_page = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if last_count == len_of_page:
            match = True


def challenge_1():
    print("Making the first test...")
    driver = webdriver.Chrome(executable_path=r'./chromedriver')
    driver.get("https://www.discourse.org/")
    elem = driver.find_element_by_link_text('Demo')
    elem.click()
    driver.switch_to.window(driver.window_handles[1])
    scroll_page(driver)
    items_with_lock_icon = driver.find_elements_by_class_name('locked')
    great_title = ""
    max_view = 0
    for item in items_with_lock_icon:
        table_tr = item.find_element_by_xpath('./../../../../..')
        title = table_tr.find_element_by_class_name('raw-link').text
        views = int(table_tr.find_element_by_class_name('views').text)
        if views > max_view:
            great_title = title
            max_view = views
        try:
            category = table_tr.find_element_by_class_name('category-name').text
        except NoSuchElementException:
            category = 'category not found'
        print(f"Title: '{title}'\nCategory: {category}\nViews: {views}\n")
    print(
        f"The title: '{great_title}' has the greater number of views: {max_view}")
    driver.close()


def challenge_2():
    print("Making the second test...")
    driver = webdriver.Chrome(executable_path=r'./chromedriver')
    driver.get("https://www.cesar.school")
    action = ActionChains(driver)

    menu_school = driver.find_element_by_id('menu-item-15376')
    action.move_to_element(menu_school).perform()

    blog_option = driver.find_element_by_xpath("//a[contains(text(),'Blog')]")
    blog_option.click()

    second_article = driver.find_element_by_xpath("//article[2]")
    title_second_article = second_article.find_element_by_tag_name('h2')
    date_secong_article = second_article.find_element_by_tag_name('time').text.replace("\n", " ")

    third_article = driver.find_element_by_xpath("//article[3]")
    title_third_article = third_article.find_element_by_tag_name('h2')
    author_third_article = third_article.find_element_by_class_name('author-name')
    scroll_page(driver)
    address_cesar = driver.find_element_by_xpath("//div[@class='onde']/p[1]")
    print(f'Título do segundo post: {title_second_article.text}')
    print(f'Data do segundo post: {date_secong_article}')
    print(f'Título do terceiro post: {title_third_article.text}')
    print(f'Autor do terceiro post: {author_third_article.text}')
    print(f'Endereço da School: {address_cesar.text}')
    driver.close()


if __name__ == "__main__":
    challenge_1()
    challenge_2()
