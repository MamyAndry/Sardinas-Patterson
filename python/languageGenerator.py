import math
import random
from sardinasPatterson import SardinasPatterson
from nltk.metrics.distance import edit_distance

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
            if(len(res) < 2):
                i -= 1
        return list(res)
    
    def count_word_composed_of_letter(self, language, letter):
        occ = 0
        for elt in language:
            if(elt.count(letter) == len(elt)):
                occ += 1
        return occ
    
    def count_word_composed_of_mixed_letter(self, language):
        occ = 0
        for elt in language:
            if('01' in elt or '10' in elt):
                occ += 1
        return occ
    
    def calcul_value(self, language):
        res = 0
        occ_0 = self.count_word_composed_of_letter(language, '0')
        occ_1 = self.count_word_composed_of_letter(language, '1')
        occ_mixte = self.count_word_composed_of_mixed_letter(language)
        res = (occ_0 * 2) + (occ_1 * 2) + (occ_mixte * 1) 
        return res / 5

    def special(self, word):
        value = "".join(word)
        number = int(value, 2)
        return number / (len(word)*240420020)
    
    def letter_probability(self, string, letter):
        return string.count(letter) / len(string)
    
    def word_entropy(self, string):
        p_0 = self.letter_probability(string, '0')
        p_1 = self.letter_probability(string, '1')
        log_0 = 0
        if(p_0 != 0):
            log_0 = math.log(p_0, 2)
        log_1 = 0
        if(p_1 != 0):
            log_1 = math.log(p_1, 2)
        res = -1
        res *= ((p_0 * log_0) + (p_1 * log_1))
        return res

    def levenshtein_average_interval(self, language):
        total_interval = 0
        pair_nb = 0
        for i in range(len(language)):
            for j in range(i+1, len(language)):
                total_interval += edit_distance(language[i], language[j])
                pair_nb += 1
        return total_interval / pair_nb if pair_nb > 0 else 0

    def entropy(self, language):
        res = 0
        for elt in language:
            res += self.word_entropy(elt)
        return res/len(language) 

    def calculate_nc(self, language):
        res = 0
        for string in language:
            p_0 = self.letter_probability(string, '0')
            p_1 = self.letter_probability(string, '1')
            res += (p_0 * len(language)) + (p_1 * len(language))
        return res

    def parity_calculation(self, language):
        res = 0
        for elt in language:
            res += elt.count('1')
        return res % 2

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
                value.append(lang)
                value.append(str(len(lang)))
                value.append(str(self.get_average_word_length(lang)))
                # value.append(str(self.get_percent_of_elt(lang, '0')))
                # value.append(str(self.get_percent_of_elt(lang, '1')))
                # value.append(str(self.get_percent_of_elt(lang, '01')))
                # value.append(str(self.get_percent_of_elt(lang, '10')))
                # value.append(str(self.get_percent_of_elt(lang, '00')))
                # value.append(str(self.get_percent_of_elt(lang, '11')))
                value.append(str(self.get_frequency_of_number(lang, '0')))
                value.append(str(self.get_frequency_of_number(lang, '1')))
                value.append(str(self.get_frequency_of_number(lang, '01')))
                value.append(str(self.get_frequency_of_number(lang, '10')))
                value.append(str(self.get_frequency_of_number(lang, '00')))
                value.append(str(self.get_frequency_of_number(lang, '11')))
                value.append(str(self.calculate_nc(lang)))
                # value.append(str(self.entropy(lang)))
                # value.append(str(self.parity_calculation(lang)))
                value.append(str(self.levenshtein_average_interval(lang)))
                value.append(str(self.special(lang)))
                value.append(code)
                res.append(value)
                count += 1
        return res