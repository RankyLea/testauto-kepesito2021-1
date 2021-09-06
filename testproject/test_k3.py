from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)
time.sleep(1)

input_field = driver.find_element_by_id("title")
test_data = ["abcd1234", "teszt233@", "abcd"]
error_messages = ["", "Only a-z and 0-9 characters allewed",
                  "Title should be at least 8 characters; you entered 4."]


def clear_and_fill_input(data):
    input_field.clear()
    input_field.send_keys(data)


def test_correct():
    """
    Helyes kitöltés esete:
        title: abcd1234
        Nincs validációs hibazüzenet
    """
    clear_and_fill_input(test_data[0])
    error_none = driver.find_element_by_xpath('//*[@class="error"]')
    assert error_none.text == error_messages[0]


def test_illegal_characters():
    """
    Illegális karakterek esete:
        title: teszt233@
        Only a-z and 0-9 characters allewed.
    """
    clear_and_fill_input(test_data[1])
    error = driver.find_element_by_xpath('//*[@class="error active"]')
    assert error.text == error_messages[1]


def test_short_filling():
    """
    Tul rövid bemenet esete:
        title: abcd
        Title should be at least 8 characters; you entered 4.
    """
    clear_and_fill_input(test_data[2])
    error = driver.find_element_by_xpath('//*[@class="error active"]')
    assert error.text == error_messages[2]

# test_correct()
# test_illegal_characters()
# test_short_filling()
