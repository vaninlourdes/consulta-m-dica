from medico import Medico
from paciente import Paciente
from consulta import Consulta
from gerenciador import Gerenciador

def exibir_lista_com_indices(lista):
    for i in range(len(lista)):
        print(f"{i} - {lista[i]}")

def selecionar_item(lista, mensagem):
    try:
        indice = int(input(mensagem))
        return lista[indice]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return None

def menu_medico(sistema, medico_logado):
    while True:
        print("\n--- Menu Médico ---")
        print("1. Cadastrar Paciente\n2. Ver Pacientes\n3. Agendar Consulta\n4. Ver Consultas")
        print("5. Remover Paciente\n6. Cancelar Consulta\n7. Logout")
        opc = input("Escolha: ")

        if opc == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            nasc = input("Nascimento: ")
            tel = input("Telefone: ")
            ts = input("Tipo Sanguíneo: ")
            senha = input("Senha: ")
            sistema.cadastrar_paciente(Paciente(nome, email, nasc, tel, ts, senha))

        elif opc == "2":
            exibir_lista_com_indices(sistema.consultar_pacientes())

        elif opc == "3":
            data = input("Data: ")
            hora = input("Hora: ")
            pacientes = sistema.consultar_pacientes()
            if not pacientes:
                print("Nenhum paciente cadastrado.")
                continue
            exibir_lista_com_indices(pacientes)
            paciente = selecionar_item(pacientes, "Escolha o paciente: ")
            if paciente:
                sistema.cadastrar_consulta(Consulta(data, hora, medico_logado, paciente))

        elif opc == "4":
            exibir_lista_com_indices(sistema.consultar_consultas())

        elif opc == "5":
            email = input("Email do paciente: ")
            sistema.remover_paciente(email)

        elif opc == "6":
            consultas = []
            for c in sistema.consultar_consultas():
                if c.get_medico().email == medico_logado.email:
                    consultas.append(c)
            if not consultas:
                print("Nenhuma consulta para cancelar.")
                continue
            exibir_lista_com_indices(consultas)
            consulta = selecionar_item(consultas, "Escolha a consulta a cancelar: ")
            if consulta:
                sistema.remover_consulta(consulta)

        elif opc == "7":
            break
        else:
            print("Opção inválida.")

def menu_paciente(sistema, paciente_logado):
    while True:
        print("\n--- Menu Paciente ---")
        print("1. Ver Minhas Consultas\n2. Cancelar Minhas Consultas\n3. Logout")
        opc = input("Escolha: ")

        if opc == "1" or opc == "2":
            consultas = []
            for c in sistema.consultar_consultas():
                if c.get_paciente().email == paciente_logado.email:
                    consultas.append(c)
            if not consultas:
                print("Nenhuma consulta encontrada.")
                continue
            if opc == "1":
                exibir_lista_com_indices(consultas)
            else:
                exibir_lista_com_indices(consultas)
                consulta = selecionar_item(consultas, "Qual deseja cancelar? ")
                if consulta:
                    sistema.remover_consulta(consulta)

        elif opc == "3":
            break
        else:
            print("Opção inválida.")

def main():
    sistema = Gerenciador()
    while True:
        print("\n--- Sistema ---")
        print("1. Login Médico\n2. Login Paciente\n3. Cadastrar Médico\n4. Sair")
        opc = input("Escolha: ")

        if opc == "1":
            email = input("Email: ")
            senha = input("Senha: ")
            medico = sistema.login_medico(email, senha)
            if medico:
                print("Login realizado.")
                menu_medico(sistema, medico)
            else:
                print("Login inválido.")

        elif opc == "2":
            email = input("Email: ")
            senha = input("Senha: ")
            paciente = sistema.login_paciente(email, senha)
            if paciente:
                print("Login realizado.")
                menu_paciente(sistema, paciente)
            else:
                print("Login inválido.")

        elif opc == "3":
            nome = input("Nome: ")
            email = input("Email: ")
            nasc = input("Nascimento: ")
            crm = input("CRM: ")
            esp = input("Especialidade: ")
            senha = input("Senha: ")
            sistema.cadastrar_medico(Medico(nome, email, nasc, crm, esp, senha))

        elif opc == "4":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
