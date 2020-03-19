from readPDFSSCOVID19Mx import PDFCOVIDtoJSON
from downloadPDFCOVID19Mx import downloadPDFCOVID19Mx
import csv

URL_COVID_MX = downloadPDFCOVID19Mx()
temp_data = PDFCOVIDtoJSON(URL_COVID_MX)
print(temp_data)