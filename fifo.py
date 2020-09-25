def get_item():
    num = int(input("페이지 수용 량: "))
    order = input("페이지 참조 순서: ").split(" ")
    return num, order

def fifo(page_num, page_chamjo):
    result = [[' ' for i in range (len(page_chamjo)+1)] for j in range(page_num)]
    how_long = [0 for i in range(page_num)]
    for i in range(len(page_chamjo)):
        go = True
        for k in range(page_num):
            result[k][i+1] = result[k][i]
            how_long[k] += 1
        for j in range(page_num):
            if result[j][i] == page_chamjo[i]:
                go=False
                break
            elif (result[j][i] == ' '):
                result[j][i+1] = page_chamjo[i]
                how_long[j] = 0
                go=False
                break
        if go:
            result[how_long.index(max(how_long))][i+1] = page_chamjo[i]
            how_long[how_long.index(max(how_long))] = 0
    return result

if __name__ == "__main__":
    page_num, page_chamjo = get_item()
    result=fifo(page_num,page_chamjo)
    for i in range(len(page_chamjo)):
        print(page_chamjo[i],end=" ")
    print()
    print("="*(len(page_chamjo)*2-1))
    for j in range(page_num):
        for i in range(len(page_chamjo)):
            print(result[j][i+1], end=" ")
        print()