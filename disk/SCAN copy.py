def scan(init, queue, dir):
    result=0
    save = init
    while queue:
        if (init == 0 or init == 199):
            dir *= -1
            req=0
            result += abs(req-save)
            save = req
            print(init, end=' ')
        if init in queue:
            req = queue.pop(queue.index(init))
            result += abs(req-save)
            save = req
            print(init, end=' ')
        init += dir * 1
    print()
    print(result)

if __name__ == "__main__":
    init = int(input("init: "))
    queue = list(map(int, input("queue: ").split()))
    before = int(input("헤드의 전 위치: "))
    if init == before:
        print("잘못된 입력입니다")
        exit()
    dir = -1 if before > init else 1
    scan(init, queue)