# readPDF_COVID-19_SS
Lee el archivo PDF que reporta la Secretaria de Salud de México y lo transforma en una salida JSON o un archivo CSV

ejemplo: 

URL_COVID_MX = "https://www.gob.mx/cms/uploads/attachment/file/541580/Tabla_casos_positivos_resultado_InDRE_2020.03.16.pdf"
dataArray = PDFCOVIDtoList(URL_COVID_MX)
dataJSON = PDFCOVIDtoJSON(URL_COVID_MX)

https://www.gob.mx/salud/documentos/nuevo-coronavirus-2019-ncov-comunicado-tecnico-diario

La dirección del documento es aún un dato duro.

https://www.gob.mx/cms/uploads/attachment/file/541579/Tabla_casos_sospechosos_COVID-19_2020.03.16.pdf
