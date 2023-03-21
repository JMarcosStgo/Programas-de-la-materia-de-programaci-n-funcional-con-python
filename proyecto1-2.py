from ast import arg
import csv
import json
import pprint


def read_csv(name_file):
    with open(name_file, encoding="utf-8") as csvfile:
        list_data = []
        data = csv.reader(csvfile, delimiter=',')
        headers = next(data)
        for x in data:
            iterador = zip(headers, x)
            list_data.append({key: value for key, value in iterador})
        # print(list_data)
        return list_data


def problem_one(list_channels):
    list_subscriptors = [channel for channel in list_channels]
    print(json.dumps(list_subscriptors, sort_keys=False, indent=4))


def problem_two(list_channels):
    list_channels = [{element.get('Youtuber'): element.get(
        'subscribers')} for element in list_channels]
    print(json.dumps(list_channels, sort_keys=False, indent=4))


def problem_tree(list_channels):
    list_channels = [{element.get('Youtuber'): element.get(
        'started')} for element in list_channels if int(element.get('started')) >= 2010]
    print(json.dumps(list_channels, sort_keys=False, indent=4))


def problem_four(list_channels):
    list_data = [{element.get('Youtuber'): element.get(
        'started')} for element in list_channels if int(element.get('started')) < 2010]
    print(json.dumps(list_data, sort_keys=False, indent=4))


def problem_five(list_channels):
    list_data = [{element.get('Youtuber'): [{"subscribers": element.get('subscribers')}, {"video views": element.get('video views')}, {
        "category": element.get('category')}, {"started": element.get('started')}]} for element in list_channels if int(element.get('started')) >= 2000]
    print(json.dumps(list_data, sort_keys=False, indent=4))


def problem_six(list_channels):
    dictionary = {element.get('Youtuber'): element.get(
        'category') for element in list_channels if element.get("category") == "Gaming"}
    pprint.pprint(dictionary)


def problem_seven(list_channels):
    dictionary = {element.get('Youtuber'): element.get(
        'subscribers') for element in list_channels}
    pprint.pprint(dictionary)


def problem_eigth(list_channels):
    dictionary = {element.get('Youtuber'): element.get(
        'started') for element in list_channels}
    pprint.pprint(dictionary)


def problem_nine(list_channels):
    dictionary = {element.get('Youtuber'): element.get(
        'video views') for element in list_channels if element.get('video views') >= "100,000,000"}
    pprint.pprint(dictionary)


def problem_ten(list_channels):
    dictionary = {element.get('Youtuber'): element.get(
        'category') for element in list_channels if element.get('category') == "Entertainment"}
    pprint.pprint(dictionary)


def problem_eleven(list_channels):
    sets = {element.get('category') for element in list_channels}
    pprint.pprint(sets)
    return sets


def problem_twelve(list_channels):
    sets = {(element.get('Youtuber'), element.get('category'))
            for element in list_channels if element.get('category') == "Education"}
    pprint.pprint(sets)
    return sets


def problem_thirteen(list_channels):
    sets = {(element.get('Youtuber'), element.get('category'))
            for element in list_channels if element.get('category') == "Entertainment"}
    #pprint.pprint(sets)
    return sets


def problem_fourteen(list_channels):
    sets = {(element.get('Youtuber'), element.get('category'))
            for element in list_channels if element.get('category') == "Music"}
    #pprint.pprint(sets)
    return sets


def problem_fiveteen(list_channels):
    sets = {(element.get('Youtuber'), element.get('category'))
            for element in list_channels if element.get('category') == "Entertainment" and element.get('video views') > "100,000,000"}
    #pprint.pprint(sets)
    return sets


def problem_sixteen(arg1, arg2):
    union = arg1.union(arg2)
    pprint.pprint(union)


def problem_seventeen(arg1, arg2):
    union = arg1.union(arg2)
    pprint.pprint(union)


def problem_eigthteen(arg1,arg2):
    intersection = arg2.intersection(arg1)
    #pprint.pprint(intersection)

def problem_nineteen(arg1, arg2):
    difference = arg1.difference(arg2)
    pprint.pprint(difference)


def problem_twenty(arg1,arg2):
    difference = arg1.symmetric_difference(arg2)
    pprint.pprint(difference)


def main():
    entrada = read_csv("mostsubscribedyoutubechannels.csv")
    # los 10 canales con mas supscriptores donde cada elemento de la lista se un diccionario rank:values
    problem_one(entrada);
    # una lista de diccionarios de Channel Official name:numbers of subscribers
    problem_two(entrada)
    # una lista con diccionarios youtubers:started donde el año en que se inicio sea mayor o igual  a 2010
    problem_tree(entrada)
    # una lista con diccionarios youtubers:started , donde el año en que se inicio sea menor a 2010
    problem_four(entrada)
    # una lista con diccionarios youtubers:started, y que los subscriptores del canal sean mayor a 100,000,000
    problem_five(entrada)
    # un diccionario de el nombre de los canales y su categoria {name:category} y que la categoria sea gaming
    problem_six(entrada)
    # un diccionario de el nombre del canal y la cantidad de subscriptores
    problem_seven(entrada)
    # un diccionario de el nombre del canal y el año en que inicio el canal
    problem_eigth(entrada)
    # un diccionario con el nombre y la cantidad de vistas que sean mayor a 100,000,000
    problem_nine(entrada)
    # un diccionario con el nombre y categoria, que la categoria sea entertaiment
    problem_ten(entrada)
    # crear un conjunto de las categorias
    arg1 = problem_eleven(entrada)
    # Crear un conjunto donde sus elementos están formados por una tupla: Youtuber/category y category  sea Education
    arg2=problem_twelve(entrada)
    # Crear un conjunto donde  sus elementos están formados por una tupla: Youtuber/category y category  sea Entertaiment
    arg1 = problem_thirteen(entrada)
    # Crear un conjunto donde  sus elementos están formados por una tupla: Youtuber/category y category  sea Music
    arg2 = problem_fourteen(entrada)
    # Crear un conjunto donde  sus elementos están formados por una tupla: Youtuber/category y category  sea Howto & Style, Ademas la cantidad de video views sea mayor a 100,000,000
    arg2 = problem_fiveteen(entrada)
    # Mediante operación de conjuntos unir los conjuntos del problema 11 y 12
    problem_sixteen(arg1,arg2)
    # Mediante operación de conjuntos unir los conjuntos del problema 11 y 14
    problem_seventeen(arg1, arg2)
    #Mediante una operacion de interseccion encontrar los youtubers con la misma categoria del ejercicio 13 y 15
    problem_eigthteen(arg1,arg2)
    #Mediante operación de conjunto obtener elementos que estan en el conjunto del ejercicio 13 pero no en el conjunto del ejercicio 15.
    problem_nineteen(arg1,arg2)
    #conjunto de elementos que están ya sea en el primero o en el segundo conjunto, pero no en ambos.
    problem_twenty(arg1,arg2)
if __name__ == '__main__':
    main()
