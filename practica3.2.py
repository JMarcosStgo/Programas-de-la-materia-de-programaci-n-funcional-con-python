import csv
import functools
import operator


def read_csv(name_file):
    list_data = []
    with open(name_file, encoding="utf-8") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        headers = next(data)
        for x in data:
            iterator = zip(headers, x)
            list_data.append([item for item in iterator])
    return list_data


def problem_one(data):
    """
        Reducir solo partidos que ganó el equipo local
    """
    reduced_data = list(filter(lambda x: x[5][1] == 'H', data))
    print("\n",reduced_data)
    return reduced_data


def summa1(x, y):
    H = []
    for item in y:
        if x == item[1][1]:
            H.append(int(item[3][1]))
    return H


def summa2(x, y):
    A = []
    for item in y:
        if x == item[1][1]:
            A.append(int(item[4][1]))
    return A


def problem_two(data):
    """
     A partir del resultado anterior, obtener el resumen de los goles de cada equipo como local 
      y los goles recibido de los equipos visitantes.
      ----------------------------------------------------------------
      -Name team|goals from the home team|goals from the visiting team-
      ----------------------------------------------------------------

    """
    # filter to names
    names_team = {item[1][1] for item in data}
    # reduce
    reduce_H = list(map(lambda x: functools.reduce(
        operator.add, summa1(x, data)), names_team))
    reduce_A = list(map(lambda x: functools.reduce(
        operator.add, summa2(x, data)), names_team))
    # join points with the names team
    names_team = list(zip(names_team, reduce_H, reduce_A))
    print("\n",names_team)
    return names_team


def problem_three(data):
    """
    A partir del resultado anterior, mostrar aquellos equipos que el 85% del total de los goles
    hayan sido como locales, es decir, que a partir del total de los goles anotado y recibos (100%), el 85% sean goles locales
    """
    sum_goals = map(lambda x: functools.reduce(operator.add, x[1:]), data)
    answer = list(zip(data, sum_goals))
    answer = list(filter(lambda x: x[0][1] > x[1]/100*85 ,answer))
    print("\n",answer)
    
def main():
    data = read_csv('soccer_df3.csv')
    output_data = problem_one(data=data)
    output_data = problem_two(output_data)
    problem_three(output_data)


if __name__ == '__main__':
    main()
