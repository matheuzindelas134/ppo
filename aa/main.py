class Motos:
    def __init__(self,marca, modelo, cilindradas, cor):
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas
        self.cor = cor
        
    def ligar(self):
        return f"A moto {self.modelo} ligou"
    
    def ver_informacoes(self):
        return f"""
        MARCA: {self.marca}
        MODELO: {self.modelo}
        CILINDRADAS: {self.cilindradas}
        COR: {self.cor}
    """


modelo1 = Motos(marca="honda",cor= "vermelha",modelo ="CG TITAN", cilindradas = "160" )
modelo2 = Motos(marca="honda",cor="chumbo", modelo ="CG FAN", cilindradas = "160" )
modelo3 = Motos(marca="honda",cor="prata", modelo ="CG START", cilindradas = "150" )

print(modelo1.ligar())
print(modelo2.ligar())
print(modelo3.ligar())

print(modelo2.ver_informacoes)



print(f"""
    Marca da primeira moto: {modelo1.marca}

    Marca da segunda moto: {modelo2.cilindradas}
    Cor da segunda moto: {modelo2.cor}

    Marca da terceira moto: {modelo3.marca}
    Cor da terceira moto: {modelo3.cor}
    Cilindradas da terceira moto: {modelo3.cilindradas}
#""")