from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def start_browser(url):
    driver = webdriver.Chrome(options=webdriver.ChromeOptions(), service=Service())
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    return driver

def test_pocetna_stranica_1():
    driver = start_browser("https://www.ctshop.rs/")
    assert "CT shop - Odlične cene, još bolja usluga!" in driver.title, "Stranica nije ucitana"
    close_browser(driver)

def test_pretraga_2():
    driver = start_browser("https://www.ctshop.rs/")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys("iphone")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys(Keys.RETURN)
    sleep(2)
    assert driver.find_elements(By.XPATH,'//span[contains(text(),"Ukupno")]') and driver.find_element(By.XPATH,'//label[text()="Sortiraj po"]'), "Pretraga nije uspela"
    close_browser(driver)

def test_prikaz_proizvoda_3():
    driver = start_browser("https://www.ctshop.rs/")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys("iphone")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys(Keys.RETURN)
    sleep(2)
    product = driver.find_element(By.XPATH,"//a[contains(text(),'Apple Iphone 16 Pro 256GB beli mobilni 6.3') and contains(text(),'Hexa Core Apple A18 Pro 8GB 256GB 48Mpx+12Mpx+48Mpx Dual Sim')]")
    product.click()
    sleep(1)
    assert driver.find_element(By.XPATH, "//span[text()='Šifra:']"), "Prikaz proizvoda nije ispravan"
    close_browser(driver)

def test_dodavanje_u_korpu_4():
    driver = start_browser("https://www.ctshop.rs/")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys("iphone")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys(Keys.RETURN)
    sleep(2)
    product = driver.find_element(By.XPATH,"//a[contains(text(),'Apple Iphone 16 Pro 256GB beli mobilni 6.3') and contains(text(),'Hexa Core Apple A18 Pro 8GB 256GB 48Mpx+12Mpx+48Mpx Dual Sim')]")
    product.click()
    sleep(1)
    driver.find_element(By.XPATH, "//button[@title='Dodaj u korpu']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Idi u korpu']").click()
    assert driver.find_element(By.XPATH, "//span[text()='Naziv proizvoda']") and driver.find_element(By.XPATH, "//th[text()='Količina']"), "Add to chart ne funkcionise"
    close_browser(driver)

def test_izbacivanje_iz_korpe_5():
    driver = start_browser("https://www.ctshop.rs/")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys("iphone")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys(Keys.RETURN)
    sleep(2)
    product = driver.find_element(By.XPATH,"//a[contains(text(),'Apple Iphone 16 Pro 256GB beli mobilni 6.3') and contains(text(),'Hexa Core Apple A18 Pro 8GB 256GB 48Mpx+12Mpx+48Mpx Dual Sim')]")
    product.click()
    sleep(1)
    driver.find_element(By.XPATH, "//button[@title='Dodaj u korpu']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Idi u korpu']").click()
    sleep(1)
    driver.find_element(By.XPATH,"//span[@id='removeItem']").click()
    sleep(1)
    assert driver.find_element(By.XPATH,"//h3[text()='Vaša korpa je trenutno prazna.']")
    close_browser(driver)

def test_filter_proizvoda_u_galeriji_6():
    driver = start_browser("https://www.ctshop.rs/")
    sleep(1)
    driver.find_element(By.XPATH, "//a[@id='laptopovi-tableti']").click()
    sleep(1)
    driver.find_element(By.XPATH,"//a[@title='Laptop računari']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[@title='Laptopovi']").click()
    driver.find_element(By.XPATH,"//label[text()='Apple M3']").click()
    driver.find_element(By.XPATH,"//button[text()='Primeni']").click()
    sleep(1)
    assert driver.find_element(By.XPATH,"//span[text()='Procesor']" and "//span[text()='Apple M3']")
    close_browser(driver)

def test_brzo_dodavanje_u_korpu_7():
    driver = start_browser("https://www.ctshop.rs/")
    actions = ActionChains(driver)
    sleep(1)
    actions.move_to_element(driver.find_element(By.XPATH, "//a[@id='laptopovi-tableti']")).perform()
    sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Laptopovi']").click()
    sleep(1)
    driver.execute_script("window.scrollBy(0, 500);")
    actions.move_to_element(driver.find_element(By.XPATH,"//a[contains(.,'Asus TUF Gaming A15 FA506NF-HN009 gejmerski laptop 15.6')]")).perform()
    sleep(1)
    driver.find_element(By.XPATH, "//a[@title='Dodaj proizvod u korpu']").click()
    sleep(1)
    assert driver.find_element(By.XPATH, "//div/a/span[contains(.,'1')]"), "Brzo dodavanje u korpu ne funkcionise"
    close_browser(driver)

def test_uvecavanje_kolicine_proizvoda_u_korpi_8():
    driver = start_browser("https://www.ctshop.rs/")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys("iphone")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys(Keys.RETURN)
    sleep(2)
    product = driver.find_element(By.XPATH,"//a[contains(text(),'Apple Iphone 16 Pro 256GB beli mobilni 6.3') and contains(text(),'Hexa Core Apple A18 Pro 8GB 256GB 48Mpx+12Mpx+48Mpx Dual Sim')]")
    product.click()
    sleep(1)
    driver.find_element(By.XPATH, "//button[@title='Dodaj u korpu']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Idi u korpu']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[@aria-label='Dodaj jos jedan']").click()
    sleep(1)
    assert driver.find_element(By.XPATH, "//input[@value='2']"), "Uvecavanje kolicine proizvoda u korpi ne funkcionise"
    close_browser(driver)

