
import os

USUARIOS = "usuarios.txt"
VIDEOS = "videos.txt"
FAVORITOS = "favoritos.txt"

def criar_arquivos():
    arquivos = [USUARIOS, VIDEOS, FAVORITOS]

    for arquivo in arquivos:
        if not os.path.exists(arquivo):
            with open(arquivo, "w", encoding="utf-8") as f:
                pass

    if os.path.getsize(VIDEOS) == 0:
        videos_exemplo = [
            "1;Breaking Bad;Serie;95",
            "2;Interestelar;Filme;88",
            "3;Stranger Things;Serie;76",
            "4;Matrix;Filme;67"
        ]

        with open(VIDEOS, "w", encoding="utf-8") as f:
            for video in videos_exemplo:
                f.write(video + "\\n")


def cadastrar_usuario():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    with open(USUARIOS, "a", encoding="utf-8") as f:
        f.write(f"{usuario};{senha}\\n")

    print("Usuário cadastrado com sucesso!")


def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    with open(USUARIOS, "r", encoding="utf-8") as f:
        for linha in f:
            dados = linha.strip().split(";")

            if dados[0] == usuario and dados[1] == senha:
                print("Login realizado com sucesso!")
                return usuario

    print("Usuário ou senha incorretos.")
    return None


def listar_videos():
    print("\\n=== LISTA DE VÍDEOS ===")

    with open(VIDEOS, "r", encoding="utf-8") as f:
        for linha in f:
            codigo, nome, tipo, curtidas = linha.strip().split(";")

            print(f"Código: {codigo}")
            print(f"Nome: {nome}")
            print(f"Tipo: {tipo}")
            print(f"Curtidas: {curtidas}")
            print("-" * 30)


def buscar_video():
    busca = input("Digite o nome do vídeo: ").lower()

    encontrado = False

    with open(VIDEOS, "r", encoding="utf-8") as f:
        for linha in f:
            codigo, nome, tipo, curtidas = linha.strip().split(";")

            if busca in nome.lower():
                encontrado = True

                print(f"\\nCódigo: {codigo}")
                print(f"Nome: {nome}")
                print(f"Tipo: {tipo}")
                print(f"Curtidas: {curtidas}")

    if not encontrado:
        print("Vídeo não encontrado.")


def curtir_video():
    codigo_busca = input("Digite o código do vídeo: ")

    videos = []

    with open(VIDEOS, "r", encoding="utf-8") as f:
        for linha in f:
            codigo, nome, tipo, curtidas = linha.strip().split(";")

            if codigo == codigo_busca:
                curtidas = str(int(curtidas) + 1)
                print("Vídeo curtido!")

            videos.append(f"{codigo};{nome};{tipo};{curtidas}")

    with open(VIDEOS, "w", encoding="utf-8") as f:
        for video in videos:
            f.write(video + "\\n")


def adicionar_favorito(usuario):
    codigo = input("Digite o código do vídeo favorito: ")

    with open(FAVORITOS, "a", encoding="utf-8") as f:
        f.write(f"{usuario};{codigo}\\n")

    print("Vídeo adicionado aos favoritos!")


def listar_favoritos(usuario):
    favoritos = []

    with open(FAVORITOS, "r", encoding="utf-8") as f:
        for linha in f:
            usuario_arq, codigo = linha.strip().split(";")

            if usuario_arq == usuario:
                favoritos.append(codigo)

    print("\\n=== FAVORITOS ===")

    with open(VIDEOS, "r", encoding="utf-8") as f:
        for linha in f:
            codigo, nome, tipo, curtidas = linha.strip().split(";")

            if codigo in favoritos:
                print(f"{codigo} - {nome} ({tipo})")


def menu_usuario(usuario):
    while True:
        print("\\n=== MENU DO USUÁRIO ===")
        print("1 - Listar vídeos")
        print("2 - Buscar vídeo")
        print("3 - Curtir vídeo")
        print("4 - Adicionar favorito")
        print("5 - Listar favoritos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_videos()

        elif opcao == "2":
            buscar_video()

        elif opcao == "3":
            curtir_video()

        elif opcao == "4":
            adicionar_favorito(usuario)

        elif opcao == "5":
            listar_favoritos(usuario)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def main():
    criar_arquivos()

    while True:
        print("\\n=== FEItv ===")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            usuario = login()

            if usuario:
                menu_usuario(usuario)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


main()
