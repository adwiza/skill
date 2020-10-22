import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Thread):
    def __init__(self, name, worms, fish_tank, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(lambda: 0)
        # будем проверять в цикле, не пора ли нам заканчивать
        self.need_stop = False
        self.fish_tank = fish_tank

    def run(self):
        try:
            self._fishing()
        except Exception as exc:
            print(exc)

    # def run(self):
    #     self.catch = defaultdict(int)
    #     for worm in range(self.worms):
    #         # time.sleep(0.01)
    #         _ = worm ** 10000  # фиксируем время ожидания поклевки
    #         fish = random.choice(FISH)
    #         if fish is not None:
    #             self.catch[fish] += 1

    #    определим функцию, эмулирующую рыбалку
    def run(self):
        self.catch = defaultdict(lambda: 0)
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждём...', flush=True)
            _ = worm ** (random.randint(50, 70) * 10000)
            dice = random.randint(1, 5)
            if self.name == 'Коля' and dice == 1:
                raise ValueError(f'Блин,у меня сломалась удлочка на {worm} червяке :-(')
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catch[fish] += 1
            if self.need_stop:
                print(f'{self.name}: Ой, жена ужнать зовёт! Сматываем удочки...', flush=True)
                break


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция {func.__name__} работала {elapsed} секунд(ы)')
        return result

    return surrogate


# vasya = Fisher(name='Вася', worms=10)
# kolya = Fisher(name='Коля', worms=10)
#
# print('.' * 20, 'Он полшли на рыбалку')
#
# vasya.start()
# kolya.start()
#
# print('.' * 20, 'Ждём пока они вернутся')
#
# vasya.join()
# kolya.join()
#
# print('.' * 20, 'Итак они вернулись')
#
# for fisher in (kolya, vasya):
#     print(f'Итого рыбак {fisher.name} поймал:')
#     for fish, count in fisher.catch.items():
#         print(f'    {fish} - {count}')


# @time_track
# def run_in_one_thead(fishers):
#     for fisher in fishers:
#         fisher.run()
#
#
# @time_track
# def run_in_thead(fishers):
#     for fisher in fishers:
#         fisher.start()
#     for fisher in fishers:
#         fisher.join()
#
#
# humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава']
# fishers = [Fisher(name=name, worms=100) for name in humans]
#
# run_in_one_thead(fishers)
# run_in_thead(fishers)

vasya = Fisher(name='Вася', worms=100)
vasya.start()
time.sleep(1)
if vasya.is_alive():  # с помощью этого метода можно проверить выполняется ли ещё поток
    vasya.need_stop = True
vasya.join()  # ожадание завершения обязательно - поток может некоторое время финализировать работу
