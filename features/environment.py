from drivers.driver import Driver

def before_all(context):
   context.driver = Driver.iniciar_driver()
   
def after_all(context):
   Driver.finalizar_driver()