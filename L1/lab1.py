import json
import xml
import xml.etree.ElementTree as ET
import sys

class Study_Facilities():
    def __init__(self, name, year, students):
        self.name=name
        self.year=year
        self.students=students

    def print_data(self):
        print(self.name, self.year, self.students)
    
    
     
class University(Study_Facilities):

    def __init__(self, name, year, students, budget_places, pay_places):
        super().__init__(name, year, students)
        self.budget_places=budget_places
        self.pay_places=pay_places

    def print_data(self):
        print(self.name, self.year, self.students, self.budget_places, self.pay_places)

    def data_parser(self, data):
        try:
            self.name = data["name"]
            self.year = data["year"]
            self.students = data["students"]
            self.budget_places = data["budget_places"]
            self.pay_places = data["pay_places"]
        except KeyError:
            print("Wrong data")
            sys.exit()


class School(Study_Facilities):


    def __init__(self, name, year, students, classes):
        super().__init__(name, year, students)
        self.classes=classes

    def print_data(self):
        print(self.name, self.year, self.students, self.classes)

    def data_parser(self, data):
        try:
            self.name = data["name"]
            self.year = data["year"]
            self.students = data["students"]
            self.classes = data["classes"]
        except KeyError:
            print("Wrong data")
            sys.exit()
    

def data_to_json(class_list, path):
    with open(path, "w") as file:
        for cl in class_list:
            json.dump(cl.__dict__, file)

def json_to_data(path):
    try:
        with open(path) as file:
            l = list(file.read().split("}"))
            data = list()
            for obj in l:
                obj += "}"
                if len(obj) < 2:
                    continue
                data.append(json.loads(obj))
    except FileNotFoundError:
        print("File doesn't exist")
        sys.exit()
        
    return data

def data_to_xml(class_list, path):
    st = ""
    for cl in class_list:
        name = ET.Element("School")
        d = cl.__dict__
        for element in d:
            section = ET.SubElement(name, element)
            section.text = str(d.get(element))
        s = ET.tostring(name, encoding="utf-8", method="xml")
        s = s.decode("UTF-8")
        st += s + "\n"

    with open(path, "w") as file:
        file.write(st)

def xml_to_data(path):
    try:
        with open(path) as file:
            st = list(file.read().split("\n"))

        data = list()
        for element in st:
            if len(element) < 2:
                continue
            tree = ET.ElementTree(ET.fromstring(element)).getroot()
            di = {}
            for el in tree:
                di[el.tag] = el.text
            data.append(di)
        return data
    except FileNotFoundError:
        print("File not found")
    except xml.etree.ElementTree.ParseError: 
        print("File incorrected")

obj_list = list()
inp = None
while(inp != 0):
    print("1 - создать экземпляр вуза\n2 - создать экземпляр школы")
    print("3 - перевести список в json\n4 - перевести список в xml")
    print("5 - считать из json\n6 - считать из xml")
    print("7 - вывести список\n0 - выход из программы")
    inp = int(input())
    if inp == 1:
        print("Введите: имя, год, кол-во студентов, бюджетные места, платные места")
        l = list(input().split(" "))
        obj_list.append(University(l[0], l[1], l[2], l[3], l[4]))
    elif inp == 2:
        print("Введите: имя, год, кол-во учеников, кол-во классов")
        l = list(input().split(" "))
        obj_list.append(School(l[0], l[1], l[2], l[3]))
    elif inp == 3:
        data_to_json(obj_list, "classes.json")
    elif inp == 4:
        data_to_xml(obj_list, "classes.xml")
    elif inp == 5:
        obj_list = list()
        l = json_to_data("classes.json")
        for element in l:
            if len(element) == 4:
                sc = School(0, 0, 0, 0)
                sc.data_parser(element)
                obj_list.append(sc)
            elif len(element) == 5:
                sc = University(0, 0, 0, 0, 0)
                sc.data_parser(element)
                obj_list.append(sc)
    elif inp == 6:
        obj_list = list()
        l = xml_to_data("classes.xml")
        for element in l:
            if len(element) == 4:
                sc = School(0, 0, 0, 0)
                sc.data_parser(element)
                obj_list.append(sc)
            elif len(element) == 5:
                sc = University(0, 0, 0, 0, 0)
                sc.data_parser(element)
                obj_list.append(sc)
    elif inp == 7:
        for obj in obj_list:
            obj.print_data()
