import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

requirement = ()  # Expected Result
labelObtained = ()  # Actual Result


def compareText():
    if requirement in labelObtained:
        print("Success: El texto corresponde con el definido")
    else:
        print("Fail: El texto no es correcto, no coincide con el definido")


# Iniciar el webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://www.bensimon.com.ar/")
driver.maximize_window()
time.sleep(2)

# Cerrar el modal para habilitar el home
closeModal = driver.find_element(
    By.CLASS_NAME, "vtex-modal-layout-0-x-closeButton")
closeModal.click()

# Entrar al avatar del login/register en la navbar
avatar = driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[5]/div/div/button")
avatar.click()
time.sleep(2)

# Validar presencia, texto y redireccionamiento del link "Volver"
loginButton = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[2]/div/button")
loginButton.click()
time.sleep(2)
link = driver.find_element(By.LINK_TEXT, "¿No tiene una cuenta? Regístrese")
link.click()
time.sleep(2)
volver = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div[1]/button")
is_volver_link_visible = volver.is_displayed()
print(is_volver_link_visible, "El link Volver es visible")
linkTextVolver = volver.text
assert linkTextVolver == "Volver", "El link Volver no es visible o no tiene el texto correspondiente"
requirement = "Volver"
labelObtained = volver.text
# print(labelObtained)
compareText()
volver.click()
time.sleep(2)

# Validar presencia, texto y redireccionamiento del link "¿No tiene una cuenta? Regístrese"
link = driver.find_element(By.LINK_TEXT, "¿No tiene una cuenta? Regístrese")
is_link_visible = link.is_displayed()
print(is_link_visible, "El link ¿No tiene una cuenta? Regístrese es visible")
linkTextCuenta = link.text
assert linkTextCuenta == "¿No tiene una cuenta? Regístrese", "El link ¿No tiene una cuenta? Regístrese, no es visible o no tiene el texto correspondiente"
link.click()
time.sleep(2)
requirement = "¿No tiene una cuenta? Regístrese"
labelObtained = linkTextCuenta
compareText()

# Validar presencia del input Email y que se pueda completar con un dato
email = driver.find_element(By.NAME, "email")
is_email_visible = driver.find_element(By.NAME, "email").is_displayed()
print(is_email_visible, "El input de Email es visible")
email.send_keys("nataliagatti15@hotmail.com")
time.sleep(2)

# Validar presencia del botón "Enviar" y que su texto sea "Enviar"
enviarButton = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/button")
is_enviar_button_visible = enviarButton.is_displayed()
print(is_enviar_button_visible, "Botón Enviar es visible")
enviarButtonText = enviarButton.text
assert enviarButtonText == "Enviar", "El botón Enviar no es visible o no tiene el texto correspondiente"
requirement = "Enviar"
labelObtained = enviarButton.text
compareText()
enviarButton.click()
time.sleep(2)

# Validar que al verificar que el email ya se encuentra registrado en la base de datos no permite avanzar con la creación de un nuevo usuario
#errorMessage = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]").text
# print(errorMessage)
#assert errorMessage == "El email ya se encuentra registrado", "Test fallido: Permite avanzar en la creación de usuario con un email ya registrado"
#print("Test exitoso: Falla la creación de usuario cuando el email ya se encuentra registrado previamente en la base de datos")
#driver.close()
try:
    errorMessage = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]").is_displayed()
    if errorMessage:
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]").text

        assert errorMessage != "El email ya se encuentra registrado", "Test exitoso: Falla la creación de usuario cuando el email ya se encuentra registrado previamente en la base de datos"
except NoSuchElementException:
    print("Test fallido: Permite avanzar en la creación de usuario con un email ya registrado")
driver.close()