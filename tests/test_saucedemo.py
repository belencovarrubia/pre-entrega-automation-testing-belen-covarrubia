# Importamos Selenium y los componentes necesarios para las pruebas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  

import time

# Configuramos las opciones para el navegador (abrir maximizado para que sea mas comodo de visualizar)
opciones = Options()
opciones.add_argument("--start-maximized")

# preparamos el driver de Chrome
servicio = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servicio, options=opciones)

# Abrimos la página web de la prueba
navegador.get("https://www.saucedemo.com")


# Esperamos a que los campos estén visibles
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, "user-name"))
)

# ingresamos el nombre y la contraseña
navegador.find_element(By.ID, "user-name").send_keys("standard_user")
navegador.find_element(By.ID, "password").send_keys("secret_sauce")

#buscamos el botón de login y lo presionamos
navegador.find_element(By.ID, "login-button").click()


# esperamos a que cargue la página de inventario y lo validamos
try:
    WebDriverWait(navegador, 10).until(
        EC.url_contains("inventory")
    )
    print("✅ Login correcto: se nos redirgió a la página del inventario.")
except:
    print("❌ Error: no se redirigió correctamente.")


# Esperamos 10 segundos antes de cerrar (para que se pueda ver correctamente e interactuar)
time.sleep(10)

# Cerramos el navegador
navegador.quit()


