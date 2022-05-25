#allow csv file reading
import csv

class FileData:
    
    dates, temperatures = [], []

    def __init__(self, file_path):
        
        file = open(file_path)
        csvreader = csv.reader(file)
        temp, date = [], []

        #iterates through the file and addes each line of the file to the arrays
        for line in csvreader:
            date.append(line[0])
            temp.append(float(line[1]))
        self.dates = date
        self.temperatures = temp

        file.close()
    
