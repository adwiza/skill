import os
import random
from collections import defaultdict
from multiprocessing import Process
from prettytable import PrettyTable

FISH = (None, 'плотва', 'окунь', 'лещ')


def fishing(name, worms):
    print(f'{name} parent process', os.getppid())
    print(f'{name} process id', os.getpid())
    catch = defaultdict(lambda: 0)
    for worm in range(worms):
        print(f'{name} Червяк № {worm} - Заросил, ждём...', flush=True)
        _ = worm ** (random.randint(50, 70) * 10000)
        fish = random.choice(FISH)
        if fish is None:
            print(f'{name}: Тьфу, сожрали червяка...', flush=True)
        else:
            print(f'{name}: Ага, у меня {fish}', flush=True)
            catch[fish] += 1
    print(f'Итого рыбак {name} поймал:')

    for fish, count in catch.items():
        catch_table = PrettyTable()
        catch_table.field_names = ['Рыба', 'Количество']
        catch_table.add_row([fish, count])
        print(catch_table)


if __name__ == '__main__':
    proc = Process(target=fishing, kwargs=dict(name='Вася', worms=10))
    proc.start()

    fishing(name='Коля', worms=10)

    proc.join()


