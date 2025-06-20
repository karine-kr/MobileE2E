# language: pt
 Funcionalidade: Permissões do Appium Settings
Cenário: Permitir localização durante uso no Appium Settings
 Dado que estou na tela de configurações do app Appium Settings
 Quando busco Appium Settings dentro dos Aplicativos
 E navego para Permissões > Localização no Appium Settings
 E permito a localização como "permitir o tempo todo" no Appium Settings
 Então a permissão "permitir o tempo todo" deve estar marcada no Appium Settings

Cenário: Negar localização no Appium Settings
 Dado que estou na tela de configurações do app Appium Settings
 Quando busco Appium Settings dentro dos Aplicativos
 E navego para Permissões > Localização no Appium Settings
 E nego a permissão como "não permitir" no Appium Settings
 Então a permissão "não permitir" deve estar marcada no Appium Settings