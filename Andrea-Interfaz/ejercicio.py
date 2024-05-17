from urllib.request import urlopen 
from bs4 import BeautifulSoup


def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read()) 
   
def leeLinea(linea):
   lista = []
   for dato in linea.find_all('td'):
      lista.append(dato.get_text())
   return lista
   
def leeTabla(tabla):
    filas = []
    for fila in tabla.find_all('tr'):
       filas.append(leeLinea(fila))
    return filas
    
    
miDir = "https://es.wikipedia.org/wiki/Honolulu"
laSopa = bajar(miDir)
lasTablas = laSopa.find_all("table")
#
tablaClima = lasTablas[2]
tabla = leeTabla(tablaClima)
print (tabla)
#print(tabla[1])
lista_dicc=[{"nom":"Salta","ptabla":1,"tempmax":1, "tempmmin":4},
            {"nom":"Kasgar","ptabla":1,"tempmax":2, "tempmmin":3},
            {"nom":"Honolulu","ptabla":1,"tempmax":2, "tempmmin":3}]