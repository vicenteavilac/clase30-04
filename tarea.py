print("Ingrese su numero de ticket:")
import time
num_ticket=int(input())

if num_ticket > 100 and num_ticket < 750:
 
 print("Su ticket es valido")
 time.sleep(1)
 print("Donde va?")
 time.sleep(1)
 print("Galeria (G) o Cancha (C)?")
 donde=input()
 if donde.upper() == "G":
        print("Usted va a la galeria, Disfrute!")
 elif donde.upper() == "C":
            print("Usted va a la cancha")
 else:
                print("No va a ningun lado")
else:
  print("Ticket maloo")