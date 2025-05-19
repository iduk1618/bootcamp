from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def start_browser(url):
    driver = webdriver.Chrome(options=Options(),service=Service())
    driver.get(url)
    driver.maximize_window()
    sleep (1)
    return driver


def test_navbar():
    driver = start_browser("https://forteco.rs/")
    navbar_items = {
        'Početna':'Forteco plus d.o.o. – Construction company',
        'O nama':'O nama - Forteco plus d.o.o.',
        'Usluge':'Usluge - Forteco plus d.o.o.',
        'Reference':'Reference - Forteco plus d.o.o.',
        'Kontakt':'Kontakt - Forteco plus d.o.o.'
    }
    sve_stranice_ucitane = False
    try:
        for item, expected_title in navbar_items.items():
            navbar_element = driver.find_element(By.XPATH, f"//span[contains(text(),'{item}')]")
            navbar_element.click()
            sleep(1)
            print(f"Testiram '{item}'")
            if "Forteco plus d.o.o. – Construction company" in driver.title:
                if expected_title in driver.title:
                    sve_stranice_ucitane = False
            else:
                driver.back()
                sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: {e}")
    finally:
        assert sve_stranice_ucitane, "Nisu ucitane sve stranice."
        close_browser(driver)

def test_usluge():
    driver = start_browser("https://forteco.rs/")
    menu = {
    'Projektovanje' : 'https://forteco.rs/usluge/projektovanje/',
    'Nadzor' : 'https://forteco.rs/usluge/strucni-i-projektantski-nadzor/',
    'Savetovanje' : 'https://forteco.rs/usluge/tehnicko-savetovanje/'
    }
    navbar_items = {
        list(menu.values())[0]: 'Projektovanje – Forteco plus d.o.o.',
        list(menu.values())[1]: 'Stručni i projektantski nadzor – Forteco plus d.o.o.',
        list(menu.values())[2]: 'Tehničko savetovanje – Forteco plus d.o.o.'
    }
    sve_stranice_ucitane = True
    for key,value in menu.items():
                print(f"Testiram '{key}': '{value}'")
    try:
        driver.execute_script("window.scrollBy(0,1500);")
        for item, expected_title in navbar_items.items():
            sleep(1)
            navbar_element = driver.find_element(By.XPATH, f"//a[@href='{item}' and contains(text(), 'Opširnije')]")
            navbar_element.click()
            sleep(1)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije ucitana. Ocekivano: '{expected_title}', Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            driver.back()
            sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: {e}")
    finally:
        assert sve_stranice_ucitane, "Nisu ucitane sve stranice."
        close_browser(driver)

def test_reference():
    driver = start_browser("https://forteco.rs/")
    navbar_items = {
        'Tübingen Carrè 5' : 'Tübingen Carrè 5 – Forteco plus d.o.o.',
        'Sportski centar Kleinfeld': 'Sportski centar Kleinfeld – Forteco plus d.o.o.',
        'Andreasturm': 'Andreasturm – Forteco plus d.o.o.'
    }
    sve_stranice_ucitane = True
    try:
        # driver.execute_script("window.scrollBy(0,3000);")
        for item, expected_title in navbar_items.items():
            sleep(1)
            navbar_element = driver.find_element(By.XPATH, f"//a[contains(text(),'{item}')]")
            navbar_element.click()
            print(f"Testiram '{item}'")
            sleep(1)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije ucitana. Ocekivano: '{expected_title}', Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            driver.back()
            sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: {e}")
    finally:
        assert sve_stranice_ucitane, "Nisu ucitane sve stranice."
        close_browser(driver)

def close_browser(driver):
    driver.minimize_window()
    driver.close()