class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def apresentacao(self):
        print(f"O {self.modelo} pertence a marca {self.marca}. Ele é do ano {self.ano} e tem velociade de {self.velocidade}")

    def quantidade(self, quantos, cm, rodas):
        print(f"O {self.modelo} possui {quantos} cavalos, {cm}cm e {rodas} rodas")


carro1 = Carro("Volkswagen", "Fusca", 1995, "210km/h")
carro2 = Carro("Ferrari", "F40", 1995, "270km/h")
carro3 = Carro("Mustang", "Camaro", 1980, "250km/h")


carro3.apresentacao()
carro3.quantidade(450, 180, 4)