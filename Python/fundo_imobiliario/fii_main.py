# Importar as bibliotecas necessarias 
from tokenize import String
import requests
from bs4 import BeautifulSoup
from datetime import date
import webbrowser
import os

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

fii = input("Digite o Fundo Imobiliário: ")
url = "https://fiis.com.br/" + fii + "/"

retorno = requests.get(url, headers = headers)

soup = BeautifulSoup(retorno.content, 'html5lib')

#####################
# Data Hoje
data_atual = date.today()
data_format = '{} / {} / {}'.format(data_atual.day, data_atual.month, data_atual.year)

# Nome do FII
fundName = soup.find(id="fund-ticker").get_text()

fundInformation = soup.find(id="informations--indexes").get_text().split("\n")
fundInformation = list(filter(None, fundInformation))
# Dividend Yield
fundDividend = fundInformation[0]
# Último Rendimento
fundRend = fundInformation[2]
# Valor Patrimonial por Cota
fundValor = fundInformation[6]


fundType = soup.find(id="informations--basic").get_text().split("\n")
fundType = list(filter(None, fundType))
# Tipo do FII
fundType = fundType[3]

valorCota = float(fundRend[2:int(len(fundRend))].replace(',', '.'))


cota10 = str(round(valorCota * 10, 2)).replace('.', ',')
cota50 = str(round(valorCota * 50, 2)).replace('.', ',')
cota75 = str(round(valorCota * 75, 2)).replace('.', ',')
cota100 = str(round(valorCota * 100, 2)).replace('.', ',')
cota250 = str(round(valorCota * 250, 2)).replace('.', ',')
cota500 = str(round(valorCota * 500, 2)).replace('.', ',')
cota1000 = str(round(valorCota * 1000, 2)).replace('.', ',')


# Abre o aquivo HTML
arq = open("index.html", "w+")


# Página HTML

