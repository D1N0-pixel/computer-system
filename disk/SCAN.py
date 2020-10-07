def scan(init, queue, direc):
    while(init in queue):
        print(queue.pop(queue.index(init)),end=" ")
    result=0
    save = init
    while queue:
        init += direc
        result += 1
        if (init == 0 or init == 199):
            direc *= -1
            print(init, end=' ')
        if init in queue:
            queue.pop(queue.index(init))
            print(init, end=' ')
    print()
    print(result)

if __name__ == "__main__":
    init = int(input("처음 헤드 위치: "))
    queue = list(map(int, input("대기 큐: ").split()))
    before = int(input("헤드의 전 위치: "))
    if init == before:
        print("잘못된 입력입니다")
        exit()
    direc = -1 if before > init else 1
    scan(init, queue, direc)