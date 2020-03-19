# Archivo: readPDFSSCOVID19Mx.py
# Autor: Juan Jose Cordova
# email: chechino@gmail.com
# twitter: @che_chino
# Fecha: 17/03/2020
# Descripción: Este programa tiene las funciones necesarias para transcribir el reporte de casos positivos de COVID19 que reporta la secretaria de salud
# el archivo PDF del reporte se transforma en un archivo JSO y en un archivo CSV

import pdftotext
import json
import re
import csv
from urllib.request import urlopen

def buildArrayCOVID(LISTA_COVID):
    '''Recibe un renglon del archivo PDF y lo separa en las columnas que requerimos
    | NoCaso | Estado | Sexo | Edad | Fecha de Diagnostico | Método de Identificación | Procedencia | Fecha de Llegada a México |
    la función regresa un arreglo'''

    CASO = LISTA_COVID[0]
    FECHA_LL = LISTA_COVID[-1]
    ESTADO = LISTA_COVID[1]    
    SEXO =  LISTA_COVID[2] 
    EDAD =  LISTA_COVID[3] 
    FECHA = LISTA_COVID[4]
    IDENTI =  LISTA_COVID[5]    
    PROCEDENCIA =LISTA_COVID[-2]
    if len(LISTA_COVID) == 8:
        ESTADO = LISTA_COVID[1]
        SEXO = LISTA_COVID[2]
        EDAD = LISTA_COVID[3]
        FECHA = LISTA_COVID[4]
        IDENTI = LISTA_COVID[5]  
        PROCEDENCIA = LISTA_COVID[6]
    elif LISTA_COVID[1]=='CIUDAD' or LISTA_COVID[1]=='SAN':
        ESTADO = "{0} {1} {2}".format(LISTA_COVID[1],LISTA_COVID[2],LISTA_COVID[3])
        SEXO = LISTA_COVID[4]
        EDAD = LISTA_COVID[5]
        FECHA = LISTA_COVID[6]
        IDENTI = LISTA_COVID[7]
    elif LISTA_COVID[1]=='QUINTANA' or LISTA_COVID[1]=='NUEVO':
        ESTADO = "{0} {1}".format(LISTA_COVID[1],LISTA_COVID[2])    
        SEXO = LISTA_COVID[3]
        EDAD = LISTA_COVID[4]
        FECHA = LISTA_COVID[5]
        IDENTI = LISTA_COVID[6]    
    elif LISTA_COVID[1]=='BAJA' and LISTA_COVID[3]=='SUR':
        ESTADO = "{0} {1} {2}".format(LISTA_COVID[1],LISTA_COVID[2],LISTA_COVID[3])    
        SEXO = LISTA_COVID[4]
        EDAD = LISTA_COVID[5]
        FECHA = LISTA_COVID[6]
        IDENTI = LISTA_COVID[7]   
    elif LISTA_COVID[1]=='BAJA' and LISTA_COVID[3]!='SUR':
        ESTADO = "{0} {1}".format(LISTA_COVID[1],LISTA_COVID[2])    
        SEXO = LISTA_COVID[3]
        EDAD = LISTA_COVID[4]
        FECHA = LISTA_COVID[5]
        IDENTI = LISTA_COVID[6]         
    elif LISTA_COVID[-2] =='Unidos' or LISTA_COVID[-2] =='Unido' or LISTA_COVID[-2]=='Zelanda':
        PROCEDENCIA = "{0} {1}".format(LISTA_COVID[-3],LISTA_COVID[-2])   
    file_json = [CASO,ESTADO,SEXO,EDAD,FECHA,IDENTI,PROCEDENCIA,FECHA_LL.strip(' \r')]
    return file_json


