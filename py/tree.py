from anytree import Node, RenderTree

class Perfil:
    def __init__(self, nome, amigos=None):
        self.nome = nome
        self.amigos = amigos if amigos else []

def encontrar_amigos_em_comum(usuario, amigo_alvo):
    amigos_em_comum = set(usuario.amigos) & set(amigo_alvo.amigos)
    return amigos_em_comum

perfil1 = Perfil("João", ["Maria", "Carlos", "Ana", "Lucas"])
perfil2 = Perfil("Maria", ["João", "Ana", "Pedro", "Lucas"])
perfil3 = Perfil("Ana", ["João", "Maria", "Pedro", "Lucas"])
perfil4 = Perfil("Carlos", ["João", "Pedro", "Lucas"])
perfil5 = Perfil("Pedro", ["Maria", "Ana", "Carlos", "Lucas"])
perfil6 = Perfil("Lucas", ["João", "Maria", "Ana", "Carlos", "Pedro"])
perfil7 = Perfil("Laura", ["Maria", "Ana", "Lucas"])
perfil8 = Perfil("Mariana", ["João", "Pedro", "Lucas"])
perfil9 = Perfil("Eduardo", ["Ana", "Carlos", "Lucas"])
perfil10 = Perfil("Luisa", ["João", "Pedro", "Laura", "Mariana", "Lucas"])
perfil11 = Perfil("Rafael", ["Maria", "Ana", "Lucas"])

# Mudar essa linha para ver pessoas diferentes
amigos_em_comum = encontrar_amigos_em_comum(perfil2, perfil3)

# Essa também
print(f"Amigos em comum entre {perfil2.nome} e {perfil3.nome}:", amigos_em_comum)

def exibir_perfis_em_comum(usuario, amigo_alvo):
    amigos_em_comum = encontrar_amigos_em_comum(usuario, amigo_alvo)
    print("Perfis em comum entre", usuario.nome, "e", amigo_alvo.nome, ":")
    for amigo in amigos_em_comum:
        print(amigo)

# Mudar essa também
exibir_perfis_em_comum(perfil2, perfil3)
