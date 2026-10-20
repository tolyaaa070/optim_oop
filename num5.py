class RealString:
    def __init__(self, string):
        self.string = str(string)

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self) == len(other)
        return len(self) == len(str(other))

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self) < len(other)
        return len(self) < len(str(other))

    def __le__(self, other):
        if isinstance(other, RealString):
            return len(self) <= len(other)
        return len(self) <= len(str(other))

    def __gt__(self, other):
        if isinstance(other, RealString):
            return len(self) > len(other)
        return len(self) > len(str(other))

    def __ge__(self, other):
        if isinstance(other, RealString):
            return len(self) >= len(other)
        return len(self) >= len(str(other))

str1 = RealString("Apple")
str2 = RealString("Яблоко")
print(str1 < str2)
print(str1 > "Hi")
print(str2 == "Banana")
print(RealString("Hi") == "Hi")