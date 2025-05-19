from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def start_browser(url):
    driver = webdriver.Chrome(service=Service(),options=Options())
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    return driver

def test_homepage():
    driver = start_browser("https://ruskicar.rs/")
    assert "Pocetna - Restoran Monument Ruski Car" in driver.title, "Stranica nije ucitana"
    print("Stranica je ucitana")
    close_browser(driver)

def test_navigation_menu():
    driver = start_browser("https://ruskicar.rs/")
    menu_items = {
        'O nama': 'O nama - Restoran Monument Ruski Car',
        'Jelovnik': 'Doručak - Restoran Monument Ruski Car',
        'Karta pića': 'Sveže ceđeni sokovi - Restoran Monument Ruski Car',
        'Galerija': 'Galerija - Restoran Monument Ruski Car',
        'Blog': 'Blog - Restoran Monument Ruski Car'
    }
    sve_stranice_ucitane = True
    try:
        for item, expected_title in menu_items.items():
            print(f"Testiram {item}")
            sleep(1)
            link_element = driver.find_element(By.XPATH, f"//a[contains(text(), '{item}')]")
            actions = ActionChains(driver)
            actions.key_down(Keys.CONTROL).click(link_element).key_up(Keys.CONTROL).perform()
            sleep(1)
            driver.switch_to.window(driver.window_handles[1])
            sleep(2)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije učitana. Očekivano: '{expected_title}', Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep(1)
        print("Testiram Kontakt")
        driver.find_element(By.XPATH, "//span[contains(text(), 'KONTAKT')]").click()
        sleep(1)
        if "Kontakt - Restoran Monument Ruski Car" not in driver.title:
                print(f"Stranica 'Kontakt' nije učitana. Očekivano: 'Kontakt - Restoran Monument Ruski Car', Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: {e}")
    finally:
        assert sve_stranice_ucitane, "Test nije uspešan! Neke stranice nisu uspešno učitane."
        close_browser(driver)

def test_menu_categories():
    driver = start_browser("https://ruskicar.rs/kategorija-jela/dorucak-sr/")
    kategorije = {
        'Doručak': 'Doručak - Restoran Monument Ruski Car',
        'Predjela': 'Predjela - Restoran Monument Ruski Car',
        'Supe i potaži': 'Supe i potaži - Restoran Monument Ruski Car',
        'Sendviči': 'Sendviči - Restoran Monument Ruski Car',
        'Rižoto': 'Rižoto - Restoran Monument Ruski Car',
        'Pizza' : 'Pizza - Restoran Monument Ruski Car',
        'Domaća pasta': 'Domaća pasta - Restoran Monument Ruski Car',
        'Jela kuće': 'Jela kuće - Restoran Monument Ruski Car',
        'Jela sa roštilja': 'Jela sa roštilja - Restoran Monument Ruski Car',
        'Burgeri': 'Burgeri - Restoran Monument Ruski Car',
        'Riba': 'Riba - Restoran Monument Ruski Car',
        'Obrok salate' : 'Obrok salate - Restoran Monument Ruski Car',
        'Salate' : 'Salate - Restoran Monument Ruski Car',
        'Hleb' : 'Hleb - Restoran Monument Ruski Car',
        'Dodaci' : 'Dodaci - Restoran Monument Ruski Car',
        'Prilozi' : 'Prilozi - Restoran Monument Ruski Car',
        'Palačinke' : 'Palačinke - Restoran Monument Ruski Car',
        'Vafle' : 'Vafle - Restoran Monument Ruski Car',
        'Torte' : 'Torte - Restoran Monument Ruski Car',
        'Kremasti' : 'Kremasti - Restoran Monument Ruski Car',
        'Raw' : 'Raw - Restoran Monument Ruski Car',
        'Pite' : 'Pite - Restoran Monument Ruski Car',
        'Sladoled i kupovi' : 'Sladoled i kupovi - Restoran Monument Ruski Car',
        'Voće' : 'Voće - Restoran Monument Ruski Car',
        'We are famous 4' : 'We are famous 4 - Restoran Monument Ruski Car'
    }
    sve_stranice_ucitane = True
    try:
        for item, expected_title in kategorije.items():
            print(f"Testiram {item}")
            sleep(1)
            element = driver.find_element(By.XPATH, f"//a[.= '{item}']")
            driver.execute_script("arguments[0].click();", element)
            sleep(1)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije učitana. Očekivano: '{expected_title}', Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            sleep(0.5)
            driver.get("https://ruskicar.rs/kategorija-jela/dorucak-sr/")
            sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: {e}")
    finally:
        assert sve_stranice_ucitane, "Test FAILED! Neke stranice nisu uspešno učitane."
        close_browser(driver)
          
def test_product_image():
    driver = start_browser("https://ruskicar.rs/kategorija-jela/sendvici-sr/")
    image_element = driver.find_element(By.XPATH, "//img[@src='https://ruskicar.rs/wp-content/uploads/2024/03/monument-sendvic.jpg']")
    image_element.click()
    sleep(1)
    assert image_element.is_displayed(), "Slika nije prikazana na stranici."
    driver.save_screenshot("slika_stranice.png")
    close_browser(driver)

def close_browser(driver):
    driver.minimize_window()
    driver.close()