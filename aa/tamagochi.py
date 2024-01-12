class tamagotchi:
    def __init__(self,nome ,especie, energia):
        self.nome = nome
        self.especie = especie
        self.energia = energia 
    
    def brincar(self):
        if self.energia >= 5:
            self.energia = self.energia - 5
        else:
            print("muita fome rolando aqui")
        
        return self.energia
    
    def comer(self):
        if self.energia <= 95:
            self.energia = self.energia + 5
        else:
            print(" buxo cheio")
        return self.energia
    
tamagotchi = tamagotchi(nome ="xingulingo", especie="aquatica", energia = 100)

while True:
    menu = int(input("""
    Escolha uma opcao 
    1 - BRINCAR 
    2 - COMER 
    0 - SAIR
"""))
    match menu:
        case 1:
            tamagotchi.brincar()
        case 2:
            tamagotchi.comer()
        case 0:
            break
        case _:
            print("Opcao invalida")

    print(f"energia atual: {tamagotchi.energia}")
