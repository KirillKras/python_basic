from random import randint, shuffle

class Barrel:
    def __init__(self):
        self.__numbers = [i for i in range(1, 91)]

    def __iter__(self):
        return self

    def __next__(self):
        nm_len = len(self.__numbers)
        if nm_len:
            rand = randint(0, len(self.__numbers)-1)
            return self.__numbers.pop(rand)
        else:
            raise StopIteration

class Card:
    def __init__(self, name):

        def create_matrix():
            s = set()
            while len(s) < 15:
                s.add(randint(1, 91))
            lst = list(s)
            line1 = lst[:5] + [None for _ in range(4)]
            shuffle(line1)
            line2 = lst[5:10] + [None for _ in range(4)]
            shuffle(line2)
            line3 = lst[10:] + [None for _ in range(4)]
            shuffle(line3)
            return [line1, line2, line3]

        self.__matrix = create_matrix()
        self.name = name
        self.balance  = 15

    def __repr__(self):
        result = []
        result.append(self.name + '-' * (34-len(self.name)) + '\n')
        for line in self.__matrix:
            for num in line:
                if num:
                    result.append(f'{num:<4}')
                else:
                    result.append('    ')
            result.append('\n')
        result.append('-' * 34 + '\n')
        return ''.join(result)


    def step(self, num):
        for i, line in enumerate(self.__matrix):
            for j, n in enumerate(line):
                if n == num:
                    self.__matrix[i][j] = '-'
                    self.balance -= 1
                    return True
        return False



class Gamer:
    def __init__(self, name):
        self.name = name
        self.card = Card(name)

    def __repr__(self):
        return self.card.__repr__()


class ManualGamer(Gamer):

    def __getEnter(self):
        enter = ''
        while enter not in [True, False]:
            enter = input('Есть число в карточке? (y/n): ')
            if enter == 'y':
                enter = True
            elif enter == 'n':
                enter = False
            else:
                print("Введите 'y' или 'n'")
        return enter

    def makeMove(self, num):
        enter = self.__getEnter()
        result = self.card.step(num)
        return enter, result


class AutoGamer(Gamer):
    def makeMove(self, num):
        result = self.card.step(num)


class Game:
    def __init__(self):
        self.manual_gamer = ManualGamer('Kirill')
        self.auto_gamer = AutoGamer('r2d2')
        self.barrel = Barrel()
        print(self.manual_gamer)
        print(self.auto_gamer)


    def go(self):
        for num in self.barrel:
            print(f'Выпало число {num}')
            enter, result = self.manual_gamer.makeMove(num)
            print(self.manual_gamer.card)
            if enter != result:
                print(f'Вы пропустили боченок. Выиграл {self.auto_gamer.name}')
                break
            self.auto_gamer.makeMove(num)
            print(self.auto_gamer.card)
            if self.manual_gamer.card.balance == 0:
                print(f'Выиграл {self.manual_gamer.name}')
                break
            if self.auto_gamer.card.balance == 0:
                print(f'Выиграл {self.auto_gamer.name}')
                break

g = Game()
g.go()