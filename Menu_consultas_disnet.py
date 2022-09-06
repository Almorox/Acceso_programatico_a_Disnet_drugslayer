#!/usr/bin/env python
# coding: utf-8
#----------------------------------------------------------------------------------------
# Este código es un trabajo para la asignatura Bases de Datos del Grado de Biotecnología 
# Trabajo realizado por Lucía Almorox y Marta Garcia
#----------------------------------------------------------------------------------------

# In[1]:


from IPython.display import clear_output
from sys import exit


# In[2]:


import mysql.connector


# In[3]:
    
#Establecemos la conexión con la base de datos: disnet_drugslayer
config = {
    'user':'disnet_drugslayer_user',
    'password':'disnet_drugslayer_pwd',
    'host':'localhost',
    'db':'disnet_drugslayer',
}

#Usamos el operador ** debido al uso de parámetros múltiples
db = mysql.connector.connect(**config)
db.autocommit = True
cursor = db.cursor(buffered=True) #cursor obtiene todas las filas del servidor


# In[4]:

#---------------------------------MENU PRINCIPAL-------------------------------

def main():
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("MENÚ PRINCIPAL DE CONSULTAS\n")
    print("[1]Información general de la base de datos")
    print("[2]Información de los fármacos")
    print("[3]Información de las enfermedades")
    print("[4]Información de los efectos fenotípicos")
    print("[5]Información de las dianas\n")
    print("BORRADOS, INSERCIONES, MODIFICACIONES\n")
    print("[6]Borrados")
    print("[7]Inserciones")
    print("[8]Modificaciones")
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("[9] AYUDA")
    print("[0] EXIT")
    #Función para elegir un elemento del menú principal
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("No existe esa opción, pruebe otra vez.")
            
    if menuSelect == 1:
        menu1()
    elif menuSelect == 2: 
        menu2()
    elif menuSelect == 3:
        menu3()
    elif menuSelect == 4:
        menu4()
    elif menuSelect == 5:
        menu5()
    elif menuSelect == 6:
        menu6()
    elif menuSelect == 7:
        menu7()
    elif menuSelect == 8:
        menu8()
    elif menuSelect == 9:
        menu9()
    elif menuSelect == 0:
        f_exit()
    else:
        print("No existe esa opción, pruebe otra vez.")
        main()


# In[5]:

#---------------------------------APARTADO 1-------------------------------
#Función para hacer consultas sobre la información general de la base de datos

