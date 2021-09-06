from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)
time.sleep(1)

test_data = [("", ""), ("2", "3", "10"), ("", "", "NaN")]

a_old = driver.find_element_by_id("a")
b_old = driver.find_element_by_id("b")
c_old = driver.find_element_by_id("result")
calc_btn = driver.find_element_by_id("submit")


def filling_out_fields(a, b):
    a_old.clear()
    b_old.clear()
    a_old.send_keys(a)
    b_old.send_keys(b)
    calc_btn.click()
    time.sleep(1)


def test_initial():
    """
    Helyesen jelenik meg az applikáció betöltéskor:
        a: <üres>
        b: <üres>
        c: <nem látszik>
    """
    assert a_old.text == test_data[0][0]
    assert b_old.text == test_data[0][1]
    assert not c_old.is_displayed()


def test_correct_calculation():
    """
    Számítás helyes, megfelelő bemenettel
        a: 2
        b: 3
        c: 10
    """
    filling_out_fields(test_data[1][0], test_data[1][1])
    assert c_old.text == test_data[1][2]


def test_empty_fields():
    """
    Üres kitöltés:
        a: <üres>
        b: <üres>
        c: NaN
    """
    filling_out_fields(test_data[2][0], test_data[2][1])
    assert c_old.text == test_data[2][2]


# test_initial()
# test_correct_calculation()
# test_empty_fields()
