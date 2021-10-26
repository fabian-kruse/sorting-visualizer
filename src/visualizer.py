import pygame as pg
import algorithms
import time

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pg.init()
WIN = pg.display.set_mode((800, 800))

instruction = '''
This is a sorting algorithm visualization tool built with Pygame.
Use the left and right keys to change between algorithms.
During execution array accesses and swaps are being counted and displayed.
If you have chosen your algorihtm press the space bar to start the proccess.
Press "r" to get a new randomization of the list.
Enjoy!'''

def get_size():
    msg = input("Please enter the number of elements between 10 and 200: ")
    try:
        if type(int(msg)) is int and int(msg) >= 10 and int(msg) <= 200:
            return int(msg)
    except:
        print("invalid input")

def check_open():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()


def update(algorithm, swap1=None, swap2=None, win=WIN):
    time.sleep(algorithm.time)
    win.fill(WHITE)
    pg.display.set_caption(
        "{}       Swaps: {}       Array accesses: {}".format(algorithm.name, algorithm.swaps, algorithm.array_accesses))
    xgap = win.get_width() // len(algorithm.array)
    ygap = win.get_height() // len(algorithm.array)
    for i in range(len(algorithm.array)):
        if swap1 == algorithm.array[i]:
            col = GREEN
        elif swap2 == algorithm.array[i]:
            col = BLUE
        else:
            col = (0, 0, 0)
        pg.draw.rect(win, col,
                     (i * xgap, win.get_height() - ygap * algorithm.array[i], xgap, ygap * algorithm.array[i]))
    check_open()
    pg.display.update()


def main(win):
    print(instruction)
    msg = ""
    while msg != "y":
        msg = input("Would you like to continue? [y/n]")
        if msg == "n":
            exit(0)
    size = get_size()
    win.fill(WHITE)
    run = True
    algo_idx = 0
    seed = 0
    algos = [algorithms.SelectionSort(size,seed), algorithms.BubbleSort(size,seed), algorithms.InsertionSort(size,seed)]
    algo = algos[algo_idx]
    started = False
    update(algo)

    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

            if started:
                continue

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    started = True
                    algo.run()
                    started = False
                elif event.key == pg.K_r:
                    seed += 1
                    algos = [algorithms.SelectionSort(size,seed), algorithms.BubbleSort(size,seed), algorithms.InsertionSort(size,seed)]
                    algo = algos[algo_idx]
                    algo.refresh()
                elif event.key == pg.K_RIGHT:
                    if algo_idx < len(algos) - 1:
                        algo_idx += 1
                    algo = algos[algo_idx]
                    update(algo)
                elif event.key == pg.K_LEFT:
                    if algo_idx > 0:
                        algo_idx -= 1
                    algo = algos[algo_idx]
                    update(algo)

    pg.quit()


if __name__ == "__main__":
    main(WIN)
