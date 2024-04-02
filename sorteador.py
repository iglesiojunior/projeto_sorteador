import random
def main():
    #processo de abertura do arquivo e ao mesmo tempo fechamento dele com a partícula with:
    with open("relação_alunos.txt", "r", encoding="utf-8") as relação_nomes:
        menu = """
===============Sorteador 1.0 by Iglésio==================
1 - deletar alunos
2 - inserir quantidade de grupos e sortear
3 - Gerar Arquivo finalizado do sorteio dos grupos
=========================================================   
"""
        #parte responsável por deletar alunos:
        inserção_index = 1
        contador_qtd_remoções = -1 #explicado em vídeo o porque do índice -1
        lista_nomes = relação_nomes.readlines()
        #while usado para nova inserção de um index e remoção imediata dele da lista:
        while inserção_index != 0:
            inserção_index = (int(input("insira o número de chamada do aluno que você deseja retirar da lista(0 para sair): ")))
            if 1 <= inserção_index <= len(lista_nomes):
                if contador_qtd_remoções == -1:
                    lista_nomes.pop(inserção_index+contador_qtd_remoções)
                elif contador_qtd_remoções < -1:
                    lista_nomes.pop(inserção_index+contador_qtd_remoções)
                elif inserção_index == 1:
                    lista_nomes(inserção_index-1)#coloquei index-1 para possibilitar que o usuário coloque o número real da chamada, e não remova pelo número do index da lista!
                contador_qtd_remoções-=1
            elif inserção_index > len(lista_nomes):
                print("Número inválido, tente novamente: ")
                inserção_index = int(input("insira o número de chamada do aluno que você deseja retirar da lista(0 para sair): "))

        #parte responsável por dividir os grupos e misturar a lista:
        random.shuffle(lista_nomes)
        #parte que divide os grupos
        qtd_grupos = int(input("insira a quantidade de grupos que você deseja: "))
        tamanho_atual_lista = len(lista_nomes)
        tamanho_alunos_grupo = 0
        grupo_maior = 0
        if qtd_grupos%2 == 0:
            if tamanho_atual_lista%2 == 0:
                tamanho_alunos_grupo = tamanho_atual_lista//qtd_grupos
            else:
                tamanho_alunos_grupo = tamanho_atual_lista//qtd_grupos
                grupo_maior += tamanho_alunos_grupo+(tamanho_atual_lista%qtd_grupos)
        else:
            if tamanho_atual_lista%2 == 0:
                tamanho_alunos_grupo = tamanho_atual_lista//qtd_grupos
                grupo_maior += tamanho_alunos_grupo+(tamanho_atual_lista%qtd_grupos)
            else:
                tamanho_alunos_grupo = tamanho_atual_lista//qtd_grupos
                grupo_maior += tamanho_alunos_grupo+(tamanho_atual_lista%qtd_grupos)
        
        

        for linha in lista_nomes:
          print(linha, end="")
main()
