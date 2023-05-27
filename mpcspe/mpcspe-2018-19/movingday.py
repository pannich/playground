import math

if __name__ == "__main__":
    no_box, V = list(map(int,input().split()))

    vmax = 0

    for n in range(no_box):
        boxes = list(map(int,input().split(" ")))
        print(boxes)
        v = math.prod(boxes)

        if v >= vmax:
            vmax = v

    d = vmax - V

    print(d)
