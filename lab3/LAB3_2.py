import os
import csv
path = "D:\Documents\УЧЕБА\лабораторные\лабы 2 курс\Тех.Пр\lab3"

def print_list(list_items):
    for i in list_items:
        print(i[0], ':', i[1])
    print()

def read_csv():
    csv_path = path + "\\data.csv"
    print (csv_path)
    with open (csv_path, "r", encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj)
        for row in reader:
            data = row[1:]
            slovar[str(row[0])] = data
    return slovar
def how_many_files():
    fcount = len(os.listdir(path))
    print ("Количество файлов в папке = " + str(fcount))

def sort_list():
    list_items = list(slovar.items())
    
    list_s = [i for i in list_items if int(i[1][2]) > 2]
    print_list(list_s)
    list_items.sort(key = lambda i: i[0]) 
    print_list(list_items)
    
    list_items.sort(key = lambda i: i[1]) 
    print_list(list_items)

if __name__ == "__main__":
    slovar = {}
    how_many_files()
    slovar = read_csv()
    sort_list()
    
    
    # # print_list(list_s)
    # list_items.sort(list_items[1][2], key = list_items[1][2] > 2)
    # print_list(list_items)
   


