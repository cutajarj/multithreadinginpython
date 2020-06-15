import threading
import time

controller = threading.Condition()


def all_free(intersections_to_lock):
    for it in intersections_to_lock:
        if it.locked_by >= 0:
            return False
    return True


def lock_intersections_in_distance(id, reserve_start, reserve_end, crossings):
    intersections_to_lock = []
    for crossing in crossings:
        if reserve_end >= crossing.position >= reserve_start and crossing.intersection.locked_by != id:
            intersections_to_lock.append(crossing.intersection)

    controller.acquire()
    while not all_free(intersections_to_lock):
        controller.wait()

    for intersection in intersections_to_lock:
        intersection.locked_by = id
        time.sleep(0.01)
    controller.release()


def move_train(train, distance, crossings):
    while train.front < distance:
        train.front += 1
        for crossing in crossings:
            if train.front == crossing.position:
                lock_intersections_in_distance(train.uid, crossing.position,
                                               crossing.position + train.train_length, crossings)
            back = train.front - train.train_length
            if back == crossing.position:
                controller.acquire()
                crossing.intersection.locked_by = -1
                controller.notify_all()
                controller.release()
        time.sleep(0.01)
