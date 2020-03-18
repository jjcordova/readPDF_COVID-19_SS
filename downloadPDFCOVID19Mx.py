from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re

def downloadPDFCOVID19Mx():
    html = urlopen('https://www.gob.mx/salud/documentos/nuevo-coronavirus-2019-ncov-comunicado-tecnico-diario')
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('a', {'href':re.compile('^(/cms/uploads/)((?!:).)*$')})
    listGamaIFM = [image['href'] for image in images if image['href'].find('positivos') != -1]
    pdfCOVID19Mx = urlopen('https://www.gob.mx{}'.format(listGamaIFM[0]))
    return pdfCOVID19Mx