from csvUtility import CsvUtility
from languageGenerator import LanguageGenerator
from sardinasPatterson import SardinasPatterson
import time

def main():
    sardinas_patterson = SardinasPatterson()
    # language_1 = ["0", "01", "101", "110"]
    # language_1 = ["1001000","0010001", "1", "1111110", "010", "000010", "00", "1001", "0"]
    # language_1 = ["1", "00", "01", "10"]
    # language_1 = ["1", "0"]
    # sardinas_patterson.language = language_1
    
    # value = sardinas_patterson.get_L1()
    # print(value)

    # value_2 = sardinas_patterson.get_Ln_plus_1(value)
    # print(value_2)

    # value_3 = sardinas_patterson.get_Ln_plus_1(value_2)
    # print(value_3)

    # print(sardinas_patterson.is_code())
    # print(sardinas_patterson.get_contre_exemple())
    # print(sardinas_patterson.make_code())

    debut = time.perf_counter()
    generator = LanguageGenerator()
    # lang = generator.generate_language()
    # print("mot genere : ", generator.generate_mot())
    # sardinas_patterson.language = lang
    # print("language genere : ", lang)
    # print(sardinas_patterson.is_code())
    # code = generator.generate_n_language(10, True)[0]
    # not_code = generator.generate_n_language(1, False)[0]

    code = generator.generate_n_language(2500, True)
    not_code = generator.generate_n_language(2500, False)
    # print("Code : ", code)    
    # print("---------------------------------------------------------------------------------------------------------")
    # print("Not Code : ", not_code)
    # print("---------------------------------------------------------------------------------------------------------")
    columns = list()
    columns.append('language')
    columns.append('length')
    columns.append('average_word_length')
    # columns.append('percentage_of_1')
    # columns.append('percentage_of_0')
    # columns.append('percentage_of_01')
    # columns.append('percentage_of_10')
    # columns.append('percentage_of_11')    
    # columns.append('percentage_of_00') 
    columns.append('frequency_of_1')
    columns.append('frequency_of_0')
    columns.append('frequency_of_01')
    columns.append('frequency_of_10')
    columns.append('frequency_of_11')
    columns.append('frequency_of_00') 
    columns.append('nc')
    # columns.append('entropy')
    columns.append('levenshtein')
    columns.append('special')
    columns.append('classe')
    values = (code + not_code)
    csv = CsvUtility()
    csv.columns = columns
    csv.values = values

    csv.to_CSV()
    fin = time.perf_counter()
    print("---------------------------------------------------------------------------------------------------------")
    print("CSV created in ", fin - debut, " seconds")
    print("---------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
