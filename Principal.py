from ClaseArma import Arma
from ClasePersonaje import Personaje
from ClaseArmadura import Armadura
from ClaseEnemigo import Combate
from ClaseEnemigo import Enemigo

print("Dia: 17 de Agosto")
print("Hora: 21:56 pm")
print("Buenas ser humano")
print("Soy tu consciencia")
print("Hace mucho que no hablamos tu y yo")
print("La ultima vez fue cuando tenias como 4 años")
print("Hace tanto que hasta se me olvido tu nombre")

Nombre_del_personaje=input()

player=Personaje(Nombre_del_personaje,100,0,0,[],[],[])
Enemigos=[]
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
    decision=input()
    if decision=="1":
        print("Gracias por entenderme intentare no molestarte mucho en tu cabeza")
        break
    elif decision=="2":
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

while True:
    decision=input()
    if decision=="1":
        print("FUISTE A LA CASA")
        print("TE ENCONTRASTE UNA AK-47")
        print("Cogela nos servira util para cualquier mal que nos encontremos")
        player.armas.append(Arma("AK-47",10,0,7,5))
        print("Quieres ver si hay mas cosas " + Nombre_del_personaje + " ?")
        print("ESCOGE 1 PARA DECIR SÍ ESCOGE 2 PARA DECIR NO (PUDRETE)")
        while True:
            decision=input()
            if decision=="1":
                print("Has econtrado una ARMADURA DE MAYA")
                player.armaduras.append(Armadura("ARMADURA DE MAYA",5,4,1))
                break
            elif decision=="2":
                print("Vaya no recordaba que eras tan aburrido")
                break
            else: print("Bruh")
            print("ESCOGE 1 PARA DECIR SÍ ESCOGE 2 PARA DECIR NO (PUDRETE)")
        break
    elif decision=="2":
        print("FUISTE AL BUNKER ABANDONADO")
        print("TE ENCONTRASTE UNA REVOLVER")
        print("Cogela nos servira util para cualquier mal que nos encontremos")
        player.armas.append(Arma("REVOLVER",7,0,5,10))
        print("Quieres ver si hay mas cosas " + Nombre_del_personaje + " ?")
        print("ESCOGE 1 PARA DECIR SÍ ESCOGE 2 PARA DECIR NO (PUDRETE)")
        while True:
            decision=input()
            if decision=="1":
                print("No hemos encontrado nada mala suerte")
                break
            elif decision=="2":
                print("Ok mejor vamonos ya")
                break
            else: print("Bruh")
            print("ESCOGE 1 PARA DECIR SÍ ESCOGE 2 PARA DECIR NO (PUDRETE)")
        break
    else: print("Bruh")
    print("ESCOGE 1 PARA DECIR SÍ ESCOGE 2 PARA DECIR NO (PUDRETE)")
print("*15 minutos despues*")
print("Vaya parece que todos esos disparos ya se han acabado")
print("Veamos que ha pasado")
print("*sale del escondite*")
print("NO PUEDE SER, HAY UN MONTON DE CADAVERES")
print("Esto no es normal")
print("Estamos en el barrio Weberly una zona muy tranquila")
print("Quieres investigar que ha pasado o seguimos el camino?")
print("ESCOGE 1 PARA INVESTIGAR ESCOGE 2 PARA CONTINUAR EL CAMINO")
while True:
    decision=input()
    if decision=="1":
        print("Veamos que hay en esos cadaveres de alla")
        print("Parece que tienen una marca en ellos")
        print("*Escuchas un rugido de una especie de animal peligroso")
        print("CORRE SALGAMOS ANTES DE QUE ESA COSA VENGA A POR NOSOTROS")
        print("*corres hacia el bosque para despistar a la bestia*")
        break
    elif decision=="2":
        print("Ok sigamos el camino")
        print("*te tropiezas con una piedra y te quedas incosciente*")
        print("Parece que te has quedado dormido y ya es de noche")
        print("Estamos en una especie de bosque")
        break
    else: print("Bruh")
    print("ESCOGE 1 PARA DECIR SÍ ESCOGE 2 PARA DECIR NO (PUDRETE)")
print("Vayamos a esa cueva parece segura para pasar la noche")
print("*Avanzas epicamente por la cueva*")
print("La cueva se divide en 2")
print("¿Por donde quieres ir?")
print("ESCOGE 1 PARA IR A LA IZQUIERDA ESOCGE 2 PARA IR A LA DERECHA")
while True:
    decision=input()
    if decision=="1":
        print("*Sigas caminando epicamente y te encuentras a un OSO HORMIGUERO")
        Enemigos.append(Enemigo("OSO HORMIGUERO",10,1,2))
        print("EMPIEZA EL COMBATE")
        Combate(player,Enemigos)
    elif decision=="2":
        print("*Sigas caminando epicamente y te encuentras a un BHUO DE 1 METRO")
        Enemigos.append(Enemigo("BHUO DE 1 METRO",10,1,2))
        print("EMPIEZA EL COMBATE")
        Combate(player,Enemigos)
        print("EPIEZA EL COMBATE")
    else: print("Bruh")
    print("ESCOGE 1 PARA IR A LA IZQUIERDA ESOCGE 2 PARA IR A LA DERECHA")

        