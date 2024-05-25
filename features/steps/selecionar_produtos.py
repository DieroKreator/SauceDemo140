# 1  - Bibliotecas / Imports
import time
from behave import given, when, then # type: ignore
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
@given(u'que entro o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()              # instanciar o objeto do Selenium webDriver especializado para o Chrome
    context.driver.maximize_window()                 # maximizar a janela do navegador
    context.driver.implicitly_wait(10)               # esperar até 1- segundos por qualquer elemnto
    # Passo em si
    context.driver.get("https://www.saucedemo.com")  # abrir o navegador no endereco do site alvo

# Preencher com usuario e senha   
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
@given(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()         # clicar no botão login

@given(u'adiciono um produto ao carrinho')
def step_impl(context):
    # valido pagina Home
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    # valido o producto
    assert context.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name").text == "Sauce Labs Backpack"
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"

@when(u'clico no icone do carrinho')
@given(u'clico no icone do carrinho')
def step_impl(context):
    # valido a quantidade no medallion do carrinho
    assert context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "1"
    context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()

# Preencher com usuario em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    # não preenche o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()         # clicar no botão login

# Preencher com usuario mas deixar a senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):    
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuario
    # não preenche a senha
    context.driver.find_element(By.ID, "login-button").click()         # clicar no botão login

# Clica no botão de login sem ter preenchido o usuario e a senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):    
    # não preenche o usuario
    # não preenche a senha
    context.driver.find_element(By.ID, "login-button").click()         # clicar no botão login

# Preencher com usuario e senha através da decisão (IF)  
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuario
        # se o usuario estiver em <branco> não há ação de preenchimento
    
    if senha != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
        # se a senha estiver em <branco> não há ação de preenchimento

    context.driver.find_element(By.ID, "login-button").click()         # clicar no botão login

@when(u'clico no botao para remover o item do carrinho')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()

@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    # time.sleep(2)  # espera por 2 segundos - remover depois = alfinete

    # teardown / encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    # teardown / encerramento
    context.driver.quit()

# Verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    # teardown / encerramento
    context.driver.quit()

@then(u'o produto {produto} está no carrinho')
def step_impl(context, produto):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"
    assert context.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == produto
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99"
    # time.sleep(3)

@then(u'o item é removido')
def step_imp(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".removed_cart_item")

    # teardown / encerramento
    context.driver.quit()