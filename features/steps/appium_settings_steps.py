from behave import given, when, then
from pages.appium_setting_page import AppiumSettingsPage
import logging

@given("que estou na tela de configurações do app Appium Settings")
def step_dado_appium_settings(context):
    context.driver.terminate_app("com.android.settings")
    context.driver.activate_app("com.android.settings")
    context.page = AppiumSettingsPage(context.driver)
    logging.info("Na tela de configurações do Appium Settings")

@when("busco Appium Settings dentro dos Aplicativos")
def step_buscar_appium_settings(context):   
    context.page.abrir_aplicativos()
    context.page.buscar_app()
    context.page.buscar_appium()
    logging.info("Busca realizada pelo app: Appium Settings")

@when("navego para Permissões > Localização no Appium Settings")
def step_navegar_permissoes_appium(context):
   context.page.clicar_permissoes()
   context.page.clicar_localizacao()

@when('permito a localização como "{tipo_permissao}" no Appium Settings')
def step_permitir_localizacao_appium(context, tipo_permissao):
   if tipo_permissao == "permitir o tempo todo":
       context.page.selecionar_permissao_tempo_todo()
   else:
       raise Exception(f"Permissão inválida: {tipo_permissao}")
   
@when('nego a permissão como "{tipo_permissao}" no Appium Settings')
def step_negar_localizacao_appium(context, tipo_permissao):
   if tipo_permissao == "não permitir":
       context.page.selecionar_permissao_nao_permitir()
   else:
       raise Exception(f"Permissão inválida: {tipo_permissao}")
   
@then('a permissão "{tipo_permissao}" deve estar marcada no Appium Settings')
def step_validar_permissao_appium(context, tipo_permissao):
   assert context.page.verificar_permissao_selecionada(tipo_permissao), f"Permissão '{tipo_permissao}' não marcada"
   logging.info(f"Permissão marcada: {tipo_permissao}")