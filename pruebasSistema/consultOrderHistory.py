import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Configurar las credenciales de usuario
# Usuario normal
USERNAME_USER = os.getenv('LOGIN_USERNAME', 'cliente@mail.com')
PASSWORD_USER = os.getenv('LOGIN_PASSWORD', 'cliente')

USERNAME_ADMIN = os.getenv('LOGIN_USERNAME', 'moisessoes@gmail.com')
PASSWORD_ADMIN = os.getenv('LOGIN_PASSWORD', '123456')


# Crear un objeto WebDriver
driver = webdriver.Firefox()

def wait_for_images_to_load(driver):
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script(
            'return Array.from(document.images).every(img => img.complete && img.naturalHeight !== 0)'
        )
    )
    
try:
    # Abrir la página de login
    driver.get('https://master.d2fcoa3vsgqot0.amplifyapp.com/signin')
    
    #-------------------------------------------------------------------
    # 0. Hacer el Login del usuario 
    #-------------------------------------------------------------------
    
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    
    # Llenar los campos de usuario y contraseña
    username_field.send_keys(USERNAME_USER)
    password_field.send_keys(PASSWORD_USER)

    # Tomar una captura de pantalla de los campos llenados
    driver.save_screenshot('img/consultHistory/login_fields_filled.png')

    # Localizar el botón de signin
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )

    # Dar clic al botón de signin
    signin_button.click()

    # Esperar a que la nueva página se cargue
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://master.d2fcoa3vsgqot0.amplifyapp.com/userView/mainPage')
    )
    
    # Esperar a que todas las imágenes se carguen completamente
    wait_for_images_to_load(driver)
    
    # Tomar una captura de pantalla del resultado del login
    driver.save_screenshot('img/consultHistory/home_page.png')

    #-------------------------------------------------------------------
    # 1. Ir al apartado de consultar historial de pedidos 
    #-------------------------------------------------------------------
    
     # Localizar el anchor con el atributo title "carrito de compra"
    history_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="historial de pedidos"]'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", history_link)

    # Usar JavaScript para hacer clic en el anchor con el atributo title "historial de pedidos"
    driver.execute_script("arguments[0].click();", history_link)

    # Esperar a que la nueva página se cargue (opcional, basado en el comportamiento esperado)
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )
    
    # Esperar un tiempo fijo
    time.sleep(2)
    
    # Tomar una captura de pantalla del cart history
    driver.save_screenshot('img/consultHistory/cart_history.png')
      
finally:
    # Cerrar el navegador
    driver.quit()
