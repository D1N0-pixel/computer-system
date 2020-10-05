import FIFO
import SSTF
import SCAN
import CSCAN

def menu():
    print("디스크 스케줄링 방식을 선택하세요")
    print("0. FIFO")
    print("1. SSTF")
    print("2. SCAN")
    print("3. C-SCAN")

def get_item():
    init = int(input("처음 헤드 위치: "))
    queue = list(map(int, input("대기 큐: ").split()))
    return init, queue

func = [FIFO.fifo, SSTF.sstf, SCAN.scan, CSCAN.cscan]

if __name__ == "__main__":
    menu()
    while(True):
        choise = input()
        if choise == '0' or choise == '1' or choise == '3':
            init, queue = get_item()
            func[int(choise)](init, queue)
            break
        if choise == '2':
            init, queue = get_item()
            before = int(input("헤드의 전 위치: "))
            if init == before:
                print("잘못된 입력입니다")
                break
            dir = -1 if before > init else 1
            func[int(choise)](init, queue, dir)
            break
        else:
            print("잘못된 입력입니다")