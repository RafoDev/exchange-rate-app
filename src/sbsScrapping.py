import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx")

def sbsScrapping(listaMonedas):
  if(url.status_code == 200):
    html = BeautifulSoup(url.text, 'html.parser')
    tabla = html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
    tabla = BeautifulSoup(str(tabla), 'html.parser')
    filasMonedas = tabla.find_all('td')
    for fila in range(0, len(filasMonedas), 3):
      dicMoneda = {
        'currency':filasMonedas[fila].get_text(),
        'buy':filasMonedas[fila + 1].get_text(),
        'sell':filasMonedas[fila + 2].get_text(),
      }
      listaMonedas.append(dicMoneda)
  else:
    print("error" + str(url.status_code))
  return listaMonedas

