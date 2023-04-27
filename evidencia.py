"""ejercicio 1"""
print(f"digite un numero")
c=int(input())
print(f"digite otro numero")
i=int(input())
if c==i:
    r=c*i
    print(f"el resultado es {r}")
if c>i:
    r=c-i
    print(f"el resultado es {r}")
if c<i:
    r=c+i
    print(f"el resultado es {r}")
"""ejercicio 2"""
print("digite el numero de computadoras")
c=int(input())
p=15000*c
if c<5:
    d=(p*100)/10
    p=d-p
    print(f"el precio a pagar es de {p}")
if c>=5 and c<10:
    d=(p*100)/20
    p=d-p
    print(f"el precio a pagar es de {p}")
if c>=10:
    d=(p*100)/40
    p=d-p
    print(f"el precio a pagar es de {p}")
"""ejercicio 3"""
print("digite el numero de llantas")
c=int(input())
if c<5:
    p=300
    t=p*c
    print(f"el precio total a pagar es de {t} y el valor de la llanta es de {p}")
if c>=5 and c<=10:
    p=250
    t=p*c
    print(f"el precio total a pagar es de {t} y el valor de la llanta es de {p}")
if c>=10:
    p=200
    t=p*c
    print(f"el precio total a pagar es de {t} y el valor de la llanta es de {p}")
"""ejercicio 4"""
print("¿Colon descubrió América?")
c=input()
if c=="si":
    print("¿La independencia de México fue en el año 1810?")
    c=input()
    if c=="si":
        print("¿The Doors fue un grupo de rock americano?")
        c=input()
        if c=="si":
            print("felicidades a ganado")
        else:
            print("ha perdido fin del juego")
    else:
        print("ha perdido fin del juego")
        
else:
    print("ha perdido fin del juego")
    """ejercicio 5"""
print(f"digite un numero")
c=int(input())
print(f"digite segundo numero")
i=int(input())
print(f"digite un tercer numero")
f=int(input())
if c<i<f or i<c<f:
    print(f"el numero mayor es {f}")
if f<c<i or c<f<i:
    print(f"el numero mayor es {i}")
if f<i<c or i<f<c:
    print(f"el numero mayor es {c}")
