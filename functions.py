
def encontrar_amigos_em_comum(usuario, amigo_alvo):
    amigos_em_comum = set(usuario.amigos) & set(amigo_alvo.amigos)
    return amigos_em_comum


def exibir_perfis_em_comum(usuario, amigo_alvo):
    amigos_em_comum = encontrar_amigos_em_comum(usuario, amigo_alvo)
    print("Perfis em comum entre", usuario.nome, "e", amigo_alvo.nome, ":")
    for amigo in amigos_em_comum:
        print(amigo)