def menu1():
    print("----------------------------------------------")
    print("Información General de la Base de Datos")
    print("[-]Número Total")
    print("\t[1]Número de Fármacos diferentes")
    print("\t[2]Número de Enfermedades diferentes")
    print("\t[3]Número de Fenotipos diferentes")
    print("\t[4]Número de Dianas terapéuticas diferentes")
    print("[-]Primeras 10 instancias")
    print("\t[5]Fármacos")
    print("\t[6]Enfermedades")
    print("\t[7]Efectos Fenotípicos")
    print("\t[8]Dianas")
    print("[9]Regresar al menú principal")
    print("----------------------------------------------")
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("\nNo existe esa opción, pruebe otra vez.")
    print("----------------------------------------------")
    
    #1.a.i-Número de farmacos diferentes
    if menuSelect == 1:
        NumDrugs = "SELECT count(distinct drug_id) FROM drug"
        cursor.execute(NumDrugs) #variable NumDrugs pasa al cursor mediante execute
        data = cursor.fetchmany() #fetchmany() es igual a fetchmany(1)
        #lo que sería igual que fetchone() pero devolviendo la instancia en 
        #una lista (de un único elemento) que podemos indexar.
        #guardamos el resultado de la consulta en la variable 'data'.
        print("\nEl número de fármacos diferentes es: ")
        for row in data:
            print(row[0])
        volver(menu1)
    
    #1.a.ii-Número de enfermedades diferentes
    elif menuSelect == 2:
        NumDiseases = "SELECT count(distinct disease_id) FROM disease"
        cursor.execute(NumDiseases)
        data = cursor.fetchmany()
        print("\nEl número de enfermedades diferentes es: ")
        for row in data:
            print(row[0])
        volver(menu1)
        
    #1.a.iii-Número de efectos fenotípicos diferentes        
    elif menuSelect == 3:
        NumPhenoEff = "SELECT count(distinct phenotype_id) FROM\
            phenotype_effect"
        cursor.execute(NumPhenoEff)
        data = cursor.fetchmany()
        print("\nEl número de efectos fenotípicos diferentes es: ")
        for row in data:
            print(row[0])
        volver(menu1)

    #1.a.iv-Número de targets diferentes
    elif menuSelect == 4:
        NumTargets = "SELECT count(distinct target_id) FROM target"
        cursor.execute(NumTargets)
        data = cursor.fetchmany()
        print("\nEl número total de dianas terapeúticas es: ")
        for row in data:
            print(row[0])
        volver(menu1)
    
    #1.b-Mostrar las 10 primeras instancias de:
    #1.b.i-Fármacos
    elif menuSelect == 5:
        Drugs = "SELECT drug_id, drug_name, molecular_type,\
            chemical_structure, inchi_key FROM drug\
            WHERE (drug_id AND drug_name AND molecular_type \
            AND chemical_structure AND inchi_key) IS NOT NULL LIMIT 10"
            #hemos limitado la consulta a las 10 primeras filas, de forma
            #que luego podemos hacer un fetchall.
        cursor.execute(Drugs)
        data = cursor.fetchall() 
        print("\nLas primeras 10 instancias de los fármacos son: ")
        print(*data, sep = '\n') #añadimos separación entre las lineas de resultado
        volver(menu1)
    
    #1.b.ii-Enfermedades
    elif menuSelect == 6:
        Diseases = "SELECT * FROM disease WHERE (disease_id AND disease_name) \
            IS NOT NULL LIMIT 10"
        cursor.execute(Diseases)
        data = cursor.fetchall()
        print("\nLas primeras 10 instancias de las enfermedades son: ")
        print(*data, sep = '\n') 
        volver(menu1)
        
    #1.b.iii-Efectos fenotípicos
    elif menuSelect == 7:
        Phenotype_effects = "SELECT * FROM phenotype_effect WHERE\
             (phenotype_id AND phenotype_name) IS NOT NULL LIMIT 10"
        cursor.execute(Phenotype_effects)
        data = cursor.fetchall()
        print("\nLas 10 primeras instancias de los efectos fenotípicos son: ")
        print(*data, sep = '\n')
        volver(menu1)

    #1.b.iv-Dianas
    elif menuSelect == 8:
        Targets = "SELECT target_id, target_name_pref, target_type,\
            taxonomy_name FROM target, organism\
            WHERE (target_id AND target_name_pref AND target_type\
            AND taxonomy_name) IS NOT NULL AND\
            organism.taxonomy_id = target.organism_id ORDER BY target_id ASC"
        cursor.execute(Targets)
        data = cursor.fetchmany(10) # si no ponemos LIMIT 10 en la consulta,
        #utilizamos fetchmany(10) en el cursor.
        print("\nLas primeras 10 instancias de las dianas son: ")
        print(*data, sep = '\n')
        volver(menu1)

    elif menuSelect == 9: 
        main() #Regresar al menú principal
        
    else:
        print("\nNo existe esa opción, pruebe otra vez.")
        menu1()
        

# In[6]:

#---------------------------------APARTADO 2-------------------------------
#Función para hacer consultas sobre la información de los fármacos

