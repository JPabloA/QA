from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Ruta de la imagen a subir
IMAGE_PATH = r"C:\Users\josep\Downloads\testImage.jpg"

# Nuevos valores para los inputs
NEW_CONTENT_NAME = "Test"
NEW_DESCRIPTION = "Esta es una descripcion para la prueba del RF03 Modificar contenido"
NEW_CLAVE = "#test"

# Crear un objeto WebDriver
driver = webdriver.Firefox()

def wait_for_images_to_load(driver):
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script(
            'return Array.from(document.images).every(img => img.complete && img.naturalHeight !== 0)'
        )
    )


try:
    # Abrir la página de galería directamente
    driver.get('https://master.d2fcoa3vsgqot0.amplifyapp.com/adminView/galleryAdmin')

    # Esperar a que la nueva página se cargue
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://master.d2fcoa3vsgqot0.amplifyapp.com/adminView/galleryAdmin')
    )
    
     # Esperar a que la página se cargue completamente
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )

    # Esperar a que un elemento clave esté presente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//img[@alt="Element Image"]'))
    )

    # Esperar a que todas las imágenes se carguen completamente
    wait_for_images_to_load(driver)
    
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
    
    # Esperar a que todas las imágenes se carguen completamente
    wait_for_images_to_load(driver)
    
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

    # Esperar a que la página se cargue completamente
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    
    # Esperar a que todas las imágenes se carguen completamente
    wait_for_images_to_load(driver)

    # Tomar una captura de pantalla de la página después de hacer clic en el botón "Guardar"
    driver.save_screenshot('img/modifyContent/returned_to_galeria_page.png')

finally:
    # Cerrar el navegador
    driver.quit()