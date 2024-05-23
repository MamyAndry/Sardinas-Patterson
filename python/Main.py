import json
from csvUtility import CsvUtility
from languageGenerator import LanguageGenerator
from sardinasPatterson import SardinasPatterson

def main():
    sardinas_patterson = SardinasPatterson()
    language_1 = ["0", "01", "101", "110"]
    # language_1 = ["1", "01", "01", "110"], 
    # language_1 = ["1", "00", "01", "10"]
    # language_1 = ["1", "0"]
    # sardinas_patterson.language = language_1
    
    # value = sardinas_patterson.get_L1()
    # print(value)

    # value_2 = sardinas_patterson.get_Ln_plus_1(value)
    # print(value_2)

    # value_3 = sardinas_patterson.get_Ln_plus_1(value_2)
    # print(value_3)

    # print(sardinas_patterson.get_L1())
    # print(sardinas_patterson.get_contre_exemple())
    # print(sardinas_patterson.make_code())

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
    columns = ['length', 'average_word_length', 'percentage_of_1', 'percentage_of_0', 'percentage_of_01', 'percentage_of_10','percentage_of_00', 'percentage_of_11', 'frequency_of_1', 'frequency_of_0', 'special', 'code']
    values = (code + not_code)
    csv = CsvUtility()
    csv.columns = columns
    csv.values = values

    csv.to_CSV()
    print("---------------------------------------------------------------------------------------------------------")
    print("CSV created")
    print("---------------------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()
