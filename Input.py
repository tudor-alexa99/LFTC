import re as regex

SPECIAL_CHARACTERS = [",", ";", "{", "}", "[", "]", "(", ")", ""]


def get_input(filename, ST_id, ST_ct, PIF):
    reserved = get_reserved('inputs/Token')
    file = open(filename, 'r')
    line = file.readline()
    line_number = 0
    while line != "adio_plictiseala" and line != "":
        line_number += 1
        new_line = tokenize(line.split())
        add_to_program(PIF, ST_id, ST_ct, reserved, new_line, line_number)
        line = file.readline()


def contains_character(t):
    for sc in SPECIAL_CHARACTERS:
        if t.__contains__(sc):
            return True
    return False


def tokenize(line):
    tokens = []
    for t in line:
        if contains_character(t):
            new_token = ""
            for letter in range(len(t)):
                if t[letter] in SPECIAL_CHARACTERS:
                    tokens.append(new_token)
                    tokens += t[letter]
                    new_token = ""
                else:
                    new_token += t[letter]
            if new_token != "":
                tokens.append(new_token)
        else:
            tokens.append(t)
    return tokens


def get_reserved(filename):
    '''Reads from token.in all the reserved words, operators and special characters'''
    f = open(filename)
    line = f.readline()

    reserved = []

    while line:
        reserved += (line.split())
        line = f.readline()
    return reserved


def check_constant(token):
    return regex.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.*\'$|^\".*\"$', token) is not None


def check_identifier(token):
    return regex.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_)*$', token) is not None


def add_to_program(PIF, ST_id, ST_ct, reserved, tokens, line):
    # tokens = (get_input('inputs/p1', reserved))
    for t in tokens:
        if t in reserved:
            PIF.add(t, None)
        elif check_constant(t):
            node = ST_ct.search(t)
            if node is None:
                PIF.add("CONST", ST_ct.pos(t))
            else:
                PIF.add("CONST", node)
        elif check_identifier(t):
            node = ST_id.search(t)
            if node is None:
                PIF.add("ID", ST_id.pos(t))
            else:
                PIF.add("ID", node)
        elif t in SPECIAL_CHARACTERS:
            PIF.add(t, None)
        else:
            raise Exception("Lexical error in line ", line)
