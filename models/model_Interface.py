from abc import ABC, abstractmethod

class ProdutoInterface(ABC):
    @abstractmethod
    def descreve_produto(self) -> None:
        pass

    @abstractmethod
    def get_nome(self) -> str:
        pass

    @abstractmethod
    def get_preco(self) -> float:
        pass

    @abstractmethod
    def set_preco(self) -> None:
        pass


class UsuarioInterface(ABC):

    @abstractmethod
    def get_cpf(self) -> None:
        pass

    @abstractmethod
    def get_idUsuario(self) -> None:
        pass

    @abstractmethod
    def get_User(self) -> str:
        pass

    @abstractmethod
    def get_Password(self) -> str:
        pass

    @abstractmethod
    def set_cpf(self) -> None:
        pass

    @abstractmethod
    def set_idUsuario(self) -> None:
        pass
