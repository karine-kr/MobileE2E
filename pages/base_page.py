import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 15)
   
   def clicar(self, locator):
       logging.info(f"Clicando no elemento: {locator}")
       elem = self.wait.until(EC.element_to_be_clickable(locator))
       elem.click()
   
   def escrever(self, locator, texto):
       logging.info(f"Escrevendo texto '{texto}' no elemento: {locator}")
       elem = self.wait.until(EC.visibility_of_element_located(locator))
       elem.clear()
       elem.send_keys(texto)
   
   def obter_texto(self, locator):
       elem = self.wait.until(EC.visibility_of_element_located(locator))
       texto = elem.text
       logging.info(f"Texto obtido do elemento {locator}: {texto}")
       return texto
  
   def esta_selecionado(self, locator):
       elem = self.wait.until(EC.visibility_of_element_located(locator))
       selecionado = elem.get_attribute("checked") == "true"
       logging.info(f"Elemento {locator} selecionado? {selecionado}")
       return selecionado