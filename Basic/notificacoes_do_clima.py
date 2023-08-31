import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

notifica = ToastNotifier()

def getdata(url) :
    requisicao = requests.get(url)

    return requisicao.text

htmlData = getdata("https://weather.com/en-IN/weather/today/l/9afbc4ea05a1c6aeba26d939e4bac141d847468914af8c82d2fbae79f13ebf21")

soup = BeautifulSoup(htmlData, 'html.parser')

clima_atual = soup.find_all("span",
                           class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")

chanceDeChuva = soup.find_all("div", 
                             class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

clima = (str(clima_atual))
chanceChuva = str(chanceDeChuva)

resultado = "clima atual" + clima[128:-9] + " com previsão de chuva" + "\n" + chanceChuva[131:-14]

notifica.show_toast("Atualização do clima", resultado, duration = 10)