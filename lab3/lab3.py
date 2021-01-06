import os
import csv
path = "D:\\Documents\\лабораторные\\лабы 2 курс\\Тех.Пр\\lab3"

#1
fcount = len(os.listdir(path))
print (fcount)

#2
slovar = {}
# def print_list(list_items,)

if __name__ == "__main__":
    csv_path = path + "\\data.csv"
    print (csv_path)
    with open (csv_path, "r", encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj)
        for row in reader:
            data = row[1:]
            slovar[str(row[0])] = data
    
    list_items = list(slovar.items())
    list_items.sort(key = lambda i: i[1][2]) 
    for i in list_items:
        print(i[0], ':', i[1])
    list_items.sort(key = lambda i: i[0]) 
    for i in list_items:
        print(i[0], ':', i[1])
    n = int(input())
    for i in list_items:
        if i[1] > n:
            print(i[0], ':', i[1])

    
   


