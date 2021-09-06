from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)
time.sleep(1)


def test_cell_numbers():
    """ A bingo tábla 25 darab cellát tartalmaz """
    cells_first_row = driver.find_elements_by_xpath('//*[@id="bingo-body"]/tr[1]/td')
    cells_second_row = driver.find_elements_by_xpath('//*[@id="bingo-body"]/tr[2]/td')
    cells_third_row = driver.find_elements_by_xpath('//*[@id="bingo-body"]/tr[3]/td')
    cells_fourth_row = driver.find_elements_by_xpath('//*[@id="bingo-body"]/tr[4]/td')
    cells_fifth_row = driver.find_elements_by_xpath('//*[@id="bingo-body"]/tr[5]/td')

    assert 25 == len(cells_first_row) + len(cells_second_row) + len(cells_third_row) + len(cells_fourth_row) + len(cells_fifth_row)


def test_number_list():
    """ A számlista 75 számot tartalmaz """
    numbers = driver.find_elements_by_xpath('//*[@id="numbers-list"]/li')
    number_list = 0
    for num in numbers:
        number_list +=1
    print(number_list)
    assert number_list == 75

# test_cell_numbers()
# test_number_list()
