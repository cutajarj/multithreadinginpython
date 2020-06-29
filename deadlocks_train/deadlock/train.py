import random

import time


def move_train(train, distance, crossings):
    while train.front < distance:
        train.front += 1
        for crossing in crossings:
            if train.front == crossing.position:
                crossing.intersection.mutex.acquire()
                crossing.intersection.locked_by = train.uid
            back = train.front - train.train_length
            if back == crossing.position:
                crossing.intersection.locked_by = -1
                crossing.intersection.mutex.release()
        time.sleep(0.01)
