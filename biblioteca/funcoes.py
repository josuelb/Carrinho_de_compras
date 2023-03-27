from models.model import Produto, Usuario, Carrinho

class Lojinha:
    def __init__(self) -> None:
        self.usuario = None
        self.produtos = [Produto('Hide', 34.70, 'Caderno de 160 paginas - 10 matérias'), Produto('Molde de fotos', 70.00, 'Molde de fotos de madeira')]

    def listar_produtos(self) -> None:
        print('---- Produtos ----')
        for i in self.produtos:
            i.descreve_produto()
        
    def cadastro(self) -> None:
        user = input('Digite seu User: ').strip()
        password = input('Digite a password: ').strip()
        nome = input('Digite seu nome completo: ').strip()
        sexo = input('Digite seu sexo: [M/F] ').strip()[0]
        dataNasc = input('Digite sua data de nascimento: [dd/mm/aaaa] ').strip()
        cpf = int(input('Digite seu cpf: '))
        carrinho = Carrinho()

        self.usuario = Usuario(1, user, password, nome, sexo, dataNasc, cpf, carrinho)
        
    def carrinho(self) -> None:
        self.usuario.carrinho.listar().__dict__
    
    def adicionar_carrinho(self) -> None:
        while True:
            self.listar_produtos()
            produto = input('Qual produto deseja adcionar ao carrinho? [0 - exit()] ')
            for i in self.produtos:
                if produto == i.get_nome():
                    self.usuario.carrinho.adicionar(produto=i)

            if produto == '0':
                break
    def dados(self) -> None:
        self.usuario.apresentacao()
        while True:
            print("""
            Digite:
                [1] - Ver CPF
                [2] - Ver idUsuario
                [3] - Alterar o CPF
                [4] - Exit()
            """)

            doc = int(input('Deseja ver algum documento a mais? '))

            match doc:
                case 1:
                    self.usuario.get_cpf()
                case 2:
                    self.usuario.get_idUsuario()
                case 3:
                    novoCPF = input('Novo CPF: ')
                    self.usuario.set_cpf(novoCPF=novoCPF)
                case 4: 
                    break
            
    
