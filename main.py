from SymbolTable import *

if __name__ == '__main__':
    ST = SymbolTable()

    print(ST.pos("banana"))
    print(ST.pos("ananas"))
    print(ST.pos("banananas"))

    assert ST.search("inexistent") is None
    assert ST.pos("valoare_noua").data == Node("valoare_noua").data