conteudo = ["<!DOCTYPE html>", \
"<html>", \

"<head>", \
"    <meta charset='utf-8'>", \
"    <meta name='viewport' content='width=device-width, initial-scale=1.0, shrink-to-fit=no'>", \
"    <title>Dash - FII</title>", \
"    <link rel='stylesheet' href='assets/bootstrap/css/bootstrap.min.css'>", \
"    <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Alfa+Slab+One'>", \
"    <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Asset'>", \
"    <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Bangers'>", \
"    <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Barrio'>", \
"    <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Bowlby+One'>", \
"    <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Bungee+Inline'>", \
"    <link rel='stylesheet' href='assets/fonts/fontawesome-all.min.css'>", \
"    <link rel='stylesheet' href='assets/fonts/line-awesome.min.css'>", \
"    <link rel='stylesheet' href='assets/css/styles.css'>", \
"</head>", \
"", \
"<body style='box-shadow: inset 0px 0px 12px 1px;'>", \
"    <div id='main'>", \
"        <div id='data_base' style='width: 154px;color: rgb(33,143,252);margin-left: 11px;'><span style='font-size: 12px;padding: 0px;'>Data Base:&nbsp;</span><input class='form-control-plaintext float-right text-right' type='text' value='" + data_format + "' readonly='' style='font-size: 12px;width: 91px;padding: 0px;padding-top: 4px;'></div>", \
"    </div>", \
"    <div id='cota-nome'>", \
"        <h1 class='text-uppercase text-center' style='padding: 5px;color: rgb(30,144,255);font-family: Bangers, cursive;font-size: 70px;text-shadow: 2px -1px 3px rgb(0,0,0);'>- " + fundName + " -</h1>", \
"    </div>", \
"    <div>", \
"        <div class='container'>", \
"            <div class='row'>", \
"                <div class='col-md-6' style='padding: 10px;'>", \
"                    <div id='valor_cota' style='color: #1E90FF;'><i class='fas fa-dollar-sign valor_cota' style='width: 24px;font-size: 18px;padding: 3px;color: #2E8B57;border-style: none;text-shadow: 2px -1px 1px #556B2F;'></i><span class='text-uppercase text-left valor_cota' for='valor_cota' style='color: rgb(30,144,255);'>VALOR DA COTA:</span>", \
"                        <input", \
"                            class='form-control-plaintext valor_cota' type='text' value='" + fundValor + "' readonly='' style='width: auto;padding-top: 0px;height: auto;font-size: 25px;'></div>", \
"                    <div id='rendimento_mes' style='color: #1E90FF;'><i class='fas fa-coins rendimento_mes' style='width: 24px;font-size: 18px;padding: 3px;color: #FFD700;text-shadow: 2px -1px 1px #b8860b;'></i><span class='text-uppercase text-left rendimento_mes' for='rendimento_mes'>rendimento do mês:</span>", \
"                        <input", \
"                            class='form-control-plaintext rendimento_mes' type='text' value='" + fundRend + "' readonly='' style='width: auto;padding-top: 0px;height: auto;font-size: 25px;'></div>", \
"                    <div id='dividend' style='color: #1E90FF;'><i class='fas fa-percent dividend' style='width: 24px;font-size: 18px;padding: 3px;text-shadow: 2px -1px 2px #000000;color: #FFFAFA;'></i><span class='text-uppercase text-left dividend' for='dividend'>dividend yield:</span><input class='form-control-plaintext dividend'", \
"                            type='text' value='" + fundDividend + "' readonly='' style='width: auto;padding-top: 0px;height: auto;font-size: 25px;'></div>", \
"                    <div id='tipo_cota' style='color: #1E90FF;'><span class='text-uppercase text-left tipo_cota' for='tipo_cota'>tipo de fii:</span><input class='form-control-plaintext text-capitalize tipo_cota' type='text' value='" + fundType + "' readonly='' style='width: auto;padding-top: 0px;height: auto;font-size: 25px;'></div>", \
"                </div>", \
"                <div class='col-md-6' style='padding: 10px;'>", \
"                    <div id='rentimento_cota'>", \
"                        <h4 class='text-uppercase font-weight-bold' style='color: rgb(33,143,252);'>rendimento do ativo se você tiver:</h4>", \
"                        <div id='cota_10'><span class='text-uppercase text-left font-weight-bold' style='color: rgb(33,143,252);margin: 0px;padding: 0px;'><i class='la la-money' style='padding: 3px;color: #2E8B57;text-shadow: 1px -1px 1px #556B2F;font-size: 33px;margin-top: 0px;padding-top: 0px;'></i>&nbsp; &nbsp;10 cotas</span>", \
"                            <input", \
"                                class='form-control-plaintext float-right text-right' type='text' value='R$ " + cota10 + "' readonly='' style='width: 150px;padding: 0px;margin-top: 10px;'></div>", \
"                        <div id='cota_-6'><span class='text-uppercase text-left font-weight-bold' style='color: rgb(33,143,252);margin: 0px;padding: 0px;'><i class='la la-money' style='padding: 3px;color: #2E8B57;text-shadow: 1px -1px 1px #556B2F;font-size: 33px;margin-top: 0px;padding-top: 0px;'></i>&nbsp; &nbsp;50 cotas</span>", \
"                            <input", \
"                                class='form-control-plaintext float-right text-right' type='text' value='R$ " + cota50 + "' readonly='' style='width: 150px;padding: 0px;margin-top: 10px;'></div>", \
"                        <div id='cota_-5'><span class='text-uppercase text-left font-weight-bold' style='color: rgb(33,143,252);margin: 0px;padding: 0px;'><i class='la la-money' style='padding: 3px;color: #2E8B57;text-shadow: 1px -1px 1px #556B2F;font-size: 33px;margin-top: 0px;padding-top: 0px;'></i>&nbsp; &nbsp;75 cotas</span>", \
"                            <input", \
"                                class='form-control-plaintext float-right text-right' type='text' value='R$ " + cota75 + "' readonly='' style='width: 150px;padding: 0px;margin-top: 10px;'></div>", \
"                        <div id='cota_-4'><span class='text-uppercase text-left font-weight-bold' style='color: rgb(33,143,252);margin: 0px;padding: 0px;'><i class='la la-money' style='padding: 3px;color: #2E8B57;text-shadow: 1px -1px 1px #556B2F;font-size: 33px;margin-top: 0px;padding-top: 0px;'></i>&nbsp; &nbsp;100 cotas</span>", \
"                            <input", \
"                                class='form-control-plaintext float-right text-right' type='text' value='R$ " + cota100 + "' readonly='' style='width: 150px;padding: 0px;margin-top: 10px;'></div>", \
"                        <div id='cota_-3'><span class='text-uppercase text-left font-weight-bold' style='color: rgb(33,143,252);margin: 0px;padding: 0px;'><i class='la la-money' style='padding: 3px;color: #2E8B57;text-shadow: 1px -1px 1px #556B2F;font-size: 33px;margin-top: 0px;padding-top: 0px;'></i>&nbsp; &nbsp;250 cotas</span>", \
"                            <input", \
"                                class='form-control-plaintext float-right text-right' type='text' value='R$ " + cota250 + "' readonly='' style='width: 150px;padding: 0px;margin-top: 10px;'></div>", \
"                        <div id='cota_-2'><span class='text-uppercase text-left font-weight-bold' style='color: rgb(33,143,252);margin: 0px;padding: 0px;'><i class='la la-money' style='padding: 3px;color: #2E8B57;text-shadow: 1px -1px 1px #556B2F;font-size: 33px;margin-top: 0px;padding-top: 0px;'></i>&nbsp; &nbsp;500 cotas</span>", \
"                            <input", \
"                                class='form-control-plaintext float-right text-right' type='text' value='R$ " + cota500 + "' readonly='' style='width: 150px;padding: 0px;margin-top: 10px;'></div>", \
"                        <div id='cota_-1'><span class='text-uppercase text-left font-weight-bold' style='color: rgb(33,143,252);margin: 0px;padding: 0px;'><i class='la la-money' style='padding: 3px;color: #2E8B57;text-shadow: 1px -1px 1px #556B2F;font-size: 33px;margin-top: 0px;padding-top: 0px;'></i>&nbsp; &nbsp;1000 cotas</span>", \
"                            <input", \
"                                class='form-control-plaintext float-right text-right' type='text' value='R$ " + cota1000 + "' readonly='' style='width: 150px;padding: 0px;margin-top: 10px;'></div>", \
"                    </div>", \
"                </div>", \
"            </div>", \
"            <div class='row'>", \
"                <div class='col-md-12'></div>", \
"            </div>", \
"        </div>", \
"    </div>", \
"    <script src='assets/js/jquery.min.js'></script>", \
"    <script src='assets/bootstrap/js/bootstrap.min.js'></script>", \
"</body>", \

"</html>"]

for linhas in conteudo:
    arq.write(linhas)
    arq.write("\n")

arq.close()

# ENVIA O HTML PARA O SERVIDOR DE TESTES DO NGINX
os.system('scp index.html ubuntu@192.168.1.110:/home/ubuntu/nginx/www/fii-monitor')

# ABRE A PÁGINA WEB QUANDO TERMINA DE RODAR O SCRIPT
#webbrowser.open('index.html')
