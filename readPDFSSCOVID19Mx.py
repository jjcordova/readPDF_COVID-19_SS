import pdftotext
import json
import re
import csv
from urllib.request import urlopen

def buildArrayCOVID(LISTA_COVID):
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
    f = urlopen(URL)
    pdf = pdftotext.PDF(f)
    text_data= pdf[0].split('\n')
    temp_data = []
    temp_data.append(buildArrayCOVID([ s.lstrip() for s in text_data[8].split() if s !='']))
    for i in range(9,53):
        temp_data.append(buildArrayCOVID([ s.lstrip() for s in text_data[i].split() if s !='']))
    for j in range(1,len(pdf)-1):
        text_data= pdf[j].split('\n')
        for i in range(0, len(text_data)):
            temp_data.append(buildArrayCOVID([ s.lstrip() for s in text_data[i].split() if s !='']))
    return temp_data


def PDFCOVIDtoJSON(URL):
    f = urlopen(URL)
    pdf = pdftotext.PDF(f)
    text_data= pdf[0].split('\n')
    temp_data = [ s.lstrip() for s in text_data[8].split() if s !='']
    temp_data = buildDicCOVID(temp_data)
    JSON_COVID_19_Mx = {"COVID_19_MX":[temp_data]} 

    for i in range(9,53):
        temp_data = [ s.lstrip() for s in text_data[i].split() if s !='']
        JSON_COVID_19_Mx['COVID_19_MX'].append(buildArrayCOVID(temp_data))

    for j in range(1,len(pdf)-1):
        text_data= pdf[j].split('\n')
        for i in range(0, len(text_data)):
            temp_data = [ s.lstrip() for s in text_data[i].split() if s !='']
            JSON_COVID_19_Mx['COVID_19_MX'].append(buildArrayCOVID(temp_data))

    return json.dumps(JSON_COVID_19_Mx).encode('utf8')   