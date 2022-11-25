import re


class TextParser:
    """Парсер текстовых данных в некой системе."""

    def __init__(self, text: str):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor) -> None:
        """Вызывает метод класса обработчика.

        :param processor: экземпляр класса обработчика
        """
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class WordCounter:
    """Счётчик частотности слов в тексте."""

    def __init__(self, text: str) -> None:
        """Обрабатывает переданный текст и создаёт словарь с частотой слов."""
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word: str) -> int:
        """Возвращает частоту переданного слова."""
        return self.__words.get(word, 0)

    def get_all_words(self) -> dict[str, int]:
        """Возвращает словарь с частотой слов."""
        return self.__words.copy()


class AdapterWordCounter:
    """Адаптер, позволяющий выводить текст в порядке частотности слов """
    # ИСПРАВИТЬ: вы написали метод, не использующий объект экземпляра self — такой метод считается статическим — если это и было целью, то следует явно декорировать метод как статический (его всё равно можно будет вызывать от объекта экземпляра)
    def process_text(self, text):
        words = WordCounter(text).get_all_words().items()
        return sorted(words, key=lambda x: x[1], reverse=True)


text = 'Вот дом, который построил Джек ' \
       'а это пшеница, которая в темном чулане хранится, ' \
       'в доме, который построил Джек %% №'

parser_text = TextParser(text)
adapter = AdapterWordCounter()
parser_text.get_processed_text(adapter)


# stdout:
"""
('который', 2)
('построил', 2)
('джек', 2)
('в', 2)
('вот', 1)
('дом', 1)
('а', 1)
('это', 1)
('пшеница', 1)
('которая', 1)
('темном', 1)
('чулане', 1)
('хранится', 1)
('доме', 1)
"""


# ИТОГ: очень хорошо — 11/12
