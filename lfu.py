def get_item():
    num = int(input("페이지 수용 량: "))
    order = input("페이지 참조 순서: ").split(" ")
    return num, order

def lfu(page_num,page_chamjo):
    result = [[' ' for i in range (len(page_chamjo)+1)] for j in range(page_num)]
    freq = dict()
    for i in range(len(page_chamjo)):
        go = True
        if freq.get(page_chamjo[i]):
            freq[page_chamjo[i]] += 1
        else:
            freq[page_chamjo[i]] = 1
        for k in range(page_num):
            result[k][i+1] = result[k][i]
        for j in range(page_num):
            if result[j][i] == page_chamjo[i]:
                go=False
                break
            elif (result[j][i] == ' '):
                result[j][i+1] = page_chamjo[i]
                go=False
                break
        if go:
            min_order=list()
            min_val = min(list(freq.values()))
            for j in range(i+1)[::-1]:
                if freq[page_chamjo[j]] == min_val:
                    if not page_chamjo[j] in min_order:
                        min_order.append(page_chamjo[j])
            for j in range(page_num):
                if result[j][i] == min_order[-1]:
                    result[j][i+1] = page_chamjo[i]
                    break
    return result

if __name__ == "__main__":
    page_num, page_chamjo = get_item()
    result=lfu(page_num,page_chamjo)
    for i in range(len(page_chamjo)):
        print(page_chamjo[i],end=" ")
    print()
    print("="*(len(page_chamjo)*2-1))
    for j in range(page_num):
        for i in range(len(page_chamjo)):
            print(result[j][i+1], end=" ")
        print()