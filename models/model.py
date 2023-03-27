from abc import ABC, abstractmethod
from typing import Type
from .model_Interface import ProdutoInterface, UsuarioInterface


class Pessoa(ABC):
    
    def __init__(self, nome: str, sexo: str, dataNasc: str, cpf: int) -> None:
        self.nome = nome
        self.sexo = sexo
        self.dataNasc = dataNasc
        self.__cpf = cpf
    
    def get_cpfPessoa(self) -> int:
        return self.__cpf

    @abstractmethod
    def apresentacao(self) -> None:
        pass


class Produto(ProdutoInterface):

    def __init__(self, nome: str, preco: float, descricao: str) -> None:
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao

    def descreve_produto(self) -> None:
        print(f"""
        Produto: {self.__nome} 
        Preço: {self.__preco}
        Descrição: {self.__descricao}
        """)

    def get_nome(self) -> str:
        return self.__nome
    
    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, novoPreco) -> None:
        self.__preco = novoPreco
        print('Preço novo salvo com sucesso!')


class Carrinho:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar(self, produto: Type[Produto]):
        self.__produtos.append(produto)
        print('Produto adicionado no carrinho!')

    def remover(self, idProduto: int):
        self.__produtos.remove(idProduto)
        print('Produto removido do carrinho!')
    
    def listar(self):
        for i in self.__produtos:
            print(i)





class Usuario(Pessoa, UsuarioInterface):

    def __init__(self, idUsuario: int, user: str, password: str, nome: str, sexo: str, dataNasc: str, cpf: int, carrinho: Type[Carrinho]) -> None:
        super().__init__(nome, sexo, dataNasc, cpf)
        self.__idUsuario = idUsuario
        self.__user = user
        self.__password = password
        self.carrinho = carrinho
    
    def apresentacao(self) -> None:
        print(f"""
        Nome: {self.nome}
        Sexo: {self.sexo}
        Data de Nascimento: {self.dataNasc}
        """)
    
    def get_cpf(self) -> None:
        if VerifUsuario.verifica(self, usuario=self):
            print(f'O CPF cadastrado é: {self.get_cpfPessoa()}')
        else:
            print("Dados Incorretos!")
    
    def get_idUsuario(self) -> None:
        if VerifUsuario.verifica(self, usuario=self):
            print(f'IdUsuario: {self.__idUsuario}')
        else:
            print("Dados incorretos")
    
    def get_User(self) -> str:
        return self.__user
    
    def get_Password(self) -> str:
        return self.__password
    
    def set_cpf(self, novoCPF: int) -> None:
        if VerifUsuario.verifica(self, usuario=self):
            self.__cpf = novoCPF
            print('CPF salvo com sucesso!')
        else:
            print('Dados incorretos')
    
    def set_idUsuario(self, novoID: int) -> None:
        if VerifUsuario.verifica(self, usuario=self):
            self.__idUsuario = novoID
            print('Id salvo com sucesso!')
        else:
            print('Dados incorretos!')
        

class VerifUsuario:

    def verifica(self, usuario: Type[Usuario]) -> bool:
        self.user = input("User: ")
        self.password = input("Password: ")

        if self.user == usuario.get_User() and self.password == usuario.get_Password():
            return True
        else:
            return False


