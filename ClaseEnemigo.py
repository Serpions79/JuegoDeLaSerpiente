import random
class Enemigo:
    nombre=""
    vida=0
    ataque=0
    defensa=0
    def __init__(self,nombre,vida,ataque,defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        
def Combate(personaje,enemigos):
   turno_player = 1
   while True:   
       print("Tu vida actual es " + str (personaje.vida))
       indice_enemigos = 0
       if turno_player == 0:
           while indice_enemigos < len(enemigos):
               if enemigos[indice_enemigos].ataque > personaje.defensa_actual:
                   resultado = - personaje.defensa_actual + enemigos[indice_enemigos].ataque
                   personaje.vida = personaje.vida - resultado
                   print(enemigos[indice_enemigos].nombre + "Te ha atacado y te ha hecho " + str(resultado) + " de daño.")
               else:
                   print("No te ha hecho daño") 
               indice_enemigos=indice_enemigos + 1
           print("Te ha queado " + str (personaje.vida))
           turno_player = 1
       else:
          turno_player = 1
          print("Que quieres hacer? 1 para atacar, 2 para huir ")
          decision=int(input())
          if decision==1:
             if len(enemigos)>1:
              while indice_enemigos < len(enemigos):
                  print("A que enemigo prefieres atacar primero?")
                  print(enemigos[indice_enemigos].nombre)
                  indice_enemigos=indice_enemigos + 1
              decision=int(input())
              indice_enemigos=decision - 1
              resultado = personaje.ataque_actual - enemigos[indice_enemigos].defensa
              enemigos[indice_enemigos].vida = enemigos[indice_enemigos].vida - resultado
              turno_player = 0
              print("Has hecho " + str(resultado) + "de daño")
              print("La vida del" + str(enemigos[indice_enemigos].nombre) + " es de " + str(enemigos[indice_enemigos].vida)) 
             else:  
              resultado = personaje.ataque_actual - enemigos[indice_enemigos].defensa
              enemigos[indice_enemigos].vida = enemigos[indice_enemigos].vida - resultado
              turno_player = 0
              print("Has hecho " + str(resultado) + "de daño")
              print("La vida del" + str(enemigos[indice_enemigos].nombre) + " es de " + str(enemigos[indice_enemigos].vida)) 
             if (enemigos[indice_enemigos].vida) <= 0:
                print("Has acabo con " + (enemigos[indice_enemigos].nombre))
                enemigos.pop(indice_enemigos)
                if len(enemigos) == 0:
                    print("Felicidades has acabado con todos los enemigos :D")
                    break
          elif decision==2:
              numerorandom=random.uniform(0,100)
              if 20>=numerorandom:
                  print("Has escapado")
                  break
              else:
                  print("No has podido huir risas enlatadas")
                  turno_player = 0