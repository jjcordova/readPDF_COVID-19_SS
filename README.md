# readPDF_COVID-19_SS

Con Scraping se lee el archivo PDF que reporta la Secretaria de Salud de México en el portal:

https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449

Y transformamos el archivo PDF salida JSON o un archivo CSV

El programa COVID19Mx.py muestra un ejemplo de como usar: 

``` python
URL_COVID_MX = downloadPDFCOVID19Mx()
temp_data = PDFCOVIDtoList(URL_COVID_MX)
with open('COVID19Mx.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in range (0,(len(temp_data))):    
        wr.writerow(temp_data[i])      
```

Se obtiene un archivo con las columnas

| NoCaso | Estado | Sexo | Edad | Fecha de Diagnóstico | Método de Identificación | Procedencia | Fecha de Llegada a México |
|--------|--------|------|------|----------------------|--------------------------|-------------|---------------------------|

Aquí pueden descargar el archivo [COVID19Mx.csv](https://github.com/jjcordova/readPDF_COVID-19_SS/blob/master/COVID19Mx.csv)
