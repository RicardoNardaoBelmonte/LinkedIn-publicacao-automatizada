from bot import iniciar_driver, fazer_login, criar_publi

email = 'seu_email@example.com'
senha = 'sua_senha'
texto_publicacao = 'Este é um exemplo de publicação no LinkedIn usando Selenium!'

# Iniciar o driver
driver = iniciar_driver()

# Fazer login
driver = fazer_login(driver, email, senha)

# Criar publicação
criar_publi(driver, texto_publicacao)