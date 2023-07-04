def leiaDinheiro(text):
    val = False
    while not val:
        go = str(input(text).replace(',', '.'))
        if go.isalpha():
            print('ERRO, Aceitamos apenas números')
        else:
            val = True
            return float(go)

def leiaTaxa(text):
    val = False
    while not val:
        go = str(input(text).replace(',', '.'))
        if go.isalpha():
            print('ERRO, Aceitamos apenas números')
        else:
            val = True
            return float(go)


