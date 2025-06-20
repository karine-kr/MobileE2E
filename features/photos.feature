# language: pt
Funcionalidade: Configurações de localização no app Fotos
Cenário: Negar localização no Fotos
 Dado que estou na tela de configurações do app Fotos
 Quando busco Fotos dentro dos Aplicativos
 E navego para Permissões > Localização no Fotos
 E nego a permissão como "não permitir" no Fotos
 Então a permissão "não permitir" deve estar marcada no Fotos

 Cenário: Permitir localização durante uso no Fotos
 Dado que estou na tela de configurações do app Fotos
 Quando busco Fotos dentro dos Aplicativos
 E navego para Permissões > Localização no Fotos
 E permito a localização como "permitir durante o uso do app" no Fotos
 Então a permissão "permitir durante o uso do app" deve estar marcada no Fotos