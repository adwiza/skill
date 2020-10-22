import os
import random
from collections import defaultdict
from multiprocessing import Process, Pipe, Queue
from queue import Empty
from prettytable import PrettyTable

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Process):

    def __init__(self, name, worms , *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms

    def run(self):
        print(f'{self.name} parent process', os.getppid())
        print(f'{self.name} process id', os.getpid())
        catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name} Червяк № {worm} - Заросил, ждём...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                catch[fish] += 1

        print(f'Итого рыбак {self.name} поймал:')

        for fish, count in catch.items():
            catch_table = PrettyTable()
            catch_table.field_names = ['Рыба', 'Количество']
            catch_table.add_row([fish, count])
            print(f'        {fish}  -  {count}')
            # print(catch_table)


if __name__ == '__main__':
    vasya = Fisher(name='Вася', worms=100)
    kolya = Fisher(name='Коля', worms=100)

    print('*' * 20, 'Они пошли на рыбалку')
    vasya.start()
    kolya.start()
    print('*' * 20, 'Ждем пока они вернутся')

    vasya.join()
    kolya.join()
    print('*' * 20, 'Итак, они вернулись')
