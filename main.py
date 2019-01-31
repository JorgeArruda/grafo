# -*- coding: utf-8 -*-
# Autor: Jorge de Arruda Martins

def print_lista(lista):
    string = ''
    for x in range(len(lista)):
        string += str(lista[x][0]) + ' -> '
        for y in range(len(lista[x][1])):
            string += str(lista[x][1][y]) + ' '
        string += '\n'
    print(string)

def print_matriz(matriz):
    string = ''
    for x in range(len(matriz)):
        string += str(x) + ' - '
        for y in range(len(matriz[x])):
            string += matriz[x][y] + '    '
        string += '\n'
    print(string)

def lista_adj(entrada):
    n_vert, arestas = (entrada[0], entrada[2])

    saida = []
    for x in range(n_vert):
        saida.append([x, []])
    for a in arestas:
        saida[a[0]][1].append(a[1])
    return saida

def matriz_adj(entrada):
    n_vert, n_arestas, arestas = (entrada[0], entrada[1], entrada[2])
    saida = []
    for x in range(n_vert):
        saida.append([])
        for y in range(n_vert):
            saida[x].append('0')
    for a in arestas:
        saida[a[0]][a[1]] = '1'
    return saida

def matriz_inc(entrada):
    n_vert, n_arestas, arestas = (entrada[0], entrada[1], entrada[2])
    saida = []
    for x in range(n_vert):
        saida.append([])
        for y in range(len(arestas)):
            saida[x].append(' 0')
    c = 0
    for a in arestas:
        if a[0] != a[1]:
            saida[a[0]][c] = ' 1'
            saida[a[1]][c] = '-1'
        else:
            saida[a[0]][c] = ' 1'
        c += 1
    return saida

if __name__ == '__main__':
    # entrada = [3, 3,  [(0, 0), (1, 2), (2, 0), (2, 1)]]
    entrada = [6, 8,  [(0, 3), (0, 1), (3, 1), (4, 3), (1, 4), (2, 4), (2, 5), (5, 5)]]
    n_alt = True
    opcao = '1'
    while str(opcao) != '0':
        print("   -   Alterar   -")
        print("1 Entrar com N de vértices e arestas")
        print("2 Adicionar aresta")
        print("   -   Mostrar   -")
        print("3 Listas de Adjacência")
        print("4 Matriz de Adjacência")
        print("5 Matriz de Incidência")
        opcao = str(input('Opção: '))

        
        print(opcao)

        if str(opcao) == '1':
            print('\n')
            entrada[0] = int(input('N de vértices: '))
            entrada[1] = int(input('N de arestas: '))
        elif str(opcao) == '2':
            entrada[2] = [] if n_alt else entrada[2]
            n_alt = False
            arestas = entrada[2]
            print('\nEntre com uma tupla: a->b')
            temp = str(input('Aresta: '))
            a, b = temp.split('->')
            arestas.append((int(a), int(b)))
            entrada[2] = arestas
            pass
        elif str(opcao) == '3':
            print('\n')
            saida = lista_adj(entrada)
            print('   -   Listas de Adjacência   -')
            print_lista(saida)
            input('\nDigite algo para continuar  ')
            pass
        elif str(opcao) == '4':
            print('\n')
            saida = matriz_adj(entrada)
            print('   -   Matriz de Adjacência (vértices X vértices)   -')
            print_matriz(saida)
            input('\nDigite algo para continuar  ')
            pass
        elif str(opcao) == '5':
            print('\n')
            saida = matriz_inc(entrada)
            print('   -   Matriz de Incidência (vértices X arestas)   -')
            print_matriz(saida)
            input('\nDigite algo para continuar  ')
            pass
        print('\n\n\n\n')
    pass
