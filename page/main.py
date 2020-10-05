import fifo
import lru
import lfu
def menu():
    print("페이지 교체 알고리즘을 선택하세요")
    print("0. FIFO")
    print("1. LRU")
    print("2. LFU")
    print("3. EXIT")

def get_item():
    num = int(input("페이지 수용량: "))
    order = input("페이지 참조 순서: ").split(" ")
    return num, order

func = [fifo.fifo, lru.lru, lfu.lfu]

if __name__ == "__main__":
    menu()
    while(True):
        choise = input()
        if choise == '0' or choise == '1' or choise == '2':
            page_num, page_chamjo = get_item()
            result = func[int(choise)](page_num, page_chamjo)
            break
        elif choise == "3":
            exit()
        else:
            print("잘못된 입력입니다")

    for i in range(len(page_chamjo)):
        print(page_chamjo[i],end=" ")
    print()

    print("="*(len(page_chamjo)*2-1))

    for i in range(page_num):
        for j in range(len(page_chamjo)):
            print(result[i][j+1], end=" ")
        print()
