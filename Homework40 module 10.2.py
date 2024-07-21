import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100
    
    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.days += 1
            defense = min(self.power, self.enemies)
            self.enemies -= defense
            print(f'{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.')
            time.sleep(1)

        print(f'{self.name} одержал победу спустя {self.days} дней!')


if __name__ == '__main__':
    knight1 = Knight('Sir Lancelot', 10)
    knight2 = Knight('Sir Galahad', 20)

    knight1.start()
    knight2.start()

    knight1.join()
    knight2.join()

print('Все битвы закончились!')
