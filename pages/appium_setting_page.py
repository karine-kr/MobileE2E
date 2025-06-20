from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class AppiumSettingsPage(BasePage):
   APLICATIVOS_OPCAO = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Pesquisar nas Configurações']")
   BUSCAR_CAMPO = (AppiumBy.ID, "com.android.settings.intelligence:id/search_src_text")
   RESULTADO_BUSCA = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Aplicativos')]")
   PESQUISA_APP = (AppiumBy.ID, "com.android.settings:id/search_app_list_menu")
   BUSCA_FOTOS = (AppiumBy.ID, "com.android.settings:id/search_src_text")
   RESULTADO_FOTOS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Appium Settings')]")
   PERMISSOES_OPCAO = (AppiumBy.XPATH, "//android.widget.TextView[@text='Permissões']")
   LOCALIZACAO_OPCAO = (AppiumBy.XPATH, "//android.widget.TextView[@text='Localização']")
   PERMITIR_TEMPO_TODO = (AppiumBy.XPATH, "//android.widget.RadioButton[@text='Permitir o tempo todo']")
   NAO_PERMITIR = (AppiumBy.XPATH, "//android.widget.RadioButton[@text='Não permitir']")

   def abrir_aplicativos(self):
       self.clicar(self.APLICATIVOS_OPCAO)

   def buscar_app(self):
       self.clicar(self.BUSCAR_CAMPO)
       self.escrever(self.BUSCAR_CAMPO, "Aplicativos")
       self.clicar(self.RESULTADO_BUSCA)
 
   def buscar_appium(self):
       self.clicar(self.PESQUISA_APP)
       self.escrever(self.BUSCA_FOTOS, "Appium Settings")
       self.clicar(self.RESULTADO_FOTOS)

   def clicar_permissoes(self):
       self.clicar(self.PERMISSOES_OPCAO)
   
   def clicar_localizacao(self):
       self.clicar(self.LOCALIZACAO_OPCAO)
   
   def selecionar_permissao_tempo_todo(self):
       self.clicar(self.PERMITIR_TEMPO_TODO)
   
   def selecionar_permissao_nao_permitir(self):
       self.clicar(self.NAO_PERMITIR)
   
   def verificar_permissao_selecionada(self, tipo_permissao: str) -> bool:
       if tipo_permissao == "permitir o tempo todo":
           return self.esta_selecionado(self.PERMITIR_TEMPO_TODO)
       elif tipo_permissao == "não permitir":
           return self.esta_selecionado(self.NAO_PERMITIR)
       else:
           raise ValueError("Tipo de permissão inválida.")