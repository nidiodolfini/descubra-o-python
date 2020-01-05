anomina = lambda param: param + param

print(anomina(2))


def funcaonomeadas(y, x, /):
    return x


# Minissérie Pythonica: Funções #4 - Anotações de tipos de argumentos

# def soma(x: int, y: int) -> int: não funciona direito, pois aceita string
#     return x + y

from numbers import Number
from typing import List, Dict, Union


def meu_sum(l: List[Number]) -> Number:
    return sum(l)


print(meu_sum([1, 2, 3]))


def cadastro_usuario(
        nome: str,
        idade: int,
        gostos: List[str]
) -> Dict[str, Union[str, int, List[str]]]:
    return {
        'nome': nome,
        'idade': idade,
        'gostos': gostos
    }


print(cadastro_usuario('Nidio', 33, ['Musica', 'café']))