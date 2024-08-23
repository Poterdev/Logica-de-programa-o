# Impressão do menu
print('---------Olá, meu nome é Erickson(4640380)---------')
print('------------Este programa irá auxiliar-------------')
print('-------     no cadastro do seus livros    -------\n')

# Função para cadastrar um livro
def cadastrar_livro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)

# Função para consultar livros
def consultar_livro():
    print("1. Consultar Todos")
    print("2. Consultar por Id")
    print("3. Consultar por Autor")
    print("4. Retornar ao menu")
    
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                if lista_livro:
                    print("Lista de todos os livros:")
                    for livro in lista_livro:
                        print(livro)
                else:
                    print("Não há livros cadastrados.")
                break
            elif opcao == 2:
                try:
                    id_consulta = int(input("Digite o ID do livro a ser consultado: "))
                    for livro in lista_livro:
                        if livro['id'] == id_consulta:
                            print("Livro encontrado:")
                            print(livro)
                            return
                    print("Livro não encontrado.")
                    break
                except ValueError:
                    print("Por favor, digite um número inteiro para o ID do livro.")
            elif opcao == 3:
                autor_consulta = input("Digite o nome do autor a ser consultado: ")
                encontrados = False  # Inicializa a variável encontrados
                for livro in lista_livro:
                    if livro['autor'] == autor_consulta:
                        print("Livro encontrado:")
                        print(livro)
                        encontrados = True
                if not encontrados:
                    print("Livro não encontrado para o autor especificado.")
                break
            elif opcao == 4:
                return
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Por favor, digite um número inteiro para a opção.")



# Função para remover livro
def remover_livro():
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido (ou digite 0 para cancelar): "))
            if id_remover == 0:
                print("Operação cancelada. Retornando ao menu principal.")
                return
            encontrado = False
            for livro in lista_livro:
                if livro['id'] == id_remover:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso.")
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado na lista.")
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido para o ID do livro.")


# Função principal do programa
def main():
    while True:
        print("Bem-vindo ao sistema de gerenciamento de livros")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            global id_global
            id_global += 1
            cadastrar_livro(id_global)
        elif opcao == '2':
            consultar_livro()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            main()
            break
        else:
            print("Opção inválida.")


# Lista vazia para armazenar os livros e variável global para controlar o ID
lista_livro = []
id_global = 0

main()



