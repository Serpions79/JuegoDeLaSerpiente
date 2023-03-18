class Personaje:
    nombre=""
    vida=15
    ataque_actual=0
    defensa_actual=0
    objetos=[]
    def __init__(self,nombre,vida,ataque_actual,defensa_actual,objetos):
        self.nombre = nombre
        self.vida = vida
        self.ataque_actual = ataque_actual
        self.defensa_actual = defensa_actual
        self.objetos = objetos
    def buscarObjeto(self,nombre):
        encontrado=0
        i=0
        while i<len(self.objetos) and encontrado==0:
            if self.objetos[i].nombre ==nombre:
                encontrado=1
            else:
                i=i+1
        if encontrado==1:
            return 1
        else:
            return 0