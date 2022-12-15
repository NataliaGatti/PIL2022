import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Definir la función de comparar textos de los links y botones reutilizables
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

# Validar que el email ingresado sea válido
try:
    errorEmail = driver.find_element(
        By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]").is_displayed()
    if errorEmail:
        errorEmailText = driver.find_element(
            By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]").text
        assert errorEmailText != "Entre con un e-mail válido", "El email ingresado no es válido"
except NoSuchElementException:
    print("El email ingresado es válido")
    
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
time.sleep(15)

# La validación del token se realiza manualmente
# token = driver.find_element(By.NAME, "token")
# token.send_keys("123456")

# Validar presencia del input Contraseña y que se pueda completar con un dato válido
password = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/label/div/input")
is_password_visible = password.is_displayed()
print(is_password_visible, "El input de Password es visible")
password.send_keys("PilTest2022")
time.sleep(2)

# Validación de las condiciones del input Contraseña
errorPassword1 = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/div/div[1]/div").get_attribute("class")
# print(errorPassword1)
assert errorPassword1 == "flex flex-row c-success", "Falta al menos una letra mayúscula en la contraseña"
errorPassword2 = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/div/div[2]/div").get_attribute("class")
assert errorPassword2 == "flex flex-row c-success", "Falta al menos una letra minúscula en la contraseña"
errorPassword3 = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/div/div[3]/div").get_attribute("class")
assert errorPassword3 == "flex flex-row c-success", "Falta al menos un número en la contraseña"
errorPassword4 = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/div/div[4]/div").get_attribute("class")
assert errorPassword4 == "flex flex-row c-success", "Deben ser como mínimo 8 caracteres"
print("Contraseña válida")

# Validar presencia del input Confirmar Contraseña y que se pueda completar con un dato válido
passwordConfirm = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[3]/label/div/input")
is_password_confirm_visible = passwordConfirm.is_displayed()
print(is_password_confirm_visible, "El input de Confirmar Password es visible")
passwordConfirm.send_keys("PilTest2022")
time.sleep(2)

# Validar presencia del botón "Crear" y que su texto sea "Crear"
crearButton = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[4]/div[2]/button")
is_crear_button_visible = crearButton.is_displayed()
print(is_crear_button_visible, "Botón Crear es visible")
crearButtonText = crearButton.text
assert crearButtonText == "Crear", "El botón Crear no es visible o no tiene el texto correspondiente"
requirement = "Crear"
labelObtained = crearButton.text
compareText()
crearButton.click()
time.sleep(10)

# Validación de las condiciones del input Código de acceso y Confirmar Contraseña
try:
    errorCode = driver.find_element(
        By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]").is_displayed()
    if errorCode:
        errorCode = driver.find_element(
            By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]").text
        assert errorCode != "El código de acceso es incorrecto", "El código de acceso es incorrecto"
        assert errorCode != "Ingrese un código de acceso válido de 6 dígitos", "Ingrese un código de acceso válido de 6 dígitos"
except NoSuchElementException:
    print("El código de acceso es válido")

try:
    passwordConfirmation = driver.find_element(
        By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[4]").is_displayed()
    if passwordConfirmation:
        errorPasswordConfirmation = driver.find_element(
            By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[4]").text
        assert errorPasswordConfirmation != "Confirmación de contraseña está incorrecta", "Las contraseñas no coinciden"
except NoSuchElementException:
    print("La Confirmación de Contraseña es correcta")

# Cerrar el webdriver
driver.close()

# Ejecutar el print de exitoso si todo se ejecutó ok
print("Test exitoso: Usuario creado en la base de datos")
