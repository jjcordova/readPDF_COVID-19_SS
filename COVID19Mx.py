from readPDFSSCOVID19Mx import PDFCOVIDtoList, PDFCOVIDtoList  
from downloadPDFCOVID19Mx import downloadPDFCOVID19Mx
import csv

URL_COVID_MX = downloadPDFCOVID19Mx()
temp_data = PDFCOVIDtoList(URL_COVID_MX)
with open('COVID19Mx.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in range (0,(len(temp_data))):
        wr.writerow(temp_data[i])