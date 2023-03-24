import yaml
from yaml.loader import FullLoader

class Unpacking_Modul:

    def Option(self):
        with open(r"C:\Users\Даниил\Desktop\PhLab-main\objects.yaml") as f:
            garbage1 = yaml.load(f, Loader=FullLoader)
            Option1 = garbage1["Option"]
            return (Option1)
    def Objects(self):
        with open(r"C:\Users\Даниил\Desktop\PhLab-main\objects.yaml") as f:
            garbage1 = yaml.load(f, Loader=FullLoader)
            Objects1 = garbage1["Objects"]
            return (Objects1)




a = Unpacking_Modul()
b = a.Objects()
keys = b.keys()
for i in b.keys():
    print(i)


