def fcfs(init, queue):
    result = 0
    while queue:
        req = queue.pop(0) 
        result += abs(init - req)
        init = req
        print(init, end=" ")
    print()
    print(result)

if __name__ == "__main__":
    init = int(input("처음 헤드 위치: "))
    queue = list(map(int, input("대기 큐: ").split()))
    fcfs(init, queue)
