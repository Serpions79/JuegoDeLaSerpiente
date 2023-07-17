class Personaje:
    nombre=""
    vida=50
    ataque_actual=0
    defensa_actual=0
    objetos=[]
    armas=[]
    amraduras=[]
    def __init__(self,nombre,vida,ataque_actual,defensa_actual,objetos,armas,armaduras):
        self.nombre = nombre
        self.vida = vida
        self.ataque_actual = ataque_actual
        self.defensa_actual = defensa_actual
        self.objetos = objetos
        self.armas = armas
        self.armaduras = armaduras
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
    
    def equiparArma(self,nombre,):
        equipacion=0
        i=0
        while i<len(self.armas) and equipacion==0:
            if self.armas[i].nombre ==nombre:
                equipacion=1
            else:
                i=i+1
        if equipacion==1:
            self.ataque_actual=self.ataque_actual + self.armas[i].ataque
            return 1
        else:
            return 0
    def equiparArmadura(self,nombre,):
        equipacion=0
        i=0
        while i<len(self.armaduras) and equipacion==0:
            if self.armaduras[i].nombre ==nombre:
                equipacion=1
            else:
                i=i+1
        if equipacion==1:
            self.defensa_actual=self.defensa_actual + self.armaduras[i].defensa
            return 1
        else:
            return 0