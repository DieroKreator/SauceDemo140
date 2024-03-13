# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By


# 2 - Classe (Opcional)
class Teste_Produtos(): 

    # 2.1 - Atributos
    url = "https://www.saucedemo.com"         # endereco do site alvo

    # 2.2 Funções e Métodos
    def setup_method(self, method):             # metodo pra inicializacao dos testes
        self.driver = webdriver.Chrome()  # instancia o objeto do selenium como Chrome
        self.driver.implicitly_wait(10)   # define o tempo de espera padrão por elementos em 10 segundos

    def teardown_method(self, method): # metodo de finalizacao dos testes
        self.driver.quit() # encerra / destroi o objeto do Selenium Webdriver da memoria

    def test_selecionar_produto(self):        # método de teste
        self.driver.get(self.url)                     # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user") # escreve no campo user-name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce") # escreve a senha