import json
import functools


def sum_count(a, b):
    return (b[0], a[1]+b[1])


def sum_count2(a):
    c = b = list(a)
    return (len(b), "".join(c))


def read_json(name_file, stop_words):
    """
        Get the average length of the words in the "short_description" field of the JSON file.
    """

    # Read stop works
    data_stop_words = [line.rstrip()
                       for line in open(stop_words, "r", encoding='utf-8')]
    # Filter words that are not in data_Stop_Works
    data = (filter(lambda x: x not in data_stop_words, json.loads(line)[
            'short_description'].split()) for line in open(name_file, 'r'))
    # Empty tuple filter, tuples are formatted (list size, list strings joined)
    data = filter(lambda x: x[1] != '', map(sum_count2, data))
    # Average of each item in data
    data = map(lambda x: len(x[1])/x[0], data)
    x = enumerate(data)
    # Sum of the averages and obtaining the total of elements
    xx, yy = functools.reduce(sum_count, x)
    # Division of the sum of averages by total elements
    print(f"The average word length is: {yy/(xx+1)}")


def main():
    read_json("News_Category_Dataset_v3.json", "stopwords-en.txt")


if __name__ == '__main__':
    main()
