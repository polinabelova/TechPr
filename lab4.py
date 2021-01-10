import os
import csv
path = "D:\Documents\УЧЕБА\лабораторные\лабы 2 курс\Тех.Пр\lab3"

class MyData:
    def __setattr__(self, name, value):
        self.__dict__[name] = value

    '''итератор разделяет строку на символы
    param: self-ссылка на элемент класса
    return: self'''
    def __iter__(self):
        self.a = 1
        return self
    
    '''метод  next должен возвращать следующий элемент в последовательности
    param:self-ссылка на элемент класса
    return:x-один символ от элемента класса'''
    def __next__(self):
        x = self.a
        self.a += 1
        return x
     
    
class Employee(MyData):
    '''Метод repr вернет строку, содержащую печатаемое формальное представление объекта.
    param:self-ссылка на объект'''
    def __repr__(self):
        return repr(self.position)
    ''''метод getitem возвращает элемент по значению ключа
    param:self- ссылка на объект, key ключ'''    
    def __getitem__(self, key): 
        return getattr(self, key)
    '''Статический метод. Выводит id и должность сотрудника'''
    @staticmethod 
    def print_id_and_position(self):
        return(self.id, self.position)


"""
Чтение данных из файла
"""
def read_csv():
    csv_path = path + "\\data.csv"
    print (csv_path)
    for row in open(csv_path, "r",encoding = 'utf-8'):
        data = row.split(",")
        emp = Employee()
        emp.__setattr__("id", data[0])
        emp.__setattr__("FIO", data[1])
        emp.__setattr__("position", data[2])
        emp.__setattr__("exp", data[3])
        print(emp.FIO)
        
        print(repr(emp))
        
        print(emp["id"])
        print(Employee.print_id_and_position(emp))
    i = 0
    myit = iter(emp.position)
    while(i < len(emp.position)):
        print(next(myit))
        i+=1

def csv_reader(csv_path):           
    for row in open(csv_path, "r",encoding = 'utf-8'): 
        '''Генератор'''   
        yield row
'''Выводит количество строк в файле'''
def how_many_rows():
    csv_gen = csv_reader(path+"\\data.csv")
    row_count = 0
    for row in csv_gen:
        row_count += 1
    print(f"Количество строк в файле = {row_count}")
def how_many_files():
    fcount = len(os.listdir(path))
    print ("Количество файлов в папке = " + str(fcount))

if __name__ == "__main__":

    how_many_files()
    how_many_rows()
    read_csv()
    
    
    
