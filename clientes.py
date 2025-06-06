class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, email, vlp):
        super().__init__(nome, idade)
        self.email = email
        self.vlp = float(vlp)