def menu2():
    print("----------------------------------------------")
    print("Información de los Fármacos")
    print("\t[1]Información de un Fármaco dado")
    print("\t[2]Sinónimos de un Fármaco dado")
    print("\t[3]Código ATC de un Fármaco dado")
    print("[4]Regresar al menú principal")
    print("----------------------------------------------")
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("\nNo existe esa opción, pruebe otra vez.")
    print("----------------------------------------------")
    
    #2.a-Información de un fármaco dado mediante el ID
    if menuSelect == 1:
        drug_id = input("Ingrese el ID del fármaco (identificador ChEMBL):\n")
        drug_id=drug_id.upper()
        Info_Farmaco = "SELECT drug_name, molecular_type, chemical_structure,\
            inchi_key FROM drug WHERE drug_id = '%s'" % (drug_id)
        cursor.execute(Info_Farmaco)
        data = cursor.fetchmany()
        if len(data) == 0:
            print("\nLa base de datos no dispone de este ID")
        else:
            print("\nLa información del fármaco con ID",drug_id,"es: ")
            print(data)
        volver(menu2)

    #2.b-Mostrar sinónimos de un fármado dado mediante el nombre
    elif menuSelect == 2:
        drug_name = input("Escriba el nombre del fármaco del cual quiere \n"
                          "que se muestren los posibles sinónimos:\n")
        drug_name=drug_name.upper() #Guardamos el nombre en mayúsculas
        Info_Sinon = "SELECT synonymous_name FROM synonymous, drug\
            WHERE synonymous.drug_id = drug.drug_id AND drug.drug_name = '%s'\
            AND synonymous.synonymous_name <> '%s'" %(drug_name, drug_name)
        cursor.execute(Info_Sinon)
        data = cursor.fetchall() 
        if len(data) == 0:
            print("\nNo existen fármacos sinónimos para el fármaco dado")
        else:
            print("\nLos fármacos sinónimos de",drug_name,"son: ")
            print(data)
        volver(menu2)

    #2.c-Muestra el código ATC de un fármaco dado por el identificador ChEMBL
    elif menuSelect == 3:
       
        drug_id = input("Escriba el ID del fármaco (identificador ChEMBL) \n"
                        "del cual quiere que se muestren los códigos ATC \n"
                        "asociados:\n")
        drug_id=drug_id.upper()
        Info_codATC = "SELECT ATC_code_id FROM atc_code WHERE\
            atc_code.drug_id = '%s'" %(drug_id)
        cursor.execute(Info_codATC)
        data = cursor.fetchall()
        if len(data) == 0:
            #Mensaje de error si no se encuentra ningún codigo ATC
            print("\nNo hay códigos ATC asociados a este fármaco")
        else:
            print("\nLos códigos ATC asociados al fármaco de ID:\n",drug_id, "son: ")
            for row in data:
                print (row[0])
        volver(menu2)
            
    elif menuSelect == 4:
        main()
    else:
        print("\nNo existe esa opción, pruebe otra vez.")
        menu2()


# In[7]:

#---------------------------------APARTADO 3-------------------------------
#Función para hacer consultas de las enfermedades

def menu3():
    print("----------------------------------------------")
    print("Información de las Enfermedades")
    print("\t[1]Fármacos para una enfermedad")
    print("\t[2]Fármaco y enfermedad con mayor\n\t   score de asociación")
    print("[3]Regresar al menú principal")
    print("----------------------------------------------")
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("\nNo existe esa opción, pruebe otra vez.")
    print("----------------------------------------------")

    #3.a-Información de un fármaco en base al nombre de la enfermedad introducida
    if menuSelect == 1:
        disease_code_name = input("Escriba el nombre de la enfermedad para la cual \n"
                                  "quiere que se muestren los fármacos asociados:\n")
        disease_code_name = disease_code_name.upper()
        Info_DrDs = "SELECT drug.drug_id, drug.drug_name\
            FROM drug, drug_disease ds, disease_code WHERE disease_code.name = '%s'\
            AND drug.drug_id=ds.drug_id AND ds.code_id=disease_code.code_id" %(disease_code_name)
        cursor.execute(Info_DrDs)
        data = cursor.fetchall()
        #Avisamos al usuario si la enfermedad que ha introducido no devuelve
        #ningún fármaco asociado.
        if len(data) == 0:
            print("\nEsta enfermedad no tiene ningún fármaco asociado")
        else:
            print("\nLos fármacos para la enfermedad\n",disease_code_name,"son: ")
            print(*data, sep = '\n')
        volver(menu3)

    #3.b-Fármaco y enfermedad con mayor score de asociación
    elif menuSelect == 2:
        Info_Score = "SELECT disease_code.name, drug.drug_name, ds.inferred_score\
            FROM drug, disease_code, drug_disease ds WHERE drug.drug_id=ds.drug_id\
            AND ds.code_id=disease_code.code_id ORDER BY ds.inferred_score DESC"
        print("Esta consulta puede tardar unos segundos")
        cursor.execute(Info_Score)
        data = cursor.fetchmany() #Mostramos solo la primera fila de las que 
        #devuelve la consulta (corresponde al par con mayor score).
        print("\nEl par enfermedad-fármaco con mayor score de \n"
              "asociación (valor que también se da) es:")
        print(*data, sep = '\n')
        
        volver(menu3)
            
    elif menuSelect == 3:
        main()
    else:
        print("\nNo existe esa opción, pruebe otra vez.")
        menu3()


