from readPDFSSCOVID19Mx import PDFCOVIDtoList, PDFCOVIDtoList  
import csv

URL_COVID_MX = "https://www.gob.mx/cms/uploads/attachment/file/541580/Tabla_casos_positivos_resultado_InDRE_2020.03.16.pdf"
temp_data = PDFCOVIDtoList(URL_COVID_MX)

with open('COVID19Mx.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in range (0,(len(temp_data)-1)):
        wr.writerow(temp_data[i])