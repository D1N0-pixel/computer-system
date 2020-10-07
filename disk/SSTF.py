def choose(present, queue):
    diff = list(map(lambda x:abs(x-present), queue))
    return queue[diff.index(min(diff))]

def sstf(init, queue):
    while(init in queue):
        print(queue.pop(queue.index(init)),end=" ")
    result = 0
    nexttrack = choose(init, queue)
    direc = 1 if init < nexttrack else -1
    while queue:
        init += direc
        result += 1
        if init == nexttrack:
            queue.pop(queue.index(init))
            if queue:
                nexttrack = choose(init, queue)
            direc = 1 if init < nexttrack else -1
            print(init, end=" ")
    print()
    print(result)

if __name__ == "__main__":
    init = int(input("처음 헤드 위치: "))
    queue = list(map(int, input("대기 큐: ").split()))
    sstf(init, queue)