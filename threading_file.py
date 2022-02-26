from threading import *
import threading
from time import sleep
import multiprocessing
from queue import Queue
from collections import deque
from random import randint

max_val = 0
que = deque([])
flag_finished = False
names = []

def display(message):
    current_thread_name = threading.current_thread().name
    current_process_name = multiprocessing.current_process().name
    print(f'message: {message},current thread name {current_thread_name}, current process name{current_process_name}')


class producer(Thread):

    # def __init__(self, names):
    #     super(producer, self).__init__(name=names)


    def run(self) -> None:
        # for i in range(max_val):
        #     get_random_value = randint(1,10)
        #     display(f"In Producer Thread : {get_random_value}")
        #     que.append(get_random_value)
        #     sleep(1)
        global names
        for nam in names:
            display(f"In Producer Thread : {nam}")
            que.append(nam)
            sleep(5)
        global flag_finished
        flag_finished = True


class consumer(Thread):
    def run(self) -> None:
        while not flag_finished:
            if que:
                get_pop_left = que.popleft()
                sleep(1)
                display(f"In Consume Thread : {get_pop_left}")


if __name__ == '__main__':
    max_val = 10
    names = ['Master Shake', 'Meatwad', 'Frylock', 'Carl', 'Early', 'Rusty', 'Sheriff', 'Granny', 'Lil', 'Rick',
             'Morty', 'Jerry', 'Summer', 'Beth']

    produce = producer()
    consume = consumer()

    produce.start()
    consume.start()

    produce.join()
    consume.join()
    print("At the end")