# In[8]:

#---------------------------------APARTADO 4-------------------------------
#Función para hacer consultas de los efectos fenotípicos

def menu4():
    print("----------------------------------------------")
    print("Información de lo Efectos fenotípicos")
    print("\t[1]Indicaciones de un fármaco dado")
    print("\t[2]Efectos secundarios de un fármaco dado")
    print("[3]Regresar al menú principal")
    print("----------------------------------------------")
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("\nNo existe esa opción, pruebe otra vez.")
    print("----------------------------------------------")
    
    #4.a-Indicaciones de un fármaco dado mediante el identificador ChEMBL
    if menuSelect == 1:
        drug_id = input("Escriba el ID (ChEMBL) del fármaco para el que \n"
                        "quiere que se muestren los efectos fenotípicos \n"
                        "para los que se usa:\n")
        drug_id=drug_id.upper()
        Info_Indic = "SELECT p.phenotype_id, p.phenotype_name\
            FROM drug_phenotype_effect dp, phenotype_effect p\
            WHERE dp.drug_id = '%s' AND dp.phenotype_type='INDICATION'\
            AND p.phenotype_id=dp.phenotype_id" %(drug_id)
        cursor.execute(Info_Indic)
        data = cursor.fetchall()
        if len(data) == 0:
            print("\nNo se han encontrado fenotipos que sean indicaciones \n"
                  "para el uso de este fármaco")
        else:
            print("\nLos efectos fenotípicos para los que se usa el \n"
                  "fármaco con ID",drug_id,"son: \n")
            print(*data, sep="\n")
        volver(menu4)
    
    #4.b-Efectos secundarios de un fármaco dado mediante el identificador ChEMBL
    elif menuSelect == 2:
        drug_id = input("Escriba el ID (ChEMBL) del fármaco para el que \n"
                        "quiere que se muestren los efectos secundarios \n"
                        "asociados:\n")
        drug_id=drug_id.upper()
        Info_Secun = "SELECT p.phenotype_id, p.phenotype_name FROM\
            drug_phenotype_effect dp, phenotype_effect p\
            WHERE dp.drug_id = '%s' AND dp.phenotype_type='SIDE EFFECT'\
            AND p.phenotype_id=dp.phenotype_id ORDER BY dp.score DESC" %(drug_id)
        cursor.execute(Info_Secun)
        data = cursor.fetchall()
        #Avisamos al usuario si no se han encontrado efectos secundarios
        #para el ID que ha introducido
        if len(data) == 0:
            print("No se han encontrado efectos secundarios asociados a este fármaco")
        else:
            print("\nLos efectos secundarios del farmaco",drug_id,"\n"
                  "(ordenados de forma descendente en base a la \n"
                  "evidencia de esta asociación) son: \n")
            print(*data, sep='\n')
        volver(menu4)
    
    elif menuSelect == 3:
        main()
            
    else:
        print("\nNo existe esa opción, pruebe otra vez.")
        menu4()


# In[9]:

#---------------------------------APARTADO 5-------------------------------
#Funcion para hacer consultas de los targets

