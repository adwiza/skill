import os
import random
from collections import defaultdict
from multiprocessing import Process, Pipe, Queue
from prettytable import PrettyTable
from queue import Empty

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Process):

    def __init__(self, name, worms, fish_receiver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.fish_receiver = fish_receiver

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name} {worm} забросили - ждём', flush=True)
            # time.sleep(random.randint(1, 3) / 10)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name} {worm} Сожрали червяка!!!', flush=True)
            else:
                print(f'{self.name}, {worm} поймал {fish} и хочет положить его в садок', flush=True)
                if self.fish_receiver.full():
                    print(f'{self.name}, {worm}: садок полон !!!', flush=True)
                # этот метод атомарный у очереди и блокирующий
                # поток приостанавливается, пока нет места в очереди
                self.fish_receiver.put(fish)
                print(f'{self.name}, {worm}: наконец-то положил {fish} в садок', flush=True)


class Boat(Process):

    def __init__(self, worms_per_fisher, humans, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.fish_receiver = Queue(maxsize=2)
        self.fish_tank = defaultdict(int)
        self.humans = humans

    def run(self):
        print('Лодка вышла в море', flush=True)
        for name in self.humans:
            fisher = Fisher(name=name, worms=self.worms_per_fisher, fish_receiver=self.fish_receiver)
            self.fishers.append(fisher)
        for fisher in self.fishers:
            fisher.start()
        while True:
            try:
                # этот метод атомарный у очереди и блокирующий
                # поток приостанавливается, пока нет места в очереди
                fish = self.fish_receiver.get(timeout=1)
                print(f'Садок принял {fish}', flush=True)
                self.fish_tank[fish] += 1
            except Empty:
                print(f'В садке пусто в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)


if __name__ == '__main__':
    #  Нельзя создавать процессы рыбаков в главном процесе а запускать их в процессе лодки - разная память.
    #  Защита от дурака, нельзя создать процесс в этом процессе, а запустить в другом
    boat = Boat(worms_per_fisher=100, humans=['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ])
    boat.start()
    boat.join()


# так же в multiprocessing есть объекты синхронизации- RLock, Barrier, Condition, Event, Semaphore.
# Это практически клоны своих тезок из threading.