def test_umanjivanje_kolicine_proizvoda_u_korpi_8():
    driver = start_browser("https://www.ctshop.rs/")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys("iphone")
    sleep(1)
    driver.find_element(By.ID, "search-input-header").send_keys(Keys.RETURN)
    sleep(2)
    product = driver.find_element(By.XPATH,"//a[contains(text(),'Apple Iphone 16 Pro 256GB beli mobilni 6.3') and contains(text(),'Hexa Core Apple A18 Pro 8GB 256GB 48Mpx+12Mpx+48Mpx Dual Sim')]")
    product.click()
    sleep(1)
    driver.find_element(By.XPATH, "//button[@title='Dodaj u korpu']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Idi u korpu']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[@aria-label='Dodaj jos jedan']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[@aria-label='Oduzmi jedan']").click()
    sleep(1)
    assert driver.find_element(By.XPATH, "//input[@value='1']"), "Umanjivanje koicine proizvoda u korpi ne funkcionise"
    close_browser(driver)

def test_forma_za_prijavu_10():
    driver = start_browser("https://www.ctshop.rs")
    driver.find_element(By.XPATH, "//img[@alt='user']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//p[text()='Email i šifra']").click()
    assert driver.find_element(By.XPATH, "//button[@id='loginBtn']"), "Forma za prijavu ne funkcionise"
    close_browser(driver)

def test_forma_za_registraciju_11():
    driver = start_browser("https://www.ctshop.rs")
    driver.find_element(By.XPATH, "//img[@alt='user']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//p[text()='Email i šifra']").click()
    driver.find_element(By.XPATH, "//span[@id='create-account-new']").click()
    sleep(1)
    assert driver.find_element(By.XPATH, "//button[@id='registerBtn']"), "Forma za registraciju ne funkcionise"
    close_browser(driver)

def test_filter_proizvoda_na_strani_akcija_12():
    driver = start_browser("https://www.ctshop.rs")
    driver.find_element(By.XPATH, "//img[@alt='percent']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//div[contains(text(),'Telefoni')]/child::button").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[@href='/akcija-mobilni-telefoni']").click()
    sleep(1)
    assert "Mobilni telefoni | Akcija | Sniženje cena | Neverovatni popusti | Obezbedite svoj telefon po sniženoj ceni | CT shop" in driver.title, "Filtriranje proizvoda u sekciji akcije ne funkcionise"
    close_browser(driver)

def test_futer_facebook_link_13():
    driver = start_browser("https://www.ctshop.rs")
    driver.find_element(By.XPATH, "//img[@alt='CT Shop Facebook']").click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    assert "facebook.com" in driver.current_url, "Facebook link u futer sekciji ne funckionise"
    driver.switch_to.window(driver.window_handles[0])
    close_browser(driver)

def test_futer_facebook_link_14():
    driver = start_browser("https://www.ctshop.rs")
    driver.find_element(By.XPATH, "//img[@alt='CT Shop Instagram']").click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    assert "instagram.com" in driver.current_url, "Instagram link u futer sekciji ne funckionise"
    driver.switch_to.window(driver.window_handles[0])
    close_browser(driver)

def test_forma_ocene_proizvoda_15():
    driver = start_browser("https://www.ctshop.rs")
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH,"//a[@id='laptopovi-tableti']")).perform()
    driver.find_element(By.XPATH,"//a[.='Laptopovi']").click()
    sleep(2)
    driver.execute_script("window.scrollBy(0,500);")
    driver.find_element(By.XPATH,"//a[contains(.,'Asus TUF Gaming A15')]").click()
    sleep(2)
    driver.execute_script("window.scrollBy(0,1800);")
    sleep(1)
    driver.find_element(By.XPATH,"//a[.='Ocene']").click()
    assert "Srednja ocena" in driver.find_element(By.XPATH,"//div[@class='average-rating']").text, "Sekcija 'Ocene' u prozoru proizvoda se ne prikazuje"
    close_browser()

# def test_sort_by_function_():
#     driver = start_browser("https://www.ctshop.rs")
#     sleep(1)
#     driver.find_element(By.ID, "search-input-header").send_keys("iphone")
#     driver.find_element(By.ID, "search-input-header").send_keys(Keys.RETURN)
#     sleep(1)
#     driver.find_element(By.XPATH,"//span[text()='Punjači za telefon']").click()
#     sleep(1)
#     driver.find_element(By.XPATH, "//span[@id='sort-by']").click()
#     driver.find_element(By.XPATH, "//option[text()='Ceni rastuće']").click()
#     sleep(1)
#     price_elements = driver.find_elements(By.XPATH, "//span[@class='regular-price']")
#     prices = []
#     for price_element in price_elements:
#         price_text = price_element.text.replace(" RSD MP cena", "").strip()
#         prices.append(float(price_text))
#     assert prices == sorted(prices), f"Cene nisu sortirane {prices} : {sorted(prices)}"
#     close_browser(driver)

def close_browser(driver):
    driver.minimize_window()
    driver.close()