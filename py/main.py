class Usuario:
    def __init__(self, id_usuario, nome):
        self.id_usuario = id_usuario
        self.nome = nome
        self.relacionamentos = []

    def adicionar_relacionamento(self, usuario):
        self.relacionamentos.append(usuario)

    def remover_relacionamento(self, id_usuario):
        self.relacionamentos = [
            user for user in self.relacionamentos if user.id_usuario != id_usuario]


class RedeSocial:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, id_usuario, nome):    
        if id_usuario not in self.usuarios:
            self.usuarios[id_usuario] = Usuario(id_usuario, nome)
        else:
            print(f"Usuário com ID {id_usuario} já existe.")

    def adicionar_relacionamento(self, id_usuario1, id_usuario2):
        if id_usuario1 in self.usuarios and id_usuario2 in self.usuarios:
            self.usuarios[id_usuario1].adicionar_relacionamento(
                self.usuarios[id_usuario2])
            self.usuarios[id_usuario2].adicionar_relacionamento(
                self.usuarios[id_usuario1])
        else:
            print("Um ou ambos os usuários não foram encontrados.")

    def remover_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for rel in usuario.relacionamentos:
                rel.remover_relacionamento(id_usuario)
            del self.usuarios[id_usuario]
        else:
            print(f"Usuário {id_usuario} não encontrado.")

    def buscar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario
        else:
            return None

    def exibir_relacionamentos(self):
        for usuario in self.usuarios.values():
            print(f"{usuario.nome} ({usuario.id_usuario})")
            for rel in usuario.relacionamentos:
                print(f"  -> {rel.nome} ({rel.id_usuario})")


def main():
    rede_social = RedeSocial()

    while True:
        print("\nMenu:")
        print("1. Adicionar usuário")
        print("2. Adicionar relacionamento")
        print("3. Remover usuário")
        print("4. Exibir relacionamentos")
        print("5. Buscar usuário")
        print("6. Sair")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            id_usuario = 0
            try:
                id_usuario = int(input("Digite o ID do novo usuário: "))
            except ValueError:
                print('Digite apenas números!')
            nome = input("Digite o nome do novo usuário: ")
            rede_social.adicionar_usuario(id_usuario, nome)
        elif escolha == '2':
            try:
                id_usuario1 = int(input("Digite o ID do primeiro usuário: "))
                id_usuario2 = int(input("Digite o ID do segundo usuário: "))
            except ValueError:
                print('Digite apenas números!')
            rede_social.adicionar_relacionamento(id_usuario1, id_usuario2)

        elif escolha == '3':
            try:
                id_usuario = int(input("Digite o ID do usuário a ser removido: "))
            except ValueError:
                print('Digite apenas números!')
            rede_social.remover_usuario(id_usuario)

        elif escolha == '4':
            rede_social.exibir_relacionamentos()

        elif escolha == '5':
            try:
                id_usuario = int(input("Digite o ID do usuário a ser buscado: "))
            except ValueError:
                print('Digite apenas números!')
            usuario = rede_social.buscar_usuario(id_usuario)
            if usuario:
                print(f"Usuário encontrado: { usuario.nome} ({usuario.id_usuario})")
                print("Relacionamentos:")
                for rel in usuario.relacionamentos:
                    print(f"  -> {rel.nome} ({rel.id_usuario})")
            else:
                print("Usuário não encontrado.")

        elif escolha == '6':
            break

        else:
            print("Escolha inválida. Tente novamente.")


main()