def menu5():
    print("----------------------------------------------")
    print("Información de las dianas")
    print("\t[1]Dianas de un tipo dado")
    print("\t[2]Organismo asociado con mayor número de \n\t   dianas")
    print("[3]Regresar al menú principal")
    print("----------------------------------------------")
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("\nNo existe esa opción, pruebe otra vez.")
    print("----------------------------------------------")
    
    #5.a-Mostrar 20 primeras dianas 
    if menuSelect == 3:
        main()
    elif menuSelect == 1:
        target_type = input("Escriba el tipo de diana para el que quiere que \n"
                            "se muestren 20 dianas por orden alfabético: \n")
        #ORDER BY ... ASC- dianas ordenadas alfabéticamente
        Target_ejs = "SELECT target_name_pref FROM target WHERE\
            target_type='%s' ORDER BY target_name_pref ASC\
            LIMIT 20" %(target_type)
        cursor.execute(Target_ejs)
        data = cursor.fetchmany(20)
        if len(data) == 0:
            print("\nNo existen dianas de este tipo en la base de datos")
        else:
            print(*data, sep='\n')
        volver(menu5)
        
    #5.b-Organismo al cual se asocia mayor número de dianas distintas
    elif menuSelect == 2:
        Max_ntargets="SELECT o.taxonomy_name, count(t.target_id)\
            FROM target t, organism o WHERE t.organism_id=o.taxonomy_id\
            GROUP BY t.organism_id ORDER BY count(t.target_id) DESC"
        cursor.execute(Max_ntargets)
        #fetchone devuelve solo la primera fila de las que devuelve la consulta
        data = cursor.fetchone()
        print("El organismo al que se le asocia un mayor número \n"
              "de dianas (valor que también se muestra) es:")
        print(data)
        volver(menu5)
        
    else:
        print("\nNo existe esa opción, pruebe otra vez.")
        menu5()


# In[10]:

#---------------------------------APARTADO 6-------------------------------
#Función para hacer borrados

def menu6():
    print("----------------------------------------------")
    print("Borrados")
    print("\t[1]Continuar con la función Borrado")
    print("[2]Regresar al menu principal")
    print("----------------------------------------------")
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("\nNo existe esa opción, pruebe otra vez.")
    print("----------------------------------------------")
    
    #Borrar asociacion entre un fármaco y enfermedad con score muy bajo
    if menuSelect == 1:
        print("Las 10 asociaciones fármaco-enfermedad con menor \n"
              "score son (esta operación puede tardar varios segundos):")
        #ORDER BY...ASC-ordenar por score ascendente,nombre fármaco y nombre de enfermedad-en ese orden
        Low_Score = "SELECT ds.inferred_score, drug.drug_name, disease_code.name\
            FROM drug, disease_code, drug_disease ds WHERE ds.inferred_score\
            IS NOT NULL AND drug.drug_id=ds.drug_id\
            AND ds.code_id=disease_code.code_id ORDER BY ds.inferred_score ASC,\
            drug.drug_name ASC, disease_code.name ASC"
            
        cursor.execute(Low_Score)
        data = cursor.fetchmany(10) #Mostrar las 10 primeras asociaciones con menor score
        print(*data, sep = '\n')
        
        #Pedir al usuario que escriba el fármaco y enfermedad que desea borrar
        drug_name = input("\nEscriba el fármaco que aparece en el par \n"
                          "fármaco-enfermedad que quiere borrar:\n")
        dis_code_name = input("\nEscriba la enfermedad que aparece en el par \n"
                              "fármaco-enfermedad que quiere borrar:\n")
        print("\nProcediendo a borrar la asociación",drug_name,"-",dis_code_name,"de la base de datos...")
        delete_instance = "DELETE FROM drug_disease\
            WHERE code_id=(SELECT disease_code.code_id from disease_code\
            WHERE disease_code.name = '%s') AND drug_id=(SELECT drug.drug_id from drug\
            WHERE drug.drug_name = '%s')" % (dis_code_name, drug_name)
        cursor.execute(delete_instance)
        row_count = cursor.rowcount
        #Si se ha conseguido borrar la asociación, el objeto row_count será 1
        #En ese caso, mostraremos al usuario la lista actualizada tras el borrado.
        if row_count == 1:
            print ("\nHecho. Número de lineas eliminadas:",row_count)
            print ("Le mostraremos de nuevo la lista para que \n"
                   "compruebe que se ha eliminado la asociación:\n")
            cursor.execute(Low_Score)
            data = cursor.fetchmany(10)
            print(*data, sep = '\n')
        #Si no se ha encontrado la asociación solicitada por el usuario,
        #no se habrá podido llevar a cabo su borrado, así que le avisamos.
        elif row_count == 0:
            print ("No ha sido posible borrar la asociación\n"
                   ,drug_name,"-",dis_code_name,", asegúrese de escribir bien \n"
                   "los nombres si lo vuelve a intentar.")
        volver(menu6) 
                
    elif menuSelect == 2:
        main()
    else:
        print("\nNo existe esa opción, pruebe otra vez.")
        menu6()


