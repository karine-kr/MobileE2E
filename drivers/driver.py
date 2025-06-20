from appium import webdriver
from appium.options.android import UiAutomator2Options

class Driver:
   driver = None
   @classmethod
   def iniciar_driver(cls):
       if cls.driver is None:
           options = UiAutomator2Options()
           options.set_capability("platformName", "Android")
           options.set_capability("deviceName", "Android Emulator")
           options.set_capability("appPackage", "com.android.settings")
           options.set_capability("appActivity", ".Settings")
           options.set_capability("automationName", "UiAutomator2")
           options.set_capability("noReset", True)
           cls.driver = webdriver.Remote(
               command_executor="http://localhost:4723/wd/hub",
               options=options
           )
       return cls.driver
   @classmethod
   def finalizar_driver(cls):
       if cls.driver:
           cls.driver.quit()
           cls.driver = None