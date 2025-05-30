class Consulta:
    def __init__(self, data, horario, medico, paciente):
        self.data = data
        self.horario = horario
        self.medico = medico
        self.paciente = paciente

    def __str__(self):
        return f"Consulta em {self.data}, às {self.horario} com o Dr(a). {self.medico.nome} para o paciente {self.paciente.nome}."

    def get_paciente(self):
        return self.paciente

    def get_medico(self):
        return self.medico
