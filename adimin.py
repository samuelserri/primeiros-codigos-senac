opcao = 1
lista_produtos = []

while opcao != 5:
    print('------------------------MENU PRINCIPAL-------------------------')
    print('# 1. - CADASTRAR PRODUTOS #')
    print('# 2. - EDITAR PRODUTOS #')
    print('# 3. - EXCLUIR ITEM #')
    print('# 4. - LISTAR TODOS OS PRODUTOS DA LISTA #')
    print('# 5. - VENDA #')
    print('# 6. - SAIR DO SISTEMA')
    print('---------------------------------------------------------------')


    opcao = int(input('qual opção você deseja?:'))
    
    if opcao == 1:
        nome = str(input('insira o nome do produto:'))
        preco = float(input('insira o preço do produto:'))
        quantidade = int(input('insira a quantidade em estoque:'))


        produto = {
    'nome': nome,
    'preço': preco,
    'quantidade': quantidade


}

        
        lista_produtos .append(produto)

        posiçao = (len(lista_produtos))
        for i in range(len(lista_produtos)):
         print(i, lista_produtos[i])


    if opcao == 2:
       for i in range(len(lista_produtos)):
         print(i, lista_produtos[i])
       indice = int(input('qual indice da lista deseja editar:?'))    
       
       submenu = ''
       while submenu != 5:
           print('---------------------SUBMENU--------------------')
           print(print(i, lista_produtos[i]))
           print('# 1 - nome #')
           print('# 2 - preço #')
           print('# 3 - quantidade #')
           print('# 4 - voltar ao menu anterior #')
           print('-------------------------------------------------')

           submenu = int(input('qual opção do submenu acima?:'))

           if submenu == 1:
               nome_novo = input('qual o novo nome?:')
               lista_produtos[indice]['nome'] = nome_novo

               for i in range(len(lista_produtos)):
                 print(i, lista_produtos[i])

           if submenu == 2:
               preco_novo = input('qual o novo preço?:')
               lista_produtos[indice]['preço'] = preco_novo

               for i in range(len(lista_produtos)):
                 print(i, lista_produtos[i])
           
           if submenu == 3:
               quantidade_nova = input('qual a nova quantidade?:')
               lista_produtos[indice]['quantidade'] = quantidade_nova

               for i in range(len(i, lista_produtos+1)):
                print(i, lista_produtos[i])
           else:
             print('saiu do submenu')


    if opcao == 3:
          indice = int(input('qual indice da lista deseja excluir:?')) 
    
          lista_produtos.pop(indice)

          print(i, lista_produtos)

    if opcao == 4:
        posiçao = (len(lista_produtos))
        for i in range(posiçao):
          print(i, lista_produtos[i])

    if opcao == 5:
        print('voce saiu da lista, volte sempre')