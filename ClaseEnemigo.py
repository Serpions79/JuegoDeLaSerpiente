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
       num_enemigos = 0
       if turno_player == 0:
           while num_enemigos < len(enemigos):
               if enemigos[num_enemigos].ataque > personaje.defensa_actual:
                   resultado = - personaje.defensa_actual + enemigos[num_enemigos].ataque
                   personaje.vida = personaje.vida - resultado
                   print(enemigos[num_enemigos].nombre + "Te ha atacado y te ha hecho " + str(resultado) + " de daño.")
               else:
                   print("No te ha hecho daño") 
               num_enemigos=num_enemigos + 1
           print("Te ha queado " + str (personaje.vida))
           turno_player = 1
       else:
          turno_player = 1
          print("Que quieres hacer? 1 para atacar, 2 para huir ")
          decision=int(input())
          if decision==1:
              print("Ataque")
          elif decision==2:
              numerorandom=random.uniform(0,100)
              if 20>=numerorandom:
                  print("Has escapado")
                  break
              else:
                  print("No has podido huir *risas enlatadas*")
                  turno_player = 0