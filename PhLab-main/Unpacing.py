class Unpacking_Modul:

    def garbage(self):
        with open(r"C:\Users\Даниил\PycharmProjects\pythonProject\venv\Lib\objects.yaml") as f:
            garbage1 = yaml.load(f, Loader=FullLoader)
            return (garbage1)





