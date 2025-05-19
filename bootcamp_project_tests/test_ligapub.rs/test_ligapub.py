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
    sleep(1)
    return driver

def test_location_homepage():
    driver = start_browser("https://ligapub.rs/")
    lokacije = {
    "https://ligapub.rs/liga-pub-obilicev-venac/": "Liga Pub Obilićev venac | Liga Pub Beograd",
    "https://ligapub.rs/liga-pub-visnjicka/": "Liga pub Višnjička | Liga Pub Beograd"
}
    sve_lokacije_ucitane = True
    try:
        for lokacija, expected_title in lokacije.items():
            driver.find_element(By.XPATH,f"//a[@href='{lokacija}']").click()
            sleep(1)
            if expected_title not in driver.title:
                sve_lokacije_ucitane = False
                sleep(0.5)
            driver.back()
            sleep(1)
    except Exception as e:
        print(f"Lokacija {lokacija} nije ucitana: {e}")
    finally:
        assert sve_lokacije_ucitane, "Nisu sve lokacije ucitane"
        close_browser(driver)

def test_navigation_menu_ov():
    driver = start_browser("https://ligapub.rs/liga-pub-obilicev-venac")
    menu_items = {
        'Naslovna': 'Naslovna | Liga Pub Beograd',
        'Najave': 'Najave | Liga Pub Beograd',
        'Karijera': 'Karijera | Liga Pub Beograd',
        'Jelovnik': 'Obilićev venac jelovnik | Liga Pub Beograd',
        'Karta PIća': 'Obilićev venac Karta pića | Liga Pub Beograd',
        'REZERVACIJE' : 'Obilićev venac kontakt | Liga Pub Beograd'
    }
    sve_stranice_ucitane = True
    try:
        for item, expected_title in menu_items.items():
            print(f"Testiram {item}")
            sleep(1)
            link_element = driver.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
            link_element.click()
            sleep(2)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije ucitana. Ocekivano: '{expected_title}'. Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            driver.back()
            sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: '{e}'")
    finally:
        assert sve_stranice_ucitane, "Test nije uspesan! Neke stranice nisu uspesno ucitane."
    close_browser(driver)

def test_navigation_menu_vi():
    driver = start_browser("https://ligapub.rs/liga-pub-visnjicka/")
    menu_items = {
        'Naslovna': 'Naslovna | Liga Pub Beograd',
        'Galerija' : 'Galerija | Liga Pub Beograd',
        'Najave': 'Najave | Liga Pub Beograd',
        'Karijera': 'Karijera | Liga Pub Beograd',
        'Jelovnik': 'Višnjička jelovnik | Liga Pub Beograd',
        'Karta PIća': 'Višnjička karta pića | Liga Pub Beograd',
        'REZERVACIJE' : 'Višnjička kontakt | Liga Pub Beograd'
    }
    sve_stranice_ucitane = True
    try:
        for item, expected_title in menu_items.items():
            print(f"Testiram {item}")
            sleep(1)
            link_element = driver.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
            link_element.click()
            sleep(2)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije ucitana. Ocekivano: '{expected_title}'. Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            driver.back()
            sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: '{e}'")
    finally:
        assert sve_stranice_ucitane, "Test nije uspesan! Neke stranice nisu uspesno ucitane."
    close_browser(driver)

def test_footer_socials_ob():
    driver = start_browser("https://ligapub.rs/liga-pub-obilicev-venac")
    driver.execute_script("window.scrollBy(0,4000);")
    socials_links ={
        'Facebook' : 'Liga Pub Beograd | Belgrade | Facebook',
        'Instagram' : 'LIGA PUB (@ligapub.bg) • Instagram photos and videos',
        'Tiktok' : 'Liga Pub Centar (@liga.pub.centar) | TikTok',
        'Linkedin' : 'Liga Pub | LinkedIn'   
    }
    sve_stranice_ucitane = True
    try:
        for item, expected_title in socials_links.items():
            print(f"Testiram {item}")
            sleep(1)
            driver.find_element(By.XPATH, f"//span[contains(text(),'{item}')]/parent::a").click()
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            sleep(1)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije ucitana. Ocekivano: '{expected_title}'. Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: '{e}'")
    finally:
        assert sve_stranice_ucitane, "Test nije uspesan! Neke stranice nisu uspesno ucitane."
        close_browser(driver)

def test_footer_socials_vi():
    driver = start_browser("https://ligapub.rs/liga-pub-visnjicka/")
    driver.execute_script("window.scrollBy(0,4000);")
    socials_links ={
        'Facebook' : 'Liga Pub | Belgrade | Facebook',
        'Instagram' : 'Liga Pub (@liga_pub_beograd) • Instagram photos and videos',
        'Linkedin' : 'Liga Pub | LinkedIn'   ,
        'Viber' : 'Liga Pub on Viber'
    }
    sve_stranice_ucitane = True
    try:
        for item, expected_title in socials_links.items():
            print(f"Testiram {item}")
            sleep(1)
            driver.find_element(By.XPATH, f"//span[contains(text(),'{item}')]/parent::a").click()
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            sleep(1)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije ucitana. Ocekivano: '{expected_title}'. Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: '{e}'")
    finally:
        assert sve_stranice_ucitane, "Test nije uspesan! Neke stranice nisu uspesno ucitane."
        close_browser(driver)

def close_browser(driver):
    driver.minimize_window()
    driver.close()