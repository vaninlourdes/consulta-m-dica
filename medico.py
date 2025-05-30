from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, email, dt_nasc, crm, especialidade, senha):
        self.nome = nome
        self.email = email
        self.data_nascimento = dt_nasc
        self.crm = crm
        self.especialidade = especialidade
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Nascido(a): {self.data_nascimento}, CRM: {self.crm}, Especialidade: {self.especialidade}."

    def get_crm(self):
        return self.crm
