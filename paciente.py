from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, email, dt_nasc, telefone, tipo_sanguineo, senha):
        self.nome = nome
        self.email = email
        self.data_nascimento = dt_nasc
        self.telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Nascido(a): {self.data_nascimento}, Telefone: {self.telefone}, Tipo Sanguíneo: {self.tipo_sanguineo}."
