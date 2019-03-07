import json
import hashlib


class IteratorOfCountries:
    def __init__(self, path):
        with open(path) as countries:
            self.list_of_countries = json.loads(countries.read())
        self.start = -1
        self.file = open('wiki_pages.txt', 'w', encoding='utf8')

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start != len(self.list_of_countries):
            self.country = self.list_of_countries[self.start]['name']['common']
            self.line_of_file = '{} - https://en.wikipedia.org/wiki/{}'.format(self.country, self.country.replace(' ', '_'))
            self.file.write(self.line_of_file + '\n')
            return self.line_of_file
        else:
            self.file.close()
            raise StopIteration


def generator(path):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode('utf8')).hexdigest()


if __name__ == '__main__':
    for line in IteratorOfCountries('countries.json'):
        print(line)

    for iteration in generator('countries.json'):
        print(iteration)