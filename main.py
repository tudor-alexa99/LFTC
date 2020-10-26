from PIF import *
from SymbolTable import *
from Input import *

if __name__ == '__main__':
    ST = SymbolTable()

    assert ST.search("inexistent") is None
    assert ST.pos("valoare_noua").data == Node("valoare_noua").data

    #
    PIF = PIF()
    ST_id = SymbolTable()
    ST_ct = SymbolTable()

    get_input('inputs/p1', ST_id, ST_ct, PIF)

    # print(PIF)
    print(ST_id.print())
    # print(tokenize(["amplu", "la,", "mare"]))

    #
    # ST = SymbolTable()
    # ST.pos("c")
    # ST.pos("b")
    # ST.pos("d")
    # ST.pos("a")
    # ST.pos("asd")
    # ST.pos("dasd")
    # ST.pos("sdfd")
    # ST.pos("dasdaw")
    #
    # print(ST.print())
    #
    # read(PIF, ST_id, ST_ct)
    #
    #

    # print(check_identifier('abi'))
