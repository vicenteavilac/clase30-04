print("Bienvenido.!")
import time
valor_mensual = 300000

nombre = input("Ingrese su nombre: ")
if nombre == "Juan":
    print("¡Hola Juan!")
    time.sleep(2)
    print("Porfavor, Elija una carrera:")
    time.sleep(2)
    print("1- Ingenieria Comercial. (8 semestres)")
    time.sleep(1)
    print("2- Ingenieria Informatica. (10 semestres)")
    time.sleep(1)
    print("3- Odontologia. (6 semestres)")
    time.sleep(1)
    print("Valor mensual = $300.000")
    time.sleep(1)
    print("En semestres de 5 Meses")
    time.sleep(1)
    print("Si la carrera dura mas de 6 semestres se le hara descuento del 15%!!")
    time.sleep(1)
    carrera = input("Carrera que Desea Estudiar : ")
    if carrera == "1":
        time.sleep(2)
        print("Ha elegido Ingeniera Comercial que dura 4 Años. Suerte!")
        num1 = (40*valor_mensual)*0.15
        time.sleep(1)
        print("El valor de su carrera con el descuento aplicado es de: ", num1)
    if  carrera == "2":
        time.sleep(2)
        print("Ha elegido Ingeniera Informatica que dura 5 Años. Suerte!")
        num2 = (50*valor_mensual)*0.15
        time.sleep(1)
        print("El valor de su carrera con el descuento aplicado es de: ", num2)
    if carrera == "3":
        time.sleep(1)
        print("Ha elegido Odontologia que dura 3 Años. Suerte!")
        time.sleep(1)
        num3 = 30*valor_mensual
        print("El valor de su carrera es de: ", num3)
    if carrera == "":
        print("Elige una opcion")
