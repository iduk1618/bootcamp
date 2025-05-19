from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def start_browser(url):
    driver = webdriver.Chrome(options=Options(),service=Service())
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    return driver

def test_mailing_list_form():
    driver = start_browser("https://horn.rs/")
    driver.execute_script("window.scrollBy(0,4500);")
    test_email = "test@gmail.com"
    sleep(0.5)
    email_element = driver.find_element(By.XPATH,"//input[@placeholder='E-mail']")
    email_element.click()
    sleep(0.5)
    email_element.send_keys(f"{test_email}")
    print(f"Unosim {test_email} u formu za mailing listu.")
    sleep(0.5)
    email_form = driver.find_element(By.XPATH, "//input[@value and @placeholder='E-mail']").get_attribute("value")
    print(f"Vredmost polja Email: {email_form}")
    sleep(0.5)
    assert email_form == test_email, "Forma za mailing listu nije ispravna"
    sleep(0.5)
    close_browser(driver)

def test_popular_categories():
    driver = start_browser("https://horn.rs/")
    menu_items = {
        'Lovacke Čizme': 'Lovacke Čizme | HORN',
        'Lovacke Cipele': 'Lovacke Cipele | HORN',
        'Lovačke Kamere': 'Lovačke Kamere | HORN',
        'Lovacke Jakne': 'Lovacke Jakne | HORN',
        'Aktivni veš': 'Aktivni veš | HORN',
        'Lovacki Kompleti': 'Lovacki Kompleti | HORN',
        'Lovački Džemperi': 'Lovački Džemperi | HORN',
        'Lovački Šeširi': 'Lovački Šeširi | HORN',
        'Lovacki Prsluci': 'Lovacki Prsluci | HORN',
        'Lovacke Pantalone': 'Lovacke Pantalone | HORN'
    }
    sve_stranice_ucitane = True
    try:
        for item, expected_title in menu_items.items():
            print(f"Testiram {item}")
            sleep(0.5)
            link_element = driver.find_element(By.XPATH, f"//p[contains(text(),'{item}') and @class='text-white text-[20px] mt-0 mb-0 leading-none']")
            link_element.click()
            sleep(1)
            if expected_title not in driver.title:
                print(f"Stranica '{item}' nije ucitana. Ocekivano: '{expected_title}', Stvarno: '{driver.title}'")
                sve_stranice_ucitane = False
            driver.back()
            sleep(1)
    except Exception as e:
        print(f"Test za '{item}' nije uspeo: {e}")
    finally:
        assert sve_stranice_ucitane, "Test nije uspešan! Neke stranice nisu uspešno učitane."
        close_browser(driver)

def test_search():
    found_elements = []
    search_keyword = "Deerhunter"
    driver = start_browser("https://horn.rs/")
    search_element = driver.find_element(By.XPATH,"//input[@placeholder='Pretraga...']")
    search_element.click()
    search_element.send_keys(f"{search_keyword}")
    sleep(1)
    driver.find_element(By.XPATH,"//button[contains(text(),'Pogledaj sve')]").click()
    sleep(1)
    search_elements = driver.find_elements(By.XPATH,"//p[contains(@class, 'text-primary') and contains(@class, 'font-normal')]")
    try:
        for element in search_elements:
            product_name = element.text.strip()
            if f"{search_keyword}" in product_name:
                found_elements.append(product_name)
        formatted_output = "\n".join(found_elements)
        print(f"Pronadjeni proizvodi: {formatted_output}")
    except Exception as e:
        print(f"Doslo je do greske {e}")
    finally:
        assert len(found_elements) > 0, "Nije pronadjen ni jedan rezultat"
        close_browser(driver)

def test_login_form():
    driver = start_browser("https://horn.rs/")
    login_form = False
    email = "test@gmail.com"
    password = "sifra123"
    driver.find_element(By.XPATH, "//div[@class and contains(text(), 'Nalog')]").click()
    sleep(1)
    email_element = driver.find_element(By.XPATH, "//input[@type='email']")
    pass_element = driver.find_element(By.XPATH, "//input[@type='password']")
    email_element.click()
    email_element.send_keys(email)
    print(f"Unosim {email} u polje 'Email'")
    pass_element.click()
    pass_element.send_keys(password)
    print(f"Unosim {password}  u polje 'Lozinka'")
    if email_element.get_attribute("value") == email and pass_element.get_attribute("value") == password:
        login_form = True
    formated_email = email_element.get_attribute("value")
    formated_password = pass_element.get_attribute("value")
    print(f"Vrednost polja Email: {formated_email}")
    print(f"Vrednost polja Lozinka: {formated_password}")
    assert login_form, "Forma za login nije ispravna"
    close_browser(driver)

def test_register_form():
    driver = start_browser("https://horn.rs/")
    register_form = False
    driver.find_element(By.XPATH, "//div[@class and contains(text(), 'Nalog')]").click()
    sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'Registruj se')]").click()
    sleep(1)
    reg_form_elements = {
        'Ime':'Pera',
        'Prezime':'Peric',
        'Adresa':'Jovana Cirlova 11',
        'Grad':'Beograd',
        'Poštanski broj':'11120',
        'Telefon':'0682223355',
        'Email':'peraperic@gmail.com',
        'Lozinka':'sifra123',
        'Potvrdi Lozinku':'sifra123'
    }
    for element,input_value in reg_form_elements.items():
        reg_form_element = driver.find_element(By.XPATH, f"//input[@placeholder='{element}']")
        reg_form_element.click()
        reg_form_element.send_keys(f"{input_value}")
        print(f"Unosim u polje {element} tekst: {input_value}")
        sleep(0.2)

    for element,input_value in reg_form_elements.items():
        reg_form_element = driver.find_element(By.XPATH, f"//input[@placeholder='{element}']").get_attribute("value")
        print(f"Proveravam polje {element}, vrednost polja je: {reg_form_element}")
        if reg_form_element != input_value:
            register_form = False
        else:
            register_form = True
    calendar_element = driver.find_element(By.XPATH, "//div[contains(text(),'Vaš datum rođenja')]")
    calendar_element.click()
    for i in range(20):
        driver.find_element(By.XPATH, "//button[@title='Previous Year']").click()
    driver.find_element(By.XPATH, "//button[@class and contains(text(),'1')]").click()
    calendar_value = driver.find_element(By.XPATH, "//div[@class='w-full h-[58px] border border-borderprimary rounded-[10px] px-[17px] py-[16px] cursor-pointer flex items-end pl-10 text-primary']").text
    print(f"Proveravam polje: Vaš datum rođenja, vrednost polja kalendar je: {calendar_value}")
    if calendar_value != None:
        register_form = True
    else:
        register_form = False
    assert register_form, "Forma za registraciju ne funkcionise."

def close_browser(driver):
    driver.minimize_window()
    driver.close()