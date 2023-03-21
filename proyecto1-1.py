import csv
import json
import pprint


def read_csv(name_file):
    with open(name_file) as csvfile:
        list_data = []
        data = csv.reader(csvfile, delimiter=',')
        headers = next(data)
        for x in data:
            iterador = zip(headers, x)
            list_data.append({key: value for key, value in iterador})
        return list_data


def problem_one(list_students):
    list_dictionary = [element for element in list_students]
    print(json.dumps(list_dictionary, sort_keys=False, indent=4))


def problem_two(name_file):
    with open(name_file) as csvfile:
        list = []
        list_population = []
        data = csv.reader(csvfile, delimiter=',')
        headers = next(data)
        for i in range(8):
            headers.remove(headers[5])
        headers.insert(5, 'Population')
        for dat in data:  # datos despues del encabezado
            for i in range(8):
                list_population.append(dat[5])
                dat.remove(dat[5])
            dat.insert(5, list_population)
            list_population = []
            iter = zip(headers, dat)
            list.append({key: value for key, value in iter})
        print(json.dumps(list, sort_keys=False, indent=4))


def problem_three(list_students):
    list_dictionarys = [{key: value for key, value in elements.items(
    ) if key == "Country/Territory" or key == "2022 Population"}for elements in list_students]
    print(json.dumps(list_dictionarys, sort_keys=False, indent=4))


def problem_four(list_students):
    list_tuples = [(elements.get('CCA3'), float(elements.get('World Population Percentage')))
                   for elements in list_students if float(elements.get('World Population Percentage')) >= 1.0]
    pprint.pprint(list_tuples)


def problem_five(list_students):
    list_tuples = [(elements.get('CCA3'), sum(list([int(y) for x, y in elements.items() if len(
        x.split(" ")) == 2 and x.split(" ")[1] == "Population"]))/8) for elements in list_students]
    pprint.pprint(list_tuples)


def problem_six(list_students):
    set_tuples = {(element.get('Country/Territory'), element.get('Continent'))
                  for element in list_students}
    pprint.pprint(set_tuples)


def problem_seven(list_students):
    continent_sets = {element.get('Continent') for element in list_students}
    pprint.pprint(continent_sets)


def problem_eight(list_students):
    country_sets = {(element.get('Country/Territory'), element.get('Continent'))
                    for element in list_students if element.get('Continent') == "North America"}
    pprint.pprint(country_sets)
    return country_sets


def problem_nine(list_students):
    country_sets = {(element.get('Country/Territory'), element.get('Continent'))
                    for element in list_students if element.get('Continent') == "South America"}
    pprint.pprint(country_sets)
    return country_sets


def problem_ten(list_students):
    country_sets = {(element.get('Country/Territory'), element.get('Continent'))
                    for element in list_students if element.get('Continent') == "Oceania"}
    pprint.pprint(country_sets)


def problem_eleven(list_students):
    country_sets = {(element.get('Country/Territory'), element.get('Continent'))
                    for element in list_students if element.get('Continent') == "Europe"}
    pprint.pprint(country_sets)
    return country_sets


def problem_twelve(list_students):
    country_sets = {(element.get('Country/Territory'), element.get('Continent'))
                    for element in list_students if element.get('Continent') == "Asia"}
    pprint.pprint(country_sets)
    return country_sets


def problem_thirteen(list_students):
    country_sets = {(element.get('Country/Territory'), element.get('Continent'))
                    for element in list_students if element.get('Continent') == "Africa"}
    pprint.pprint(country_sets)
    return country_sets


def problem_fourteen(arg1, arg2, arg3):
    union_sets = arg1.union(arg2.union(arg3))
    print(union_sets)


def problem_fiveteen(arg1, arg2):
    union_sets = arg1.union(arg2)
    print(union_sets)


def problem_sixteen(list_students):
    country_sets = {(element.get('Country/Territory'), float(element.get('World Population Percentage')))
                    for element in list_students if float(element.get('World Population Percentage')) < 0.4}
    pprint.pprint(country_sets)
    return country_sets


def problem_seventeen(list_students):
    country_sets = {(element.get('Country/Territory'), element.get('World Population Percentage'))
                    for element in list_students if float(element.get('World Population Percentage')) > 0.2}
    pprint.pprint(country_sets)
    return country_sets


def problem_eighteen(arg1, arg2):
    intersection_sets = arg1.intersection(arg2)
    pprint.pprint(intersection_sets)


def problem_nineteen(arg1, arg2):
    intersection_sets = arg1.difference(arg2)
    pprint.pprint(intersection_sets)


def problem_twenty(arg1, arg2):
    res = arg2.difference(arg1)
    pprint.pprint(res)


def main():
    l = read_csv("world_population.csv")
    # problema 1
    problem_one(l)
    #problema 2
    a = problem_two("world_population.csv")
    #problema 3
    problem_three(l)
    #problema 4
    problem_four(l)
    #problema 5
    problem_five(l)
    #problema 6
    problem_six(l)
    #problema 7
    problem_seven(l)
    #problema 8
    arg11=problem_eight(l)
    #problema 9
    arg22=problem_nine(l)
    #problema 10
    problem_ten(l)
    #problema 11
    arg1=problem_eleven(l)
    #problema 12
    arg2=problem_twelve(l)
    #problema 13
    arg3=problem_thirteen(l)
    #problema 14
    problem_fourteen(arg1,arg2,arg3)
    #problema 15
    problem_fiveteen(arg11,arg22)
    #problema 16
    arg111=problem_sixteen(l)
    #problema 17
    arg222=problem_seventeen(l)
    #problema 18
    problem_eighteen(arg111,arg222)
    #problema 19
    problem_nineteen(arg111,arg222)
    #problema 20
    problem_twelve(l)
    
if __name__ == '__main__':
    main()
