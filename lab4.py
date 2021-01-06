import os
import csv
path = "D:\Documents\УЧЕБА\лабораторные\лабы 2 курс\Тех.Пр\lab3"

class Employee:
    def __setattr__(self, name, value):
        self.__dict__[name] = value



def read_csv():
    collect = []
    csv_path = path + "\\data.csv"
    print (csv_path)
    with open (csv_path, "r", encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj)
        for row in reader:
            data = row[1:]
            # men.__setattr__("surname", "Иванов")
            # men.__setattr__("name", "Иван")
            # collect.append(men)
            print (data[0])
            
            
    
def how_many_files():
    fcount = len(os.listdir(path))
    print ("Количество файлов в папке = " + str(fcount))
if __name__ == "__main__":
    slovar = {}
    how_many_files()
    read_csv()
    collect = []

    men = Employee()
    men.__setattr__("surname", "Иванов")
    men.__setattr__("name", "Иван")
    collect.append(men)

    print(collect[0].name)
    