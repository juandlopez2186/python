"""1. reto"""

o=1
n=int(input("digite el numero de vendedores "))
while o<=n: 
    v=(100000*100)/10
    t=v*3+100000
    print(f"lo que gana el vendedor por comision{v} y en total es {t}")
    o=o+1

        
"""2. reto"""

o=1
n=int(input("digite el numero de clientes "))
while o<=n:
    p=int(input("digite el valor de las compras "))
    c=int(input("digite el color de la balota ,1 rojo ,2 amarillo ,3 blanca "))
    if c==1:
        d=p*100/40
        t=d-p
        print(f"el precio total a pagar es de {t} ")
    if c==2:
        d=p*100/25
        t=d-p
        print(f"el precio total a pagar es de {t} ")
    if c==3:
        print(f"el precio total a pagar es de {p} ")
        

"""3. reto"""

n=1
while n<=40:
    m1=int(input("digite la nota de la materia no1 en rango de 1 a 5"))
    m2=int(input("digite la nota de la materia no2 en rango de 1 a 5"))
    m3=int(input("digite la nota de la materia no3 en rango de 1 a 5"))
    m4=int(input("digite la nota de la materia no4 en rango de 1 a 5"))
    m5=int(input("digite la nota de la materia no5 en rango de 1 a 5")) 
    pro=(m1+m2+m3+m4+m5)*100/5
    if pro<=3:
        print("el estudiante no tiene derecho al examen de nivelacion")
    else:
        print("el estudiante tiene derecho al examen de nivelacion")

"""4. reto"""
c1=0
c2=0
c3=0
c=1
while c<=2500000:
    v=int(input("digite 1 si desea votar por guillermo,digite 2 si desea votar por jorge digite 2,si desea votar  por Alejandro digite 3: "))
    if v==1:
        c1=c1+1
    if v==2:
        c2=c2+1
    if v==3:
        c3=c3+1
    c=c+1

if c1 > c2 and c1 > c3:
    n = c1
    g ="guillermo"
elif c2 > c1 and c2 > c3:
    n = c2
    g = "jorge"
else:
    n = c3
    g = "Alejandro"


print(f"El candidato {g} es el ganador con {n} votos de un total de {c} votos.")
"""5. reto"""

a=1
c=0
s=0
o=0
m=0
while a<=100:
    d=int(input("digite la calificacion del estudiante "))
    if d<50:
        c=c+1
    elif d>=50 and d<70:
        s=s+1
    elif d>=70 and d<80:
        o=o+1
    elif d>=80:
        m=m+1
    print(f"la cantidad de estudiantes que tienen una nota menor a 50 son {c}, entre 50 y 69 son {s}, entre 70 79 son {o} , superior o igual a 80 son {m}")
    a=a+1