from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import getpass

usuario_facebook = input("Digite seu usuário do Facebook: ")
senha_facebook = getpass.getpass("Digite sua senha: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com")
sleep(1)

campo_usuario = driver.find_element_by_id('email')
campo_usuario.send_keys(usuario_facebook)
campo_senha = driver.find_element_by_id('pass')
campo_senha.send_keys(senha_facebook)
botao_login = driver.find_element_by_id('u_0_b')
botao_login.click()
print("Logado")
input("Precione qualquer tecla para sair.")
driver.quit()
print("Fim")