def buildDicCOVID(LISTA_COVID):
    '''Recibe un renglon del archivo PDF y lo separa en las columnas que requerimos
    | NoCaso | Estado | Sexo | Edad | Fecha de Diagnostico | Método de Identificación | Procedencia | Fecha de Llegada a México |
    la función regresa un diccionario'''    
    CASO = LISTA_COVID[0]
    FECHA_LL = LISTA_COVID[-1]
    ESTADO = LISTA_COVID[1]    
    SEXO =  LISTA_COVID[2] 
    EDAD =  LISTA_COVID[3] 
    FECHA = LISTA_COVID[4]
    IDENTI =  LISTA_COVID[5]    
    PROCEDENCIA =LISTA_COVID[-2]
    if len(LISTA_COVID) == 8:
        ESTADO = LISTA_COVID[1]
        SEXO = LISTA_COVID[2]
        EDAD = LISTA_COVID[3]
        FECHA = LISTA_COVID[4]
        IDENTI = LISTA_COVID[5]  
        PROCEDENCIA = LISTA_COVID[6]
    elif LISTA_COVID[1]=='CIUDAD' or LISTA_COVID[1]=='SAN':
        ESTADO = "{0} {1} {2}".format(LISTA_COVID[1],LISTA_COVID[2],LISTA_COVID[3])
        SEXO = LISTA_COVID[4]
        EDAD = LISTA_COVID[5]
        FECHA = LISTA_COVID[6]
        IDENTI = LISTA_COVID[7]
    elif LISTA_COVID[1]=='QUINTANA' or LISTA_COVID[1]=='NUEVO':
        ESTADO = "{0} {1}".format(LISTA_COVID[1],LISTA_COVID[2])    
        SEXO = LISTA_COVID[3]
        EDAD = LISTA_COVID[4]
        FECHA = LISTA_COVID[5]
        IDENTI = LISTA_COVID[6]    
    elif LISTA_COVID[1]=='BAJA' and LISTA_COVID[3]=='SUR':
        ESTADO = "{0} {1} {2}".format(LISTA_COVID[1],LISTA_COVID[2],LISTA_COVID[3])    
        SEXO = LISTA_COVID[4]
        EDAD = LISTA_COVID[5]
        FECHA = LISTA_COVID[6]
        IDENTI = LISTA_COVID[7]   
    elif LISTA_COVID[1]=='BAJA' and LISTA_COVID[3]!='SUR':
        ESTADO = "{0} {1}".format(LISTA_COVID[1],LISTA_COVID[2])    
        SEXO = LISTA_COVID[3]
        EDAD = LISTA_COVID[4]
        FECHA = LISTA_COVID[5]
        IDENTI = LISTA_COVID[6]         
    elif LISTA_COVID[-2] =='Unidos' or LISTA_COVID[-2] =='Unido' or LISTA_COVID[-2]=='Zelanda':
        PROCEDENCIA = "{0} {1}".format(LISTA_COVID[-3],LISTA_COVID[-2])   
    file_json = {'NCaso':CASO,
                'Estado':ESTADO,
                'Sexo':SEXO,
                'Edad':EDAD,
                'FechaIniSintomas':FECHA,
                'Identificacion':IDENTI,
                 'Procedencia':PROCEDENCIA,
                 'FechaLlegadaMexico':FECHA_LL.strip(' \r')
                } 
    return file_json


def PDFCOVIDtoList(URL):
    '''Recibe el archivo PDF con el reporte positivo de enfermos de COVID19 y 
    regresa una arreglo de listas'''
    pdf = pdftotext.PDF(URL)
    k=len(pdf)
    for j in range(0,k):
        text_data= pdf[j].split('\n')
        if j==0:            
            temp_data = []
            for i in range(6,51):
                temp_data.append(buildArrayCOVID([ s.lstrip() for s in text_data[i].split() if s !='']))
        elif j==1:
            for l in range(0,53):
                temp_data.append(buildArrayCOVID([ s.lstrip() for s in text_data[l].split() if s !='']))
        elif j==2:
            for l in range(0,18):
                temp_data.append(buildArrayCOVID([ s.lstrip() for s in text_data[l].split() if s !='']))                
    return temp_data

def PDFCOVIDtoJSON(URL):
    '''Recibe el archivo PDF con el reporte positivo de enfermos de COVID19 y 
    regresa una objeto JSON'''    
    pdf = pdftotext.PDF(URL)
    text_data= pdf[0].split('\n')
    temp_data = [ s.lstrip() for s in text_data[6].split() if s !='']
    temp_data = buildDicCOVID(temp_data)
    JSON_COVID_19_Mx = {"COVID_19_MX":[temp_data]} 

    for i in range(7,52):
        temp_data = [ s.lstrip() for s in text_data[i].split() if s !='']
        JSON_COVID_19_Mx['COVID_19_MX'].append(buildArrayCOVID(temp_data))

    for j in range(1,len(pdf)-1):
        text_data= pdf[j].split('\n')
        for i in range(0, len(text_data)):
            temp_data = [ s.lstrip() for s in text_data[i].split() if s !='']
            JSON_COVID_19_Mx['COVID_19_MX'].append(buildArrayCOVID(temp_data))

    return json.dumps(JSON_COVID_19_Mx).encode('utf8')   