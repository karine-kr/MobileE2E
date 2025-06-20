from behave import given, when, then
from pages.photos_page import PhotosPage
import logging

@given("que estou na tela de configurações do app Fotos")
def step_dado_fotos(context):
    context.driver.terminate_app("com.android.settings")
    context.driver.activate_app("com.android.settings")
    context.page = PhotosPage(context.driver)
    logging.info("Na tela de configurações do app Fotos")

@when("busco Fotos dentro dos Aplicativos")
def step_buscar_fotos(context):
    context.page.abrir_aplicativos()
    context.page.buscar_app()
    context.page.buscar_fotos()
    logging.info("Busca realizada pelo app: fotos")

@when("navego para Permissões > Localização no Fotos")
def step_navegar_permissoes_fotos(context):
    context.page.clicar_permissoes()
    context.page.clicar_localizacao()

@when('permito a localização como "{tipo_permissao}" no Fotos')
def step_permitir_localizacao_fotos(context, tipo_permissao):
    if tipo_permissao == "permitir durante o uso do app":
        context.page.selecionar_permissao_uso()
    else:
       raise Exception(f"Permissão inválida: {tipo_permissao}")

@when('nego a permissão como "{tipo_permissao}" no Fotos')
def step_negar_localizacao_fotos(context, tipo_permissao):
    if tipo_permissao == "não permitir":
        context.page.selecionar_permissao_nao_permitir()
    else:
        raise Exception(f"Permissão inválida: {tipo_permissao}")

@then('a permissão "{tipo_permissao}" deve estar marcada no Fotos')
def step_validar_permissao_fotos(context, tipo_permissao):
    assert context.page.verificar_permissao_selecionada(tipo_permissao), f"Permissão '{tipo_permissao}' não marcada"
    logging.info(f"Permissão marcada: {tipo_permissao}")