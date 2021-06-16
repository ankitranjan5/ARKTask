import numpy as np
from cv2 import cv2 as cv
import time

IMAGE_PATH = "colored maze.png"

OBSTACLE_COLOR = (0, 0, 0)
FINAL_COLOR = (0, 0, 255)
PATH_COLOR = (127, 0, 0)
TRANSITION_COLOR = (255, 120, 0)

source = (300, 20)
des = (300, 320)


def stopwatch(func):
    def timeWrapper(*args, **kwargs):
        begin = time.time()
        img = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end-begin)
        return img
    return timeWrapper


def computeDist(x, y):
    ans = np.sqrt((x[0]-y[0])**2 +
                  (x[1]-y[1])**2)
    return ans


def isValid(point: tuple = None, img=None) -> bool:
    x, y = point
    if(x >= 0 and y >= 0 and x < img.shape[0] and y < img.shape[1] and
       (img[point] != OBSTACLE_COLOR).any()):
        return True
    return False


@stopwatch
def dijkstraw(image: np.ndarray = None, start: tuple = None, destination: tuple = None):
    img = image.copy()
    h, w = img.shape[:2]
    dist = np.full((h, w), fill_value=np.inf,
                   dtype=np.float32)
    parent = np.arange(h*w).reshape((h, w))

    source = start
    dist[source] = 0

    FREQ = 5
    COUNT = 0
    while source != destination:

        img[source] = FINAL_COLOR

        for i in range(-1, 2):
            for j in range(-1, 2):
                point = (source[0]+i, source[1]+j)
                if(isValid(point, img) and (img[point] != FINAL_COLOR).any()):
                    if(dist[source]+computeDist(source, point) < dist[point]):
                        img[point] = TRANSITION_COLOR
                        parent[point] = source[0] * \
                            w + source[1]
                        dist[point] = dist[source] + \
                            computeDist(source, point)

        mask = (img == TRANSITION_COLOR).all(axis=2)
        b = np.ma.MaskedArray(dist, ~mask)
        index = np.ma.argmin(b, fill_value=np.inf)
        source = index // w, index % w

        if(COUNT % FREQ == 0):
            COUNT = 0
            cv.imshow("Dijkstra", img)
            cv.waitKey(1)
        COUNT += 1

    print("Distance:", dist[destination])
    path(img, parent=parent, dest=destination,
         start=start, windowName="Dijkstra")


@stopwatch
def AStar(image: np.ndarray = None, start: tuple = None, destination: tuple = None):
    img = image.copy()

    h, w = img.shape[:2]
    dist = np.full((h, w), fill_value=np.inf,
                   dtype=np.float32)

    ####################### A_STAR PRECOMPUTE HEURISTIC #######################
    destinationDist = np.full(
        (h, w), fill_value=0, dtype=np.float64)
    for i in range(h):
        for j in range(w):
            destinationDist[i, j] = np.sqrt(
                (i-destination[0])**2 + (j-destination[1])**2)

    parent = np.arange(h*w).reshape((h, w))

    source = start
    dist[source] = 0
    FREQ = 5
    COUNT = 0
    while source != destination:

        img[source] = FINAL_COLOR

        for i in range(-1, 2):
            for j in range(-1, 2):
                point = (source[0]+i, source[1]+j)
                if(isValid(point, img) and (img[point] != FINAL_COLOR).any()):
                    if(dist[source]+computeDist(source, point) < dist[point]):
                        img[point] = TRANSITION_COLOR
                        parent[point] = source[0] * \
                            w + source[1]
                        dist[point] = dist[source] + \
                            computeDist(source, point)

        mask = (img == TRANSITION_COLOR).all(axis=2)

        # ADD HEURISTIC #######
        b = np.ma.MaskedArray(
            dist + destinationDist, ~mask)  # CHECK DOC
            
        index = np.ma.argmin(b, fill_value=np.inf)
        source = index // w, index % w

        if(COUNT % FREQ == 0):
            COUNT = 0
            cv.imshow("A*", img)
            cv.waitKey(1)
        COUNT += 1
    print("Distance:", dist[destination])
    path(img, parent=parent, dest=destination,
         start=start, windowName="A*")


def path(img, parent, dest, start, windowName):
    point = dest
    h, w = img.shape[:2]
    img2 = img.copy()
    while(point != start):
        x, y = parent[point] // w, parent[point] % w
        img2[x, y] = PATH_COLOR
        point = (x, y)
        cv.imshow(windowName, img2)
        cv.waitKey(1)


def main():
    img = cv.imread(IMAGE_PATH, cv.IMREAD_COLOR)
    img = cv.resize(img, (340, 400))
    k = cv.waitKey(0)
    dijkstraw(img, source, des)
    cv.waitKey(0)


if __name__ == "__main__":
    main()
