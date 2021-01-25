# Program to remove a column in big list of inserts for mysql

def abrir():
    f = open('users.txt', 'r')
    lista = f.read().split(',')
    # print(lista)
    # f.close()
    return lista


def run():
    # Insert the number of columns in one insert:
    columns = 7
    # INsert the number of tuplas or registers you have
    Registros = 100

    Iterations = columns*Registros
    a = abrir()
    tupla = []
    for var in list(range(1, Iterations, columns)):
        tupla.append("("+a[var]+","+a[var+1]+","+a[var+2]+","+a[var+3]+","+a[var+4]+","+a[var+5])
    print("Tuples Moified", len(tupla))
    # print(tupla[99])

    s = ", ".join(tupla)
    text_file = open("Output.txt", "w")
    text_file.write(str(s))
    text_file.close()


if __name__ == "__main__":
    run()
    abrir()
