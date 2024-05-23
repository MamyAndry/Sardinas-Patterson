import random

from sardinasPatterson import SardinasPatterson

class LanguageGenerator:
    word_max_length = 7
    language_max_length = 10

    def get_average_word_length(self, language):
        res = 0
        for elt in language:
            res += len(elt)
        return round((res / len(language)), 2)
    
    def get_percent_of_elt(self, language, letter):
        res = 0
        for elt in language:
            res += elt.count(letter) / len(language)
        return res
    
    def get_number_of_elt(self, language, letter):
        res = 0
        for elt in language:
            res += elt.count(letter)
        return res

    def get_frequency_of_number(self, language, letter):
        res = 0
        diviseur = self.get_average_word_length(language)
        for elt in language:
            res += elt.count(letter) / diviseur
        return res

    def generate_mot(self):
        res = []
        limit = random.randint(1, self.word_max_length)
        for i in range(limit):
            value = int( random.random() * 10)
            res.append(str(value % 2))
        return ''.join(res)
    

    def generate_language(self):
        res = set()
        limit = random.randint(1, self.language_max_length)
        i = 0
        while i < limit:
            res.add(self.generate_mot())
            i += 1
            if(len(res) < 3):
                i -= 1
        return list(res)
    
    def special(self, word):
        value = "".join(word)
        number = int(value, 2)
        return number / (len(word)*200000002)

    def generate_n_language(self, limit, code):
        res = list()
        languages = list()
        sardinas_patterson = SardinasPatterson()        
        lang = None
        count = 0
        while count != limit:
            lang = self.generate_language()
            sardinas_patterson.language = lang
            if( lang not in languages and sardinas_patterson.is_code()[0] is code ):
                value = []
                languages.append(lang)
                value.append(str(len(lang)))
                value.append(str(self.get_average_word_length(lang)))
                value.append(str(self.get_percent_of_elt(lang, '0')))
                value.append(str(self.get_percent_of_elt(lang, '1')))
                value.append(str(self.get_percent_of_elt(lang, '01')))
                value.append(str(self.get_percent_of_elt(lang, '10')))
                value.append(str(self.get_percent_of_elt(lang, '00')))
                value.append(str(self.get_percent_of_elt(lang, '11')))
                value.append(str(self.get_frequency_of_number(lang, '0')))
                value.append(str(self.get_frequency_of_number(lang, '1')))
                value.append(str(self.special(lang)))
                value.append(code)
                res.append(value)
                count += 1
        return res