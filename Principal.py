from ClaseArma import Arma
from ClasePersonaje import Personaje

print("Dia: 17 de Agosto")
print("Hora: 9:38 am")
print("Buenos dias persona")
print("Soy tu consciencia")
print("Hace mucho que no hablamos tu y yo")
print("La ultima vez fue cuando tenias como 4 años")
print("Hace tanto que hasta se me olvido tu nombre")

Nombre_del_personaje=input()

player=Personaje(Nombre_del_personaje,100,0,0,[],[])

print("Es verdad cuanto tiempo " +  Nombre_del_personaje + ", espero que estes tan bien como estoy yo")
print(Nombre_del_personaje + ", si estoy aqui hablando contigo es que algo malo ha ocurrido recuerda lo que nos dijo el tio Ben")
print("Si comes lechugas te convertiras en un superheroe")
print("A espera eso no")
print("Si escuchas una voz en tu cabeza debes de ir a mi antigua casa situada en la Isla Mauricio lo entenderas cuando sea el momento idoneo")
print("Entonces...")
print("Ya sabemos que hacer...por asi decirlo")
print("Oye yo soy tu consciencia y como tal seguramente hare unas preguntas en el viaje")
print("No hay problema no?")
print("ESCOGE 1 PARA DECIR SÍ ESCOGE 2 PARA DECIR NO (PUDRETE)")

while True:
    decision=int(input())
    if decision==1:
        print("Gracias por entenderme intentare no molestarte mucho en tu cabeza")
        break
    elif decision==2:
        print("Perdon...")
        break
    else: print("Bruh")
    print("ESCOGE 1 PARA DECIR SÍ ESCOGE 2 PARA DECIR NO (PUDRETE)")

print("5 MINUTOS DESPUES")
print("Ok creo que la casa del tio Ben estaba a la derecha")
print("*Se escucha un tiroteo*")
print("Ladron Herido: *Se acerca*, Ayuda porfavor no quiero estar aqui")
print("Ladron Herido: *Recibe un disparo en la cabeza*")
print("Corre " + Nombre_del_personaje + " hay que salir de aqui cuanto antes")
print("Hay una casa que parece bastante segura, pero tambien esta esa especie de bunker antiguo parece que no hay nadie dentro")
print("A cual deberiamos ir para estar a salvo")
print("ESCOGE 1 PARA IR A LA CASA, ESCOGE 2 PARA IR AL BUNKER ABANDONADO")
decision=int(input())
if decision==1:
    print("FUISTE A LA CASA")
    print("TE ENCONTRASTE UNA AK-47")
    print("Cogela nos servira util para cualquier mal que nos encontremos")
    player.armas.append(Arma("AK-47",10,5,7,4))
elif decision==2:
    print("FUISTE AL BUNKER ABANDONADO")
    print("TE ENCONTRASTE UNA REVOLVER")
    print("Cogela nos servira util para cualquier mal que nos encontremos")
    player.armas.append(Arma("REVOLVER",7,8,5,10))

print("20 MINUTOS DESPUES")
