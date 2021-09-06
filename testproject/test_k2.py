from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)
time.sleep(1)

rnd_color_name = driver.find_element_by_id("randomColorName")
rnd_color_rgb = driver.find_element_by_id("randomColor")
test_color_name = driver.find_element_by_id("testColorName")
test_color_rgb = driver.find_element_by_id("testColor")
start_btn = driver.find_element_by_id("start")
stop_btn = driver.find_element_by_id("stop")
result = driver.find_element_by_id("result")


def test_initial():
    """
    Helyesen jelenik meg az applikáció betöltéskor:
        Alapból egy random kiválasztott szín jelenik meg az == bal oldalanán.
        A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ]
    """
    assert rnd_color_name.is_displayed()
    assert rnd_color_rgb.is_displayed()
    assert not test_color_name.is_displayed()


def test_testing_buttons():
    """
    El lehet indítani a játékot a start gommbal.
        Ha elindult a játék akkor a stop gombbal le lehet állítani.
    """
    assert start_btn.is_enabled()
    assert stop_btn.is_enabled()


def playing_with_colors():
    start_btn.click()
    time.sleep(5)
    stop_btn.click()


def test_control_result():
    """
    Eltaláltam, vagy nem találtam el.
        Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le,
        amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a Correct! felirat jelenik meg.
        Ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen.
    """
    playing_with_colors()
    if rnd_color_name == test_color_name:
        assert result.text == "Correct!"
    else:
        assert result.text == "Incorrect!"

# test_initial()
# test_testing_buttons()
# control_result()
