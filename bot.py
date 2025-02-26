from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pyautogui
import pyperclip

def iniciar_driver():
    # Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
    chrome_options = Options()
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    arguments = ['--lang=pt-BR', '--window-size=1000,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)
    # Navegar até um site
    return driver

def fazer_login(driver, email, senha):
    driver.get('https://www.linkedin.com/checkpoint/lg/login?rmDisableAutoLogin=true&midToken=AQGjF7NDb4_hlQ')
    sleep(2)
    driver.find_element(By.NAME,'session_key').send_keys(email)
    sleep(1)
    driver.find_element(By.NAME,'session_password').send_keys(senha)
    sleep(1)
    botao_login = driver.find_element(By.XPATH, "//button[@data-litms-control-urn='login-submit']")
    botao_login.click()
    sleep(60)#Esta pausa é para que caso ele peça para você confirmar o login no celular, você tenha tempo de fazer isso
    print('Login feito com sucesso')
    return driver

def digitar_como_humano(texto, atraso_min=0.05, atraso_max=0.3):
    for caractere in texto:
        if caractere == '\n':
            pyautogui.press('enter')
        elif caractere == '\t':
            pyautogui.press('tab')
        elif not caractere.isascii():
            pyperclip.copy(caractere)
            pyautogui.hotkey('ctrl', 'v')
        else:
            pyautogui.typewrite(caractere)
        sleep(random.uniform(atraso_min, atraso_max))

def criar_publi(driver, texto):
    perfil = driver.find_element(By.ID, 'ember16')
    perfil.click()
    sleep(2)
    perfil.send_keys(Keys.TAB , Keys.ENTER)
    sleep(5)
    driver.execute_script("window.scrollTo(0, 1000);")
    sleep(4)
    criar_publi = driver.find_element(By.XPATH, "//a[@id='navigation-create-post-Criar-publica-o']")
    criar_publi.click()
    sleep(4)
    digitar_como_humano(texto)
    sleep(2)
    resposta = input('Deseja adicionar fotos? Se sim, digite ok e pressione enter caso contrário pressione enter: ')
    if resposta == 'ok':
        hover_element = driver.find_element(By.CSS_SELECTOR, "span.artdeco-hoverable-trigger")
        actions = ActionChains(driver)
        actions.move_to_element(hover_element).perform()
        botao_upload_arquivo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Adicione uma foto"].share-promoted-detour-button'))
            )
        botao_upload_arquivo.click()
        input('Escolha a foto e clique em abrir, depois digite terminei e aperte enter: ')
        botao_avancar = driver.find_element(By.XPATH, '//button[@type="button" and contains(., "Avançar")]')
        botao_avancar.click()
        sleep(5)

    publicar = driver.find_element(By.XPATH, "//button[span[text()='Publicar']]")
    publicar.click()
    sleep(5)
    driver.close()


