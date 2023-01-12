from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()

    pagina.goto('https://www.siepe.educacao.pe.gov.br/')
    print(1)
    pagina.fill('xpath=//*[@id="login"]','')
    print(2)
    pagina.fill('xpath=//*[@id="senha"]', '')
    print(3)
    pagina.locator('xpath=/html/body/div[1]/header/div/div[2]/form/div[1]/button/span').click()
    print(4)
    pagina.locator('xpath=/html/body/div[1]/div[1]/div/div[1]/button').click()
    print(5)
    pagina.locator('xpath=/html/body/div[1]/div[1]/div/div[1]/div/ul/li[2]/a/span').click()
    print(6)
    pagina.locator('xpath=//*[@id="divGrupos"]/ul/li[2]/a').click()
    print(7)
    pagina.locator('xpath=//*[@id="divListaModulos"]/a[2]/div').click()
    print(8)

    print(9)

    print(10)

    print(11)

    print(12)

    print(13)

    print(14)

    print(15)

    print(16)

    print(17)

    time.sleep(10000)
