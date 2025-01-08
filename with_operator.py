import os

os.system('COLOR B')

class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames

    def _clean_word(self, word):
        """Удаляет знаки препинания из слова."""
        for char in [',', '.', '=', '!', '?', ';', ':']:
            word = word.replace(char, '')

        return word.strip('-')

    def get_all_words(self):
        """Возвращает словарь, содержащий слова из каждого файла."""
        all_words = {}

        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                words = [
                    self._clean_word(word)
                    for word in text.split()
                ]
                all_words[filename] = words

        return all_words

    def find(self, word):
        """Возвращает позицию первого найденного слова в каждом файле."""
        result = {}
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            try:
                index = words.index(word)
                result[filename] = index + 1 # индексация начинается с 1
            except ValueError:
                pass # Слово отсутствует

        return result

    def count(self, word):
        """Возвращает количество указанного слова в каждом файле."""
        result = {}
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            result[filename] = words.count(word)

        return result

finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
print(finder.find('слово'))
print(finder.count('другое_слово'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

try:
    os.system('PAUSE')
except:
    os.system('CLS')