# In[11]:

#---------------------------------APARTADO 7-------------------------------
#Función para hacer inserciones

def menu7():
    print("----------------------------------------------")
    clear_output(wait=True)
    print("Inserciones")
    print("\t[1]Continuar con la función Inserción")
    print("[2]Regresar al menú principal")
    print("----------------------------------------------")
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("\nNo existe esa opción, pruebe otra vez.")
    print("----------------------------------------------")
    
    if menuSelect ==1:
        print("Información sobre la inserción")
        drug_name = input("Escriba el nombre del fármaco (debe estar ya \n"
                          "presente en la base de datos) al que quiere \n"
                          "asociar un nuevo identificador: \n")
        #Para asegurarnos de que el nombre del fármaco que ha dado el usuario
        #existe en nuestra base de datos, hacemos una consulta buscando el ID
        #de dicho fármaco.
        drug_id_already = "SELECT drug_id FROM drug WHERE drug_name='%s'" % (drug_name)
        cursor.execute(drug_id_already)
        drug_id = cursor.fetchone()  
        #drug_id es un objeto que contiene el ID existente (si es que existe)
        #en la BD que corresponde al fármaco que ha introducido el usuario.
        #Solo que está entre comillas y almacenado en una tupla.
        #cursor.fetchone devolverá un objeto nulo (None) si no hay un ID para
        #el nombre del fármaco del usuario. En ese caso, avisamos al usuario.
        if drug_id == None:
            print("\nEl nombre introducido no corresponde a ningún \n"
                  "fármaco de la base de datos.")
            volver(menu7)
        #Si sí hemos encontrado el ID en la BD que corresponde al fármaco del usario...    
        else:
            drug_id_literal = drug_id[0] #sacamos el ID de las comillas y de la tupla para poder
            #utilizarlo en una consulta.
            #Y pedimos al usuario la nueva codificación del fármaco y el vocabulario de esta.
            new_code_id = input("Escriba la nueva codificación que quiere \n"
                                "asociar a dicho fármaco: \n")
            new_vocab = input("Escriba el vocabulario al que pertenece \n"
                              "esa codificación: \n")
            
            #comprobamos que el nuevo ID introducido por el usuario sea nuevo de verda en la BD.
            check_new_code = "SELECT code_id FROM drug_has_code WHERE code_id='%s'" % (new_code_id)
            cursor.execute(check_new_code)
            code_check = cursor.fetchmany()
            
            if len(code_check) == 1: #Si la consulta ha devuelto el código, code_check será un
            #objeto con longitud 1, así que avisamos al usuario de que el código introducido no es nuevo.
                print("\nEl código introducido ya existe en la base de datos")
                volver(menu7)
            elif len(code_check) == 0: #Si no se ha encontrado el código del usuario en la BD, seguimos
            #con la inserción
                print("\nIntroduciendo",drug_id_literal,new_code_id,new_vocab,"\nen la tabla drug_has_code...")
                insertion = "INSERT INTO drug_has_code VALUES('%s', '%s', '%s')" % (drug_id_literal, new_code_id, new_vocab)
                #Necesitamos utilizar el objeto drug_id_literal mencionado anteriormente para que
                #funcione la inserción (con durg_id da error)
                cursor.execute(insertion)
                print("\nHecho")
                volver(menu7)
            
    elif menuSelect == 2:
        main()
    else:
        print("\nNo existe esa opción, pruebe otra vez.")
        menu7()


# In[12]:

#---------------------------------APARTADO 8-------------------------------
#Función para hacer modificaciones en los scores

