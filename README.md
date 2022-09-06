# Acceso_programatico_a_Disnet_drugslayer

Este programa escrito en Python permite acceder a la base de datos ‘disnet_drugslayer.sql’. A través de una conexión con MySQL Workbench el usuario será capaz de realizar diferentes operaciones sobre la información de las tablas de datos. Las operaciones se pueden elegir a través de un menú que muestra las siguientes opciones:

## Consultas
### 1. Información general de la base de datos:

#### a. Número total:

Muestra el número total de fármacos, enfermedades, efectos fenotípicos, y targets diferentes. 

* i. NumDrugs: número de fármacos diferentes.
* ii. NumDiseases: número de enfermedades diferentes (identificadas por el 
UMLS CUI, tabla ‘disease’).
* iii. NumPhenoEff: número de efectos fenotípicos.
* iv. NumTargets: número de targets diferentes.
* v. NumDDIs: número de interacciones entre fármacos diferentes.

#### b. Primeras 10 instancias:

Muestra las 10 primeras instancias de cada una de las anteriores entidades: 
fármacos, enfermedades, efectos fenotípicos y targets. Muestra sólo aquellas 
instancias en las que ninguno de los campos que se pide sea nulo. De cada instancia muestra:

* i. Drugs: identificador, nombre, tipo molecular, estructura química e InChykey.
* ii. Diseases: identificador (UMLS CUI, es decir, ‘disease_id’) y nombre
(‘disease_name’).
* iii. Phenotype effects: identificador y nombre.
* iv. Targets: identificador, nombre, tipo y nombre del organismo
(‘taxonomy_name’).


### 2. Información de los fármacos:

#### a. Información de un fármaco dado:
Dado el identificador de ChEMBL de un fármaco (‘drug_id’) (que se pide por 
teclado), muestra su nombre (‘drug_name’), tipo molecular (‘molecular_type’), 
estructura química (‘chemical_structure’) e InChi-key (‘inchi_key’).

#### b. Sinónimos de un fármaco dado:
Dado el nombre de un fármaco (‘drug.drug_name’) (que debe pedirse por teclado), 
muestra los posibles sinónimos de este (‘synonymous.synonymous_name’).

#### c. Código ATC de un fármaco dado:
Dado el identificador de ChEMBL de un fármaco (‘drug_id’) (que se pide por 
teclado), muestra el/los códigos ATC asociados (‘ATC_code_id’). Si no se encuentra 
ningún código ATC para dicho fármaco, muestra un mensaje informando al usuario 
de que la base de datos no tiene guardado un código ATC para dicho fármaco.

### 3. Información de las enfermedades:

#### a. Fármacos para una enfermedad:
Dado el nombre de una enfermedad en un vocabulario (disease_code.name) (que se pide por teclado), muestra los identificadores (drug.drug_id) y nombres 
(drug.drug_name) de los fármacos con los cuales se puede tratar dicha enfermedad.

#### b. Fármaco y enfermedad con el mayor score de asociación:
Muestra los nombres de la enfermedad (disease_code.name) y del fármaco
(drug.drug_name) que presentan el mayor valor del score de asociación 
(inferred_score).

### 4. Información de los efectos fenotípicos:

#### a. Indicaciones de un fármaco dado:
Dado el identificador de ChEMBL de un fármaco (‘drug_id’) (que se pide por 
teclado), muestra aquellos efectos fenotípicos que sean indicaciones para las cuales 
se utiliza el fármaco. Muestra el identificador (‘phenotype_effect’.‘phenotype_id’) y 
el nombre (‘phenotype_effect’.‘phenotype_name’) del efecto fenotípico.

#### b. Efectos secundarios de un fármaco dado:
Dado el identificador de ChEMBL de un fármaco (‘drug_id’) (que debe pedirse por 
teclado), muestra aquellos efectos fenotípicos categorizados como efectos 
secundarios generados por el fármaco. Se devuelven ordenados de forma 
descendente en base a la evidencia de esta asociación (score). Muestra el 
identificador (‘phenotype_effect’.‘phenotype_id’) y el nombre (‘phenotype_effect’.
‘phenotype_name’) del efecto fenotípico.

### 5. Información de los targets:

#### a. Dianas de un tipo dado:
Muestra el nombre de las primeras 20 dianas (‘target_name’) ordenadas 
alfabéticamente y de un tipo concreto (‘target_type’) (que se pide por 
teclado).

#### b. Organismo al cual se asocian un mayor número de dianas:
Muestra qué organismo (‘taxonomy_name’) está asociado a un mayor número de 
dianas distintas (‘target_id’).

## Borrados, inserciones, modificaciones

### 6. Borrados.

El usuario puede borrar la asociación entre un fármaco y una enfermedad con un score muy bajo
(‘inferred_score’). Para ello, el menú muestra las 10 primeras interacciones con un score menor (ordenadas por 
score ascendente, nombre del fármaco y de la enfermedad en este orden -se muestran estos campos-), de tal forma que el usuario 
puede seleccionar una de ellas y borrarla. (Sólo se borrará la asociación, no los fármacos o enfermedades que participen en ella).

### 7. Inserciones.

El usuario puede introducir nuevas codificaciones de fármacos asociadas a fármacos ya 
presentes en la base de datos. El usuario deberá proporcionar un nuevo identificador del 
fármaco (‘drug_has_code’.‘code_id’) y el vocabulario correspondiente (‘drug_has_code’.
‘vocabulary’), así como el nombre del fármaco (‘drug’.‘drug_name’) al cual está asociado (ya 
presente en la base de datos).

Un ejemplo podría ser que el usuario introdujese la siguiente información la aspirina:
* El nombre del fármaco: ‘ASPIRIN’
* La codificación del fármaco en el vocabulario nuevo: ‘D001241’
* El nombre del vocabulario en cuestión: ‘MeSH´

### 8. Modificaciones.

Hay scores de asociaciones entre fármacos y efectos secundarios muy bajos
(‘drug_phenotype_effect’.‘score’), con lo que dado un valor numérico (solicitado por 
teclado) todos los scores menores que ese, serán actualizados para tener un valor de 0.
Se aplica solo para el caso de los efectos secundarios, no de las indicaciones.
