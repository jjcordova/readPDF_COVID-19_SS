# Archivo: downloadPDFCOVID19Mx.py
# Autor: Juan Jose Cordova
# email: chechino@gmail.com
# twitter: @che_chino
# Fecha: 17/03/2020
# Descripción: Este programa hace scraping al portal de la secretaria de salud,
# en donde creo va a publicar las actualizaciones de la tabla de casos positivos en el 
# diagnostico de COVID19
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re

def downloadPDFCOVID19Mx():
    '''Realiza scraping del portal de la secreataria de salud
    https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449
    y busca el enlace al archivo PDF basado en la palabra 'positivo' y regresa el archivo PDF
    al que se hace referencia'''
    html = urlopen('https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449')
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('a', {'href':re.compile('^(/cms/uploads/)((?!:).)*$')})
    listGamaIFM = [image['href'] for image in images if image['href'].find('positivos') != -1]
    pdfCOVID19Mx = urlopen('https://www.gob.mx{}'.format(listGamaIFM[0]))
    return pdfCOVID19Mx