# readPDF_COVID-19_SS

Con Scraping se lee el archivo PDF que reporta la Secretaria de Salud de México en el portal:

https://www.gob.mx/salud/documentos/nuevo-coronavirus-2019-ncov-comunicado-tecnico-diario

Y transformamos el archivo PDF salida JSON o un archivo CSV

ejemplo: 

URL_COVID_MX = downloadPDFCOVID19Mx()

temp_data = PDFCOVIDtoList(URL_COVID_MX)

