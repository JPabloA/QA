from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Configurar las credenciales de usuario
USERNAME = os.getenv('LOGIN_USERNAME', 'moisessoes@gmail.com')
PASSWORD = os.getenv('LOGIN_PASSWORD', '123456')

# Ruta de la imagen a subir
IMAGE_PATH = r"C:\Users\Mois\Downloads\menuconfig.png"

# Nuevos valores para los inputs
NEW_CONTENT_NAME = "si"
NEW_DESCRIPTION = "Nueva descripción"
NEW_CLAVE = "#clave"

# Crear un objeto WebDriver
driver = webdriver.Firefox()

try:
    # Abrir la página de login
    driver.get('https://master.d2fcoa3vsgqot0.amplifyapp.com/signin')

    # Localizar los campos de usuario y contraseña
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )

    # Llenar los campos de usuario y contraseña
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    # Tomar una captura de pantalla de los campos llenados
    driver.save_screenshot('img/modifyContent/login_fields_filled.png')

    # Localizar el botón de signin
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )

    # Dar clic al botón de signin
    signin_button.click()

    # Esperar a que la nueva página se cargue
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://master.d2fcoa3vsgqot0.amplifyapp.com/adminView/mainPageAdmin')
    )

    # Tomar una captura de pantalla del resultado del login
    driver.save_screenshot('img/modifyContent/login_result.png')

    # Localizar el anchor con el atributo title "galería"
    galeria_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="galería"]'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", galeria_link)

    # Usar JavaScript para hacer clic en el anchor con el atributo title "galería"
    driver.execute_script("arguments[0].click();", galeria_link)

    # Esperar a que la nueva página se cargue (opcional, basado en el comportamiento esperado)
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )

    # Tomar una captura de pantalla de la página después de hacer clic en "galería"
    driver.save_screenshot('img/modifyContent/galeria_page.png')

    # Localizar el primer elemento con alt="Element Image"
    element_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//img[@alt="Element Image"]'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", element_image)

    # Usar JavaScript para hacer clic en el primer elemento con alt="Element Image"
    driver.execute_script("arguments[0].click();", element_image)

    # Esperar a que la nueva página se cargue (opcional, basado en el comportamiento esperado)
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )

    # Tomar una captura de pantalla de la página después de hacer clic en el elemento de imagen
    driver.save_screenshot('img/modifyContent/element_image_page.png')

    # Localizar el anchor con la clase específica
    specific_anchor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.text-neutral-800.dark\\:text-neutral-200'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", specific_anchor)

    # Usar JavaScript para hacer clic en el anchor con la clase específica
    driver.execute_script("arguments[0].click();", specific_anchor)

    # # Esperar a que la URL cambie después de hacer clic en el anchor
    # WebDriverWait(driver, 10).until(
    #     EC.url_changes(driver.current_url)
    # )

    # Tomar una captura de pantalla de la página después de hacer clic en el anchor
    driver.save_screenshot('img/modifyContent/specific_anchor_page.png')

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
    driver.save_screenshot('img/modifyContent/modify_button_page.png')

    # Localizar el input con el id "imagen"
    image_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'imagen'))
    )

    # Desplazar hasta el input antes de interactuar
    driver.execute_script("arguments[0].scrollIntoView();", image_input)

    # Enviar la ruta del archivo directamente al input de tipo file
    image_input.send_keys(IMAGE_PATH)

    # Tomar una captura de pantalla de la página después de seleccionar la imagen
    driver.save_screenshot('img/modifyContent/image_selected_page.png')

    # Modificar los inputs con los IDs "contentName", "description" y "clave"
    content_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'contentName'))
    )
    
    # Limpiar el contenido del campo de entrada
    for _ in range(len(content_name_input.get_attribute("value"))):
        content_name_input.send_keys(Keys.BACKSPACE)
    else:
        content_name_input.send_keys(NEW_CONTENT_NAME)

    description_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'description'))
    )
    description_input.clear()
    description_input.send_keys(NEW_DESCRIPTION)

    clave_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'clave'))
    )
    clave_input.clear()
    clave_input.send_keys(NEW_CLAVE)

    # Tomar una captura de pantalla después de modificar los inputs
    driver.save_screenshot('img/modifyContent/inputs_modified_page.png')

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

    # Tomar una captura de pantalla de la página después de volver a la galería
    driver.save_screenshot('img/modifyContent/returned_to_galeria_page.png')

finally:
    # Cerrar el navegador
    driver.quit()
