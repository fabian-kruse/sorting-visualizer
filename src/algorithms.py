import random
import time


class Algorithm():
    def __init__(self,size,time, name,seed):
        self.array = [i+1 for i in range(size)]
        random.Random(seed).shuffle(self.array)
        self.swaps, self.array_accesses = 0,0
        self.time = time
        self.name = name

    def update_display(self,swap1 = None,swap2 = None):
        import visualizer
        visualizer.update(self,swap1,swap2)


    def run(self):
        self.algorithm()

    def refresh(self):
        self.array_accesses = 0
        self.swaps = 0
        self.update_display()



class SelectionSort(Algorithm):
    def __init__(self,size,seed):
        super().__init__(size,0.07,"SelectionSort",seed)

    def algorithm(self):
        for i in range(len(self.array)):
            min_index = i
            for j in range(i + 1,len(self.array)):
                self.array_accesses += 2
                if(self.array[j] < self.array[min_index]):
                    min_index = j
            self.array_accesses += 4
            self.array[i],self.array[min_index] = self.array[min_index], self.array[i]
            self.swaps += 1
            self.update_display(self.array[i],self.array[min_index]) #we don't count access as they are not algorithmic but visual

class BubbleSort(Algorithm):

    def __init__(self,size,seed):
        super().__init__(size,0.01,"BubbleSort",seed)

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array) - 1 - i):
                self.array_accesses += 2
                if self.array[j] > self.array[j + 1]:
                    self.array_accesses += 4
                    self.array[j], self.array[j + 1] = self.array[j + 1],self.array[j]
                self.update_display(self.array[j],self.array[j + 1]) #we don't count access as they are not algorithmic but visual
                self.swaps +=1

class InsertionSort(Algorithm):

    def __init__(self,size,seed):
        super().__init__(size,0.08,"InsertionSort",seed)

    def algorithm(self):
        for i in range(1,len(self.array)):
            self.array_accesses += 1
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array_accesses += 1 #next while iteration
                self.array_accesses += 2
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array_accesses += 1 #first while iteration
            self.array_accesses += 1
            self.array[j + 1] = key
            self.update_display(self.array[key - 1],self.array[i]) #we don't count access as they are not algorithmic but visual
            self.swaps += 1