def menu8():
    print("----------------------------------------------")
    print("Modificaciones")
    print("\t[1]Continuar con la función Modificación")
    print("[2]Regresar al menú principal")
    print("----------------------------------------------")
    while True:
        try:
            menuSelect = int(input("Ingrese la opción: "))
            break
        except ValueError:
            print("\nNo existe esa opción, pruebe otra vez.")
    print("----------------------------------------------")

    if menuSelect == 2:
        main()
    elif menuSelect == 1:
        print("\nLos scores de asociación fármaco - efecto \n"
              "secundario que estén por debajo del umbral que \n"
              "usted dé por teclado (o sean iguales a este)\n"
              " serán actualizados para tener un valor de 0")
        Min_score=input("Escriba el valor para ese umbral (si va a escribir \n"
                        "parte decimal, utilice punto en vez de coma): \n")
        #Modificar solo en el caso de los EFECTOS SECUNDARIOS (SIDE EFFECT)
        Score_updt = "UPDATE drug_phenotype_effect SET score=0\
            WHERE phenotype_type='SIDE EFFECT' AND score BETWEEN 0 AND '%s'" %(Min_score)
        cursor.execute(Score_updt)
        print("\nHecho.")
        volver(menu8)
    else:
        print("\nNo existe esa opción, pruebe otra vez.")
        menu8()
        
# In[13]:
#---------------------------------APARTADO 9-------------------------------
#Funcion de ayuda para usar el programa

def menu9(): 
    print("\n----------------------------------------------\n\n"
          "\t\t\t RESUMEN DEL PROGRAMA\n\n"
          "----------------------------------------------\n"
          "Este programa ofrece acceso a la base de datos \n"
          "disnet_drugslayer y permite hacer consultas,\n"
          "borrados, inserciones y modificaciones.\n"
          "\nTablas:  \n"
          "\t - DRUGS: tabla principal que contiene \n"
          "\t\t información relacionada con cada fármaco \n"
          "\t\t (identificador, nombre, tipo molecular,\n"
          "\t\t estructura química etc).\n"
          "\t - DISEASE: contiene información relativa a \n"
          "\t\t enfermedades. Recoge otras tablas como \n"
          "\t\t drug_disease que relaciona farmacos\n"
          "\t\t y enfermedades.\n"
          "\t - PHENOTYPE EFFECT: efectos fenotípicos. \n"
          "\t\t Recoge también la tabla 'drug_phenotype_effect'\n"
          "\t\t que relaciona farmacos con los efectos fenotípicos.\n"
          "\t - TARGET: dianas terapéuticas de los fármacos. \n"
          "\t\t Recoge también la tabla 'organism' con los \n"
          "\t\t nombres de los organismos y la tabla 'drug_target'\n"
          "\t\t que relaciona los fármacos con los targets.\n"
          "\n-----------------------------------------------\n\n"
          "\t\t\t USO DEL PROGRAMA\n\n"
          "----------------------------------------------\n"
          "En el menú principal podrá ver 9 opciones, \n"
          "teclee el número correspondiente a la consulta que\n"
          "desee hacer en el terminal.\n"
          "En todos los submenús tendrá la opción de volver\n"
          "al menú principal.\n"
          "--------------------"
          "\n\nIMPORTANTE: \n"
          "En las opciones del menu, de la 1 a la 5 son\n"
          "consultas, pero las opciones de la 6 a la 8 \n"
          "permiten hacer cambios en la base de datos.\n"
          "---------------------------------------------------"
          "\nGRACIAS POR USAR ESTE PROGRAMA"
          )
    volver(main)
    
# In[14]:
    
#Función para salir en el menú principal

def f_exit():
    respuesta=input("¿Está seguro que desea salir? \n"
                    "[S para Sí, cualquier otra tecla para permanecer\n"
                    "en el Menú Principal de Consultas] \n")
    respuesta=respuesta.upper()
    if respuesta=="S":
        db.close()
        exit()
    else:
        main()
    
#---------------------------------FUNCION VOLVER-------------------------------

def volver(x):
    respuesta=input("¿Quiere realizar otra consulta? \n"
                    "[S para Sí, cualquier otra tecla para No] ")
    respuesta=respuesta.upper()
    if respuesta=="S":
        x()
    else:
        db.close()
        exit()
    
# In[15]:


main()



