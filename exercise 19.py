from functools import lru_cache


def moves(h):
    a, b = h  # Если куча одна, то return h+1, h*2
    return (a+1, b), (a*4, b), (a, b+1), (a, b*4)  # Ходы


@lru_cache(None)
def game(h):
    a, b = h
    if a+b >= 82:
        return "W"  # Условие для кучи
    if any(game(m) == "W" for m in moves(h)):
        return "P1"
    if any(game(m) == "P1" for m in moves(h)):  # Для 19 меняем all на any
        return "B1"
    if any(game(m) == "B1" for m in moves(h)):
        return "P2"
    if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
        return "B2"


for s in range(1, 100):
    h = 4, s  # Начальное кол-во камней в куче
    if game(h) == 'B1':  # Исход
        print(s, game(h))
