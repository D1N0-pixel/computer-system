def cscan(init, queue):
    result=0
    direc = 1
    while queue:
        init += direc
        result += 1
        if (init == 0 or init == 199):
            direc *= -1
            print(init, end=' ')
        if direc < 0:
            continue
        if init in queue:
            queue.pop(queue.index(init))
            print(init, end=' ')
    print()
    print(result)

if __name__ == "__main__":
    init = int(input("처음 헤드 위치: "))
    queue = list(map(int, input("대기 큐: ").split()))
    cscan(init, queue)