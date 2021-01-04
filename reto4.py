from io import open

class Alumno:
    def __init__(self,nombre,edad,dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

class Docente:
    def __init__(self,nombre,edad,dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

class Curso:
    def __init__(self,nombre):
        self.nombre=nombre

class Nota:
    def __init__(self,nombre_alumno,nombre_curso):
        self.nombre_alumno=nombre_alumno
        self.nombre_curso=nombre_curso
        self.notas=[]
        
    def añadir_notas(self,nota):
        self.notas.append(nota)
    
def añadir_cursos():
    cantidad=int(input("Ingrese cantidad de cursos: "))
    file=open("cursos.txt","a")
    for i in range(cantidad):
        c=Curso(input("Ingrese curso: "))
        file.write(c.nombre+"\n")
    file.close()

def create_alumno():
    file=open("alumnos.txt","a")
    alumno=input("Ingrese nombre del alumno: ")
    edad=input("Ingrese edad del alumno: ")
    dni=input("Dni del alumno: ")
    
    al=Alumno(alumno,edad,dni)

    texto="Nombre de alumno: "+al.nombre+" Edad de alumno: "+al.edad+" Dni del alumno: "+al.dni+"\n"
    file.write(texto)
    file.close()

    cursos=[]
    file=open("cursos.txt","r")
    for linea in file.readlines():
        cursos.append(linea.rstrip("\n"))
    file.close()

    texto1=""
    texto2=""
    texto3=""
    suma=0
    notas=[]
    for i in range(len(cursos)):
        nota=input("Ingrese nota de "+cursos[i]+": ")
        n=Nota(al.nombre,cursos[i])
        n.añadir_notas(nota)
        notas.append(int(nota))
        suma=suma+int(nota)
        texto1=texto1+cursos[i]+": "+nota+" "
    promedio=round(suma/len(cursos),2)

    mayor=-99
    menor=99
    for i in notas:
        if i>mayor:
            mayor=i
        if i<menor:
            menor=i
    
    texto2=texto2+str(promedio)
    texto3=texto3+"Nombre: "+n.nombre_alumno+" Cursos: "+texto1+" Promedio: "+texto2+" Mayor nota: "+str(mayor)+" Menor nota: "+str(menor)+"\n"

    file=open("notas.txt","a")
    file.write(texto3)
    file.close()

def read_alumno():
    file=open("alumnos.txt","r")
    for linea in file.readlines():
        print(linea)
    file.close()

def update_alumno_edad():
    texto=[]
    file=open("alumnos.txt","r")
    for linea in file.readlines():
        texto.append(linea.rstrip("\n"))
    file.close()
    nombre=input("Ingrese alumno a buscar: ")
    for i in range(len(texto)):
        if texto[i].split(" ")[3]==nombre:
            nuevoEdad=input("Ingrese nueva edad: ")
            indice=i
            break

    texto2=""
    if indice>0 and indice<len(texto):
        for i in range(indice):
            texto2=texto2+texto[i]+"\n"
        for i in range(indice,indice+1):
            texto2=texto2+"Nombre de alumno: "+texto[i].split(" ")[3]+" Edad de alumno: "+nuevoEdad+" Dni de alumno: "+texto[i].split(" ")[11]+"\n"
        for i in range(indice+1,len(texto)):
            texto2=texto2+texto[i]+"\n"
    elif indice==0:
        texto2=texto2+"Nombre de alumno: "+texto[i].split(" ")[3]+" Edad de alumno: "+nuevoEdad+" Dni de alumno: "+texto[i].split(" ")[11]+"\n"
        for i in range(indice+1,len(texto)):
            texto2=texto2+texto[i]+"\n"
    elif indice==len(texto)-1:
        for i in range(len(texto)-2):
            texto2=texto2+texto[i]+"\n"
        texto2=texto2+"Nombre de alumno: "+texto[i].split(" ")[3]+" Edad de alumno: "+nuevoEdad+" Dni de alumno: "+texto[i].split(" ")[11]+"\n"

    file=open("alumnos.txt","w")
    file.write(texto2)
    file.close()
    
def update_alumno_dni():
    texto=[]
    file=open("alumnos.txt","r")
    for linea in file.readlines():
        texto.append(linea.rstrip("\n"))
    file.close()
    nombre=input("Ingrese alumno a buscar: ")
    for i in range(len(texto)):
        if texto[i].split(" ")[3]==nombre:
            nuevoDni=input("Ingrese nuevo dni: ")
            indice=i
            break

    texto2=""
    if indice>0 and indice<len(texto):
        for i in range(indice):
            texto2=texto2+texto[i]+"\n"
        for i in range(indice,indice+1):
            texto2=texto2+"Nombre de alumno: "+texto[i].split(" ")[3]+" Edad de alumno: "+texto[i].split(" ")[7]+" Dni de alumno: "+nuevoDni+"\n"
        for i in range(indice+1,len(texto)):
            texto2=texto2+texto[i]+"\n"
    elif indice==0:
        texto2=texto2+"Nombre de alumno: "+texto[i].split(" ")[3]+" Edad de alumno: "+texto[i].split(" ")[7]+" Dni de alumno: "+nuevoDni+"\n"
        for i in range(indice+1,len(texto)):
            texto2=texto2+texto[i]+"\n"
    elif indice==len(texto)-1:
        for i in range(len(texto)-2):
            texto2=texto2+texto[i]+"\n"
        texto2=texto2+"Nombre de alumno: "+texto[i].split(" ")[3]+" Edad de alumno: "+texto[i].split(" ")[7]+" Dni de alumno: "+nuevoDni+"\n"

    file=open("alumnos.txt","w")
    file.write(texto2)
    file.close()

def delete_alumno():
    texto=[]
    file=open("alumnos.txt","r")
    for linea in file.readlines():
        texto.append(linea.rstrip("\n"))
    file.close()
    nombre=input("Ingresa alumno a borrar: ")
    for i in range(len(texto)):
        if texto[i].split(" ")[3]==nombre:
            indice=i
            break

    texto2=""
    for i in range(indice):
        texto2=texto2+texto[i]+"\n"
    for i in range(indice+1,len(texto)):
        texto2=texto2+texto[i]+"\n"

    file=open("alumnos.txt","w")
    file.write(texto2)
    file.close()


    texto3=[]
    file=open("notas.txt","r")
    for linea in file.readlines():
        texto3.append(linea.rstrip("\n"))
    file.close()

    for i in range(len(texto3)):
        if texto3[i].split(" ")[1]==nombre:
            indice=i
            break

    texto4=""
    for i in range(indice):
        texto4=texto4+texto3[i]+"\n"
    for i in range(indice+1,len(texto3)):
        texto4=texto4+texto3[i]+"\n"

    file=open("notas.txt","w")
    file.write(texto4)
    file.close()


def create_docente():
    file=open("docentes.txt","a")
    docente=input("Ingrese nombre del docente: ")
    edad=input("Ingrese edad del docente: ")
    dni=input("Dni del docente: ")
    
    doc=Docente(docente,edad,dni)

    texto="Nombre de docente: "+doc.nombre+" Edad de docente: "+doc.edad+" Dni del docente: "+doc.dni+"\n"
    file.write(texto)
    file.close()

def read_docente():
    file=open("docentes.txt","r")
    for linea in file.readlines():
        print(linea)
    file.close()

def update_docente_edad():
    texto=[]
    file=open("docentes.txt","r")
    for linea in file.readlines():
        texto.append(linea.rstrip("\n"))
    file.close()
    nombre=input("Ingrese docente a buscar: ")
    for i in range(len(texto)):
        if texto[i].split(" ")[3]==nombre:
            nuevoEdad=input("Ingrese nueva edad: ")
            indice=i
            break

    texto2=""
    if indice>0 and indice<len(texto):
        for i in range(indice):
            texto2=texto2+texto[i]+"\n"
        for i in range(indice,indice+1):
            texto2=texto2+"Nombre de docente: "+texto[i].split(" ")[3]+" Edad de docente: "+nuevoEdad+" Dni de docente: "+texto[i].split(" ")[11]+"\n"
        for i in range(indice+1,len(texto)):
            texto2=texto2+texto[i]+"\n"
    elif indice==0:
        texto2=texto2+"Nombre de docente: "+texto[i].split(" ")[3]+" Edad de docente: "+nuevoEdad+" Dni de docente: "+texto[i].split(" ")[11]+"\n"
        for i in range(indice+1,len(texto)):
            texto2=texto2+texto[i]+"\n"
    elif indice==len(texto)-1:
        for i in range(len(texto)-2):
            texto2=texto2+texto[i]+"\n"
        texto2=texto2+"Nombre de docente: "+texto[i].split(" ")[3]+" Edad de docente: "+nuevoEdad+" Dni de docente: "+texto[i].split(" ")[11]+"\n"

    file=open("docentes.txt","w")
    file.write(texto2)
    file.close()

def update_docente_dni():
    texto=[]
    file=open("docentes.txt","r")
    for linea in file.readlines():
        texto.append(linea.rstrip("\n"))
    file.close()
    nombre=input("Ingrese docente a buscar: ")
    for i in range(len(texto)):
        if texto[i].split(" ")[3]==nombre:
            nuevoDni=input("Ingrese nuevo dni: ")
            indice=i
            break

    texto2=""
    if indice>0 and indice<len(texto):
        for i in range(indice):
            texto2=texto2+texto[i]+"\n"
        for i in range(indice,indice+1):
            texto2=texto2+"Nombre de docente: "+texto[i].split(" ")[3]+" Edad de docente: "+texto[i].split(" ")[7]+" Dni de docente: "+nuevoDni+"\n"
        for i in range(indice+1,len(texto)):
            texto2=texto2+texto[i]+"\n"
    elif indice==0:
        texto2=texto2+"Nombre de docente: "+texto[i].split(" ")[3]+" Edad de docente: "+texto[i].split(" ")[7]+" Dni de docente: "+nuevoDni+"\n"
        for i in range(indice+1,len(texto)):
            texto2=texto2+texto[i]+"\n"
    elif indice==len(texto)-1:
        for i in range(len(texto)-2):
            texto2=texto2+texto[i]+"\n"
        texto2=texto2+"Nombre de docente: "+texto[i].split(" ")[3]+" Edad de docente: "+texto[i].split(" ")[7]+" Dni de docente: "+nuevoDni+"\n"

    file=open("docentes.txt","w")
    file.write(texto2)
    file.close()

def delete_docente():
    texto=[]
    file=open("docentes.txt","r")
    for linea in file.readlines():
        texto.append(linea.rstrip("\n"))
    file.close()
    nombre=input("Ingresa docente a borrar: ")
    for i in range(len(texto)):
        if texto[i].split(" ")[3]==nombre:
            indice=i
            break

    texto2=""
    for i in range(indice):
        texto2=texto2+texto[i]+"\n"
    for i in range(indice+1,len(texto)):
        texto2=texto2+texto[i]+"\n"

    print(texto2)
    file=open("docentes.txt","w")
    file.write(texto2)
    file.close()

#añadir_cursos()

def leer_estadisticas():
    texto=[]
    file=open("notas.txt","r")
    for linea in file.readlines():
        texto.append(linea.rstrip("\n"))
    file.close()
    nombre=input("Escriba nombre de alumno: ")
    for i in range(len(texto)):
        if texto[i].split(" ")[1]==nombre:
           print(texto[i])
           break

def menu():
    print("RETO SEMANA 4: \n")
    print("0. Crear alumno: ")
    print("1. Leer alumnos: ")
    print("2. Actualizar edad del alumno: ")
    print("3. Actualizar dni del alumno: ")
    print("4. Eliminar alumno: ")
    print("5. Crear docente: ")
    print("6. Leer docentes: ")
    print("7. Actualizar edad del docente: ")
    print("8. Actualizar dni del docente: ")
    print("9. Eliminar docente: ")
    print("10. Notas de alumno: \n")

    opcion=int(input("Escoja opcion: "))
    while opcion<0 or opcion>10:
        opcion=int(input("Escoja opcion entre 0 y 10: "))
    return opcion

opcion=menu()
while opcion<=10:
    if opcion==0:
        create_alumno()
    elif opcion==1:
        read_alumno()
    elif opcion==2:
        update_alumno_edad()
    elif opcion==3:
        update_alumno_dni()
    elif opcion==4:
        delete_alumno()
    elif opcion==5:
        create_docente()
    elif opcion==6:
        read_docente()
    elif opcion==7:
        update_docente_edad()
    elif opcion==8:
        update_docente_dni()
    elif opcion==9:
        delete_docente()
    elif opcion==10:
        leer_estadisticas()

    print()
    opcion=menu()
