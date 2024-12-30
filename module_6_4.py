class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0] if args else "Unnamed House"
        cls.houses_history.append(house_name)
        instance = super(House, cls).__new__(cls)
        return instance


    def __init__(self, first, second=25, third=3.14):
        self.first = first
        self.second = second
        self.third = third


    def __del__(self):
        print(f"{self.first} снесён, но он останется в истории")



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


# Удаление объектов
del h2
del h3
print(House.houses_history)