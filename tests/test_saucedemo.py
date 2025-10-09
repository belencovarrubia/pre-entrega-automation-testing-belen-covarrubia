# Importamos Selenium y componentes necesarios
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  

import time

# Configuramos opciones para el navegador (abrir maximizado para que sea mas comodo de visualizar)
opciones = Options()
opciones.add_argument("--start-maximized")

# preparamos el driver de Chrome
servicio = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servicio, options=opciones)

# Abrimos la página web de la prueba
navegador.get("https://www.saucedemo.com")

# Esperamos 10 segundos antes de cerrar (para que se pueda ver correctamente e interactuar)
time.sleep(10)

# Cerramos el navegador
navegador.quit()


