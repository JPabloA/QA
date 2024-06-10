import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Configurar las credenciales de usuario
USERNAME = os.getenv('LOGIN_USERNAME', 'testing@gmail.com')
PASSWORD = os.getenv('LOGIN_PASSWORD', '123456')

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
    driver.save_screenshot('img/deleteProductFromCart/login_fields_filled.png')

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
    driver.save_screenshot('img/deleteProductFromCart/login_result.png')
    
    #-------------------------------------------------------------------
    # 1.Verificar que el usuario no tenga nada en su carrito de compras
    #-------------------------------------------------------------------
    
    # Localizar el anchor con el atributo title "carrito de compra"
    cart_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="carrito de compra"]'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", cart_link)

    # Usar JavaScript para hacer clic en el anchor con el atributo title "carrito de compra"
    driver.execute_script("arguments[0].click();", cart_link)

    # Esperar a que la nueva página se cargue (opcional, basado en el comportamiento esperado)
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )
    
    # Esperar un tiempo fijo
    time.sleep(2)
    
    # Tomar una captura de pantalla del carrito empty
    driver.save_screenshot('img/deleteProductFromCart/empty_cart.png')
    
    #-------------------------------------------------------------------
    # 2. Tienda y agregar producto al carrito
    #-------------------------------------------------------------------
    
    # Localizar el anchor con el atributo title "tienda"
    tienda_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="tienda"]'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", tienda_link)

    # Usar JavaScript para hacer clic en el anchor con el atributo title "tienda"
    driver.execute_script("arguments[0].click();", tienda_link)

    # Esperar a que todas las imágenes se carguen completamente
    wait_for_images_to_load(driver)
    
    # Tomar una captura de pantalla de la página después de hacer clic en "store"
    driver.save_screenshot('img/deleteProductFromCart/store_view.png')
    
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
    driver.save_screenshot('img/deleteProductFromCart/product_view.png')
    
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

    #-------------------------------------------------------------------
    # 3. Volver a carrito y eliminar el producto
    #-------------------------------------------------------------------
    
    # Localizar el anchor con el atributo title "carrito de compra"
    cart_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="carrito de compra"]'))
    )

    # Desplazar hasta el elemento antes de hacer clic
    driver.execute_script("arguments[0].scrollIntoView();", cart_link)

    # Usar JavaScript para hacer clic en el anchor con el atributo title "carrito de compra"
    driver.execute_script("arguments[0].click();", cart_link)

    # Esperar a que la nueva página se cargue (opcional, basado en el comportamiento esperado)
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )
    
    # Esperar a que los productos del carrito se carguen completamente
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//button[text()="-"]'))
    )

    # Esperar a que todas las imágenes se carguen completamente
    wait_for_images_to_load(driver)
    
    # Tomar una captura de pantalla de la página después de hacer clic en "el carrito de compras"
    driver.save_screenshot('img/deleteProductFromCart/userCart_view.png')
    
    # Localizar el botón de disminuir cantidad del primer producto
    reduce_quantity_button = driver.find_elements(By.XPATH, '//button[text()="-"]')[0]
    
    #  Esperar a que todas las imágenes se carguen completamente
    wait_for_images_to_load(driver)
    
    # Tomar una captura de pantalla antes de disminuir la cantidad
    driver.save_screenshot('img/deleteProductFromCart/beforeReduce_cuantity.png')
    
    # Hacer clic en el botón de disminuir cantidad
    reduce_quantity_button.click()
    
    # Esperar un tiempo prudencial para que los cambios se reflejen en la página
    time.sleep(2)
    
    # Tomar una captura de pantalla después de disminuir la cantidad
    driver.save_screenshot('img/deleteProductFromCart/afterReduce_cuantity.png')


finally:
    # Cerrar el navegador
    driver.quit()
