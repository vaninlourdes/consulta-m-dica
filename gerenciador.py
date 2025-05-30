class Gerenciador:
    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.consultas = []

    def cadastrar_medico(self, medico):
        self.medicos.append(medico)

    def cadastrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def remover_paciente(self, email):
        paciente_encontrado = None
        for paciente in self.pacientes:
            if paciente.email == email:
                paciente_encontrado = paciente
                break

        if paciente_encontrado:
            self.pacientes.remove(paciente_encontrado)

            consultas_a_remover = []
            for consulta in self.consultas:
                if consulta.get_paciente().email == email:
                    consultas_a_remover.append(consulta)

            for consulta in consultas_a_remover:
                self.consultas.remove(consulta)

    def remover_consulta(self, consulta):
        if consulta in self.consultas:
            self.consultas.remove(consulta)

    def consultar_pacientes(self):
        return self.pacientes

    def consultar_medicos(self):
        return self.medicos

    def cadastrar_consulta(self, consulta):
        self.consultas.append(consulta)

    def consultar_consultas(self):
        return self.consultas

    def login_medico(self, email, senha):
        for medico in self.medicos:
            if medico.email == email and medico.senha == senha:
                return medico
        return None

    def login_paciente(self, email, senha):
        for paciente in self.pacientes:
            if paciente.email == email and paciente.senha == senha:
                return paciente
        return None
