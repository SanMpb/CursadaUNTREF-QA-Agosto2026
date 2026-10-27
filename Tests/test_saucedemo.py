import pytest
 
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
 
 
@pytest.fixture

def driver():

    # Abrir Chrome

    driver = webdriver.Chrome()

    driver.maximize_window()
 
    # Entrar a SauceDemo

    driver.get("https://www.saucedemo.com/")
 
    yield driver
 
    # Cerrar Chrome al terminar

    driver.quit()
 
 
def test_ordenar_productos_precio_menor_a_mayor(driver):
 
    # LOGIN

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()
 
    # Esperar que aparezca el selector de ordenamiento

    wait = WebDriverWait(driver, 10)
 
    selector_element = wait.until(

        EC.presence_of_element_located(

            (By.CLASS_NAME, "product_sort_container")

        )

    )
 
    # Seleccionar Price (low to high)

    selector = Select(selector_element)

    selector.select_by_value("lohi")
 
    # Obtener todos los precios

    elementos_precio = driver.find_elements(

        By.CLASS_NAME,

        "inventory_item_price"

    )
 
    # Convertir "$7.99" etc. a números

    precios = [

        float(elemento.text.replace("$", ""))

        for elemento in elementos_precio

    ]
 
    # Mostrar precios en consola

    print("Precios encontrados:", precios)
 
    # Verificar que estén ordenados

    assert precios == sorted(precios)
 