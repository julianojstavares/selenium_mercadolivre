from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
"""
Para executar o teste utilize o botão play no Visual Studio caso a extensão
Code Runner estiver instalada ou digite no terminal o comando
"python nome_do_arquivo.py" depois de ativar o ambiente virtual no windows
com o comando venv\Scripts\activate
"""


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessar(self, site):
        self.chrome.get(site)

    def buscar(self, texto):
        try:
            busca = self.chrome.find_element_by_css_selector(
                '.nav-search-input')
            busca.click()
            busca.send_keys(texto)
            busca.send_keys(Keys.RETURN)
        except Exception as e:
            print('Erro ao buscar:', e)

    def finalPagina(self):
        try:
            self.chrome.execute_script(
                "window.scrollTo(0,document.body.scrollHeight)")
        except Exception as e:
            print('Erro ao rolar página:', e)

    def clicar_ultimo(self):
        try:
            item = self.chrome.find_element_by_xpath(
                '/html/body/main/div/div[1]/section/ol[16]/li[3]/div')
            item.click()
        except Exception as e:
            print('Erro ao clicar no último item:', e)

    def print_preco(self):
        try:
            moeda = self.chrome.find_element_by_xpath(
                '//*[@id="root-app"]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/span/span[1]')
            preco = self.chrome.find_element_by_xpath(
                '//*[@id="root-app"]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/span/span[2]')
            print(f'Preço item = {moeda.text} {preco.text}')
        except Exception as e:
            print('Erro ao mostrar preço:', e)

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessar('https://www.mercadolivre.com.br/')
    chrome.buscar('tv 55 polegadas')
    sleep(3)
    chrome.finalPagina()
    chrome.clicar_ultimo()
    chrome.print_preco()
    chrome.sair()
