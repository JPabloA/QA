from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep

# Configurar las credenciales de usuario
USERNAME = os.getenv('LOGIN_USERNAME', 'moisessoes@gmail.com')
PASSWORD = os.getenv('LOGIN_PASSWORD', '123456')

PATH = 'img/modifyCalendar/'

# Nuevos valores para los inputs
NEW_EVENT_NAME = "Klupp Casemiro"
NEW_EVENT_CLIENT = "Casemiro Clopp"
NEW_EVENT_LOCATION = "Estadio Santiago Bernabeu"
NEW_EVENT_DESCRIPTION = "Necesita maquillaje de Jesús rey de Reyes"

# Crear un objeto WebDriver
driver = webdriver.Firefox()

def wait_for_images_to_load(driver):
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script(
            'return Array.from(document.images).every(img => img.complete && img.naturalHeight !== 0)'
        )
    )
try:
   
    driver.get('https://master.d2fcoa3vsgqot0.amplifyapp.com/adminView/calendar')
    
    # -------------------- Modificar Entrada de Agenda --------------------
    
    sleep(2)

    # Tomar una captura de pantalla de la página después de hacer clic en "store"
    driver.save_screenshot(f'{PATH}/calendar_view.png')

    # Esperar a que el primer párrafo <p> esté presente
    first_paragraph = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))

    # Hacer clic en el primer párrafo
    first_paragraph.click()

    WebDriverWait(driver, 50).until(
        EC.url_changes(driver.current_url)
    )
    
    sleep(2)
    driver.save_screenshot(f'{PATH}/entrada.png')

    # Localizar el anchor con la clase específica
    specific_anchor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.text-neutral-800.dark\\:text-neutral-200'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", specific_anchor)

    # Usar JavaScript para hacer clic en el anchor con la clase específica
    driver.execute_script("arguments[0].click();", specific_anchor)

    # Tomar una captura de pantalla de la página después de hacer clic en el anchor
    driver.save_screenshot(f'{PATH}/specific_anchor_page.png')

     # Localizar el botón con el texto "Modificar"
    modify_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Modificar"]'))
    )

    # Desplazar hasta el botón antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", modify_button)

    # Usar JavaScript para hacer clic en el botón con el texto "Modificar"
    driver.execute_script("arguments[0].click();", modify_button)

    # Esperar a que la URL cambie después de hacer clic en el botón "Modificar"
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )

    # Tomar una captura de pantalla de la página después de hacer clic en el botón "Modificar"
    driver.save_screenshot(f'{PATH}/modify_button_page.png')

    #  -------------------- Modificar Entrada de Agenda --------------------
    # Modificar los inputs con los IDs "eventName", "eventClient", "eventLocation" y "clave"
    event_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'eventName'))
    )

    # Limpiar el contenido del campo de entrada
    for _ in range(len(event_name_input.get_attribute("value"))):
        event_name_input.send_keys(Keys.BACKSPACE)
    else:
        event_name_input.send_keys(NEW_EVENT_NAME)

    event_client_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'eventClient'))
    )

    for _ in range(len(event_client_input.get_attribute("value"))):
        event_client_input.send_keys(Keys.BACKSPACE)
    else:
        event_client_input.send_keys(NEW_EVENT_CLIENT)

    event_location_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'eventLocation'))
    )

    for _ in range(len(event_location_input.get_attribute("value"))):
        event_location_input.send_keys(Keys.BACKSPACE)
    else:
        event_location_input.send_keys(NEW_EVENT_LOCATION)

    event_description_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'clave'))
    )

    event_description_input.clear()
    event_description_input.send_keys(NEW_EVENT_DESCRIPTION)

    # Tomar una captura de pantalla después de modificar los inputs
    driver.save_screenshot(f'{PATH}/inputs_modified_page.png')

    # Localizar el botón con el texto "Guardar"
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Guardar"]'))
    )

    # Desplazar hasta el botón antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", save_button)

    # Usar JavaScript para hacer clic en el botón con el texto "Guardar"
    driver.execute_script("arguments[0].click();", save_button)

    # Esperar a que la URL cambie después de hacer clic en el botón "Guardar"
    WebDriverWait(driver, 50).until(
        EC.url_changes(driver.current_url)
    )

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))

    # Tomar una captura de pantalla de la página después de volver a la galería
    driver.save_screenshot(f'{PATH}/returned_to_galeria_page.png')

    # Esperar a que el primer párrafo <p> esté presente
    first_paragraph2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))

    # Hacer clic en el primer párrafo
    first_paragraph2.click()
    
    sleep(2)
    driver.save_screenshot(f'{PATH}/entrada_modificada.png')


finally:
    # Cerrar el navegador
    driver.quit()
