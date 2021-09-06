from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)
time.sleep(1)

letter = driver.find_element_by_id("chr")
operator = driver.find_element_by_id("op")
number = driver.find_element_by_id("num")
submit_btn = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")


list_of_ascii = f'{!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~}

def test_tc1():
    """
    Helyesen betöltődik az applikáció:
        Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
        !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~
    """
    ascii_list = driver.find_element_by_xpath('/html/body/div/div/p[3]')
    print(ascii_list.text)
    assert f'{ascii_list.text} == list_of_ascii'



def test_tc2:
    """
    Megjelenik egy érvényes művelet:
        chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
        op mező vagy + vagy - karaktert tartlamaz
        num mező egy egész számot tartalamaz
    """
    assert letter.is_enabled()
    assert operator.is_enabled()
    assert number.is_enabled()

def test_tc3():
    """
    Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
        A megjelenő chr mezőben lévő karaktert kikeresve a táblában
        Ha a + művelet jelenik meg akkor balra lépve ha a - akkor jobbra lépve
        A num mezőben megjelenő mennyiségű karaktert
        az result mező helyes karaktert fog mutatni
    """
    submit_btn.click()
    assert result.text == eval(f'{letter.text}{operator.text}{number.text}')

test_tc1()
test_tc2()
test_tc3()