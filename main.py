from biblioteca.funcoes import Lojinha

lojinha = Lojinha()

while True:
    print("""
    -------------------------
    --- Lojinha Ecommerce ---
    -------------------------
        [0] - Exit()
        [1] - Fazer Cadastro
        [2] - Ver carrinho
        [3] - Ver dados
        [4] - Ver produtos
        [5] - Adicionar ao carrinho
    """)

    r = int(input('Digite uma opção: '))

    match r:
        case 0: 
            break
        case 1:
            lojinha.cadastro()
        case 2:
            lojinha.carrinho()
        case 3:
            lojinha.dados()
        case 4:
            lojinha.listar_produtos()
        case 5:
            lojinha.adicionar_carrinho()
        case _:
            print("[ERROR] Opção invalida!")
    


