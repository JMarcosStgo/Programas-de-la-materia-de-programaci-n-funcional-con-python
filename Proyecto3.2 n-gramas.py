def n_gramas(data, n, b, name_file):
    # Generator
    data_gramas = (line.rstrip().split("=")[1].split(
        ",") for line in open(data, "r", encoding='utf-8') if len(line) > n)
    # Crear diccionario
    dict_n_gramas = dict()
    res = []
    while True:
        try:
            # Recorrer linea a linea el txt
            a = next(data_gramas)
            # crear tuplas
            data_n_gramas = map(lambda x: tuple(a[x:x+n]), range(0, len(a)-n+1))
            for x in *data_n_gramas, :
                res.append(x)
        except StopIteration:
            print("Finaliza lectura")
            break
    # Frecuencias
    for x in res:
        if x not in dict_n_gramas:
            dict_n_gramas[x] = 1
        else:
            dict_n_gramas.update({x: 1 + dict_n_gramas.get(x)})
    res = {key: val for key, val in sorted(
        dict_n_gramas.items(), key=lambda ele: ele[1], reverse=True)}
    # Escritura
    with open(name_file, "w", encoding="utf-8") as out_file:
        out_file.writelines((f"[{value}] {','.join(key)}  \n")
                            for key, value in res.items() if value >= b)


if __name__ == '__main__':
    n = 3
    b = 4
    name_file = "Ejemplo_n_"+str(n)+"_B_"+str(b)+".txt"
    n_gramas("AlfaMasMenos5000.txt", n, b, name_file)
