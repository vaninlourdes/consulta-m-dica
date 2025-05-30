class Pessoa:
    def __init__(self, nome, email, dt_nasc):
        self.nome = nome
        self.email = email
        self.data_nascimento = dt_nasc

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Nascido(a): {self.data_nascimento}."

    def get_nome(self):
        return self.nome
