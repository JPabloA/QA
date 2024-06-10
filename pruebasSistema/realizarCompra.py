from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep

# Configurar las credenciales de usuario
USERNAME = os.getenv('LOGIN_USERNAME', 'cliente@mail.com')
PASSWORD = os.getenv('LOGIN_PASSWORD', 'cliente')

# Ruta de la imagen a subir
IMAGE_PATH = r"C:\Users\Mois\Downloads\comprobante_pago.jpeg"
PATH = 'img/realizarCompra/'

# Nuevos valores para los inputs
PROVINCIA = "San José"
CANTON = "San José"
DISTRITO = "Pavas"
DIRECCION = "De la iglesia católica 200 metros al sur"

# Crear un objeto WebDriver
driver = webdriver.Firefox()

def wait_for_images_to_load(driver):
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script(
            'return Array.from(document.images).every(img => img.complete && img.naturalHeight !== 0)'
        )
    )

try:
    # -------------------- Iniciar sesión --------------------
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
    driver.save_screenshot(f'{PATH}/login_fields_filled.png')

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

    wait_for_images_to_load(driver)

    # Tomar una captura de pantalla del resultado del login
    driver.save_screenshot(f'{PATH}/login_result.png')

    # -------------------- Agregar al carrito --------------------
    # Localizar el anchor con el atributo title "tienda"
    tienda_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="tienda"]'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", tienda_link)

    # Usar JavaScript para hacer clic en el anchor con el atributo title "tienda"
    driver.execute_script("arguments[0].click();", tienda_link)

    WebDriverWait(driver, 50).until(
        EC.url_changes(driver.current_url)
    )

    # # Esperar a que todas las imágenes se carguen completamente
    # wait_for_images_to_load(driver)
    
    # Tomar una captura de pantalla de la página después de hacer clic en "store"
    driver.save_screenshot(f'{PATH}/store_view.png')
    
    # Seleccionar el producto a comprar
    # Localizar el tile del producto con el nombre específico
    product_tile = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "relative flex flex-col overflow-hidden border cursor-pointer")]//h3[contains(text(),"Paleta de colorete y bronceador de Kiko2")]'))
    )
    
    # Hacer clic en el tile del producto
    product_tile.click()
    
    # Esperar a que todas las imágenes se carguen completamente
    wait_for_images_to_load(driver)
    
    # Tomar una captura de pantalla después de hacer clic en el producto
    driver.save_screenshot(f'{PATH}/product_view.png')
    
   # Esperar a que la página del producto se cargue completamente
    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )

    # Esperar hasta que el botón "Agregar al carrito" esté presente y sea clickeable
    add_to_cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Agregar a carrito"]'))
    )

    # Hacer clic en el botón "Agregar al carrito"
    add_to_cart_button.click()

    WebDriverWait(driver, 50).until(
        EC.url_changes(driver.current_url)
    )

    image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Product Image']")))

    driver.save_screenshot(f'{PATH}/shipping_info.png')

    # ------------------ Realizar la compra ------------------	

    # Localizar el anchor con el atributo title "galería"
    carrito_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="carrito de compra"]'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", carrito_link) 

    # Usar JavaScript para hacer clic en el anchor con el atributo title "galería"
    driver.execute_script("arguments[0].click();", carrito_link)

    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='Imagen']"))
    )

    driver.save_screenshot(f'{PATH}/carrito_page.png')

    buy_buttom = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Finalizar compra"]'))
    )

    # Desplazar hasta el botón antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", buy_buttom)

    # Usar JavaScript para hacer clic en el botón con el texto "Guardar"
    driver.execute_script("arguments[0].click();", buy_buttom)

    driver.save_screenshot(f'{PATH}/shipping_info.png')

    sleep(2)

    # Modificar los inputs con los IDs "contentName", "description" y "clave"
    province_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'provincia'))
    )
    province_input.send_keys(PROVINCIA)

    canton_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='campo1'][1]"))
    )
    canton_input.send_keys(CANTON)

    # Esperar y modificar el segundo input
    district_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='campo1'][2]"))
    )
    district_input.send_keys(DISTRITO)

    address_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'campo2'))
    )
    address_input.send_keys(DIRECCION)

    # Localizar el input con el id "imagen"
    image_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'imagen'))
    )

    # Desplazar hasta el input antes de interactuar
    driver.execute_script("arguments[0].scrollIntoView();", image_input)

    # Enviar la ruta del archivo directamente al input de tipo file
    image_input.send_keys(IMAGE_PATH)

    # Tomar una captura de pantalla de la página después de seleccionar la imagen
    driver.save_screenshot(f'{PATH}/image_selected_page.png')

    # Localizar el botón de signin
    shipping_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )

    # Dar clic al botón de signin
    shipping_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )

    driver.save_screenshot(f'{PATH}/post_shipping.png')

    # sleep(2)
    
finally:
    # Cerrar el navegador
    driver.quit()
