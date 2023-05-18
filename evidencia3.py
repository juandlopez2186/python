"""1.reto """
m=int(input("Digite el valor de la casa"))
d=int(input("Digite el valor de la inversion"))
if m<1000000:
    m=(d/2)
    print(f"su socio y usted deben pagar {m} cada uno")
elif m>=1000000:
    m=d-m
    m=(m/2)
    print(f"su socio y usted deben pagar {m} cada uno")
    
"""2.reto """
m=int(input("Digite el numero de hectarias"))
m=m*10000
if m>1000000:
    m=(m*70)/100
    print(f"debe plantar {m} metros cuadrados de pinos")
    m=(m*20)/100
    print(f"debe plantar {m} metros cuadrados de oyamel")
    m=(m*10)/100
    print(f"debe plantar {m} metros cuadrados de cedro")
elif m<=1000000:
    m=(m*50)/100
    print(f"debe plantar {m} metros cuadrados de pinos")
    m=(m*30)/100
    print(f"debe plantar {m} metros cuadrados de oyamel")
    m=(m*20)/100
    print(f"debe plantar {m} metros cuadrados de cedro")

"""3.reto """

t1=0
t2=0
t3=0
t4=0
c1=0
c2=0
c3=0
c4=0
p1=0
p2=0
p3=0
p4=0
c=1
while c<=10:
    m=int(input("Digite la edad"))
    if m>=0 and m<=12:
        p=int(input("digite su peso "))
        p1=p1+p
        c1=c1+1
        t1=(p1*c1)/100
        c=c+1
    elif m>=13 and m<=29:
        p=int(input("digite su peso "))
        p2=p2+p
        c2=c2+1
        t2=(p2*c2)/100
        c=c+1
    elif m>=30 and m<=59:
        p=int(input("digite su peso "))
        p3=p3+p
        c3=c3+1
        t3=(p3*c3)/100
        c=c+1
    elif m>=60:
        p=int(input("digite su peso "))
        p4=p4+p
        c4=c4+1
        t4=(p4*c4)/100
        c=c+1
print(f"el promedio de peso en niños es de {t1} en jovenes {t2} en adultos {t3} y en viejos {t4}")
        
"""5.reto """

c=1
m=int(input("Digite la cant de obreros "))
while c<=m:
    h=int(input("Digite la cant de horas trabajadas "))
    if h<=40:
        h=h*20
        print(f"el empleado recibe ${h} por sus horas trabajadas  ")
        c=c+1
    elif h>=40 :
        h=h-40
        h=h*25
        print(f"el empleado recibe $800 por sus primeras 40 horas trabajadas y un bono de ${h} por sus horas extra ")
        c=c+1        
        
"""5.reto """

m=int(input("Digite la edad"))
if m>=5 and m<=14:
    t=(10000*35)/100
    t=10000-t
    print(f"el precio del boleto es de {t}")
elif m>=15 and m<=19:
    t=(10000*25)/100
    t=10000-t
    print(f"el precio del boleto es de {t}")
elif m>=20 and m<=45:
    t=(10000*10)/100
    t=10000-t
    print(f"el precio del boleto es de {t}")
elif m>=46 and m<=65:
    t=(10000*25)/100
    t=10000-t
    print(f"el precio del boleto es de {t}")
elif m>=66:
    t=(10000*35)/100
    t=10000-t
    print(f"el precio del boleto es de {t}")