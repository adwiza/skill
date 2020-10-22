import time
from collections import defaultdict
import random
from threading import Thread
import queue


FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Thread):
    def __init__(self, name, worms, catcher, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catcher = catcher

    #    определим функцию, эмулирующую рыбалку
    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждём...', flush=True)
            time.sleep(random.randint(5, 20) / 10)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}, {worm}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}, {worm}: поймал {fish} и хочет положить его в садок', flush=True)
            if self.catcher.full():
                print(f'{self.name}, {worm}: Приёмщик полон !!!', flush=True)
            # Этот метод у очереди атомарный и блокирующий
            # Поток приостанавливается, пока нет места в очереди
            self.catcher.put(fish)
            print(f'{self.name}, {worm}: Наконец-то отдал {fish} приёмщику \n', flush=True)


class Boat(Thread):

    def __init__(self, worms_per_fisher=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.catcher = queue.Queue(maxsize=2)
        self.fish_tank = defaultdict(int)

    def add_fisher(self, name):
        fisher = Fisher(name=name, worms=self.worms_per_fisher, catcher=self.catcher)
        self.fishers.append(fisher)

    def run(self):
        print('Лодка вышла в море...', flush=True)
        for fisher in self.fishers:
            fisher.start()

        while True:
            try:
                # Этот метод у очереди атомарный и блокирующий
                # Поток приостанавливается и блоаируется, пока нет элементов в очереди
                fish = self.catcher.get(timeout=1)
                print(f'Приёмщик принял {fish} и положил в садок', flush=True)
                self.fish_tank[fish] += 1
            except queue.Empty:
                print('Приёмщику нет рыбы в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)


boat = Boat(worms_per_fisher=10)
humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава']
for name in humans:
    boat.add_fisher(name=name)

boat.start()
boat.join()
print(f'Лодка привезла {boat.fish_tank}')
