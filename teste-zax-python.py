# Autor: Gabriel Rosa Stork
import random


class Motoboy:
    """
    Classe para representar os motoboys.

    Parâmetros
    ----------
    id_ : int
        O número identificador do motoboy.
    preco : int
        O preço cobrado pela entrega.
    exclusivas : list
        Quais as lojas são exclusivas do motoboy (caso não exista, será
        atribuído o valor True a _todas_lojas, indicando que o motoboy pode
        pegar pedidos em todas as lojas).
    """
    def __init__(self, id_: int, preco: int, exclusivas: list = []) -> None:
        self.id_ = id_
        self.preco = preco
        self.exclusivas = exclusivas

        if len(self.exclusivas) > 0:
            self._todas_lojas = False
        else:
            self._todas_lojas = True

        self._dinheiro = 0
        self._pedidos = []

    def __str__(self) -> str:
        """
        A partir da lista de pedidos de um motoboy, cria uma lista de strings
        detalhando todos os pedidos em ordem de entrega (número do pedido da
        loja, loja do pedido e valor a ser recebido). Além de informar o
        número do motoboy e quanto dinheiro ele ganhará no total.

        Retornos:
        --------
        info : str
            Informações necessárias de um motoboy.
        """
        pedidos = [
            (
                f'- Entrega {pedido[0]}: Pedido {pedido[1][1]} da Loja '
                f'{pedido[1][0]} (R${self.preco} + R${pedido[1][2]})\n'
            )
            for pedido in enumerate(self._pedidos, 1)
        ]

        info = (
            f'\nMotoboy número {self.id_} possui {len(self._pedidos)} '
            f'pedido(s)\n{"".join(pedidos)}Vai ganhar: R${self._dinheiro}\n'
        )

        return info


class Loja:
    """
    Classe para representar as lojas.

    Parâmetros
    ----------
    id_ : int
        O número identificador da loja.
    pedidos : list
        O valor de cada pedido (em ordem) a ser entregue a um motoboy.
    porcentagem : int
        A porcentagem do valor do pedido a ser pago ao motoboy.
    """
    def __init__(self, id_: int, pedidos: list, porcentagem: int) -> None:
        self.id_ = id_
        self.pedidos = list(enumerate(pedidos, 1))
        self.porcentagem = porcentagem

    def entregar_pedido(self, motoboy: Motoboy) -> None:
        """
        Entrega o primeiro pedido da lista ao motoboy especificado, sempre
        respeitando as exclusividades. Caso não haja mais pedido a ser entregue,
        a loja é retirada da lista.

        Parâmetros
        ----------
        motoboy : Motoboy
            O motoboy a quem será entregue o pedido.
        """
        if motoboy._todas_lojas or self in motoboy.exclusivas:
            pedido = self.pedidos.pop(0)
            pagamento = (pedido[1] * (self.porcentagem / 100))

            motoboy._dinheiro += motoboy.preco + pagamento
            motoboy._pedidos.append([self.id_, pedido[0], pagamento])

            if len(self.pedidos) == 0:
                lojas.remove(self)


def adicionar_objetos() -> tuple[list, list]:
    """
    Instancia os objetos de cada classe (como especificados no teste) dentro de
    listas.

    Retornos:
    --------
    lojas : list
        Lista dos objetos da classe Loja.
    motoboys : list
        Lista dos objetos da classe Motoboy.
    """
    lojas = [
        Loja(1, [50, 50, 50], 5),
        Loja(2, [50, 50, 50, 50], 5),
        Loja(3, [50, 50, 100], 15),
    ]

    motoboys = [
        Motoboy(1, 2),
        Motoboy(2, 2),
        Motoboy(3, 2),
        Motoboy(4, 2, [lojas[0]]),
        Motoboy(5, 3),
    ]

    return lojas, motoboys


def distribuir_pedidos() -> None:
    """
    Enquanto ainda houverem pedidos, uma loja aleatória entrega o próximo
    pedido da fila a um motoboy aleatório (motoboys com exclusividades sempre
    pegam o primeiro pedido das(s) loja(s) em que tem prioridade(s)).
    """
    prioridades = [(motoboy, motoboy.exclusivas) for motoboy in motoboys]

    for prioridade in prioridades:
        for loja in prioridade[1]:
            loja.entregar_pedido(prioridade[0])

    while len(lojas) > 0:
        loja = random.choice(lojas)
        motoboy = random.choice(motoboys)
        loja.entregar_pedido(motoboy)


def obter_info_motoboy(n: int) -> None:
    """
    Procura um motoboy, dentre todos, de acordo com seu atributo id_, e imprime
    suas informações caso ele exista.

    Parâmetros
    ----------
    n : int
        Número identificador do motoboy a ser procurado.
    """
    for motoboy in motoboys:
        if motoboy.id_ == n:
            print(motoboy)
            break
    else:
        print('Motoboy não encontrado.')


if __name__ == '__main__':
    lojas, motoboys = adicionar_objetos()
    distribuir_pedidos()
    comando = 'Digite o número do motoboy a ser verificado (0 para sair): '

    while True:
        try:
            n = int(input(comando))

            if n == 0:
                break
            else:
                obter_info_motoboy(n)

        except ValueError:
            print('Tipo de dado inválido.')
