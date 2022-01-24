from re import A

class Beer:
    def __init__(self, names):
        self.names = names

    def __call__(self):
        print("It's beer o'clock!")

    def __len__(self):
        return len(self.names)

    def __str__(self):
        s ="This is the list of current beers in stock: \n"
        for b in self.names:
            s+= f"{b}\n"
        return s

    def __contains__(self, name):
        if name in self.names:
            return True
        else:
            return False

    def __add__(self, beer2):
        return Beer(self.names + beer2.names)


a = Beer(['Terrapin Rye Pale Ale','Saranac Wild Berry Wheat', 'Heneiken', 'Carlsberg', 'Tuborg', 'Berlienr Kindle', 'Dogfish Head', 'Edelweiss', 'Lakefront Organic ESB', 'Old Milwaukee', 'Redhook IPA'])
a()

print(a)

if 'Carlsberg' in a:
    print("Beer in stock")
else:
    print("Beer not in stock")

print(len(a))

b = Beer(['Master Brew', 'Guld dame', 'Påskebryg'])
c = a+b
print(c)