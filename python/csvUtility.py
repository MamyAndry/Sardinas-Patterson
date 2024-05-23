import csv

class CsvUtility:
    columns = []
    values = []

    def to_CSV(self):
        with open('./codes.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.columns)
            for elt in self.values:
                csvwriter.writerow(elt)