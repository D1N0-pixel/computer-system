def get_item():
    num = int(input("페이지 수용 량: "))
    order = input("페이지 참조 순서: ").split(" ")
    return num, order

def lru(page_num,page_chamjo):
    result = [[' ' for i in range (len(page_chamjo)+1)] for j in range(page_num)]

    for i in range(len(page_chamjo)):
        go = True
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
            cnt=1
            resent = set()
            while len(resent) < page_num - 1:
                for j in range(page_num):
                    if page_chamjo[i-cnt] == result[j][i]:
                        resent.add(page_chamjo[i-cnt])
                cnt+=1
            for j in range(page_num):
                if not result[j][i] in resent:
                    result[j][i+1] = page_chamjo[i]
    return result
if __name__ == "__main__":
    page_num, page_chamjo = get_item()
    result=lru(page_num,page_chamjo)
    for i in range(len(page_chamjo)):
        print(page_chamjo[i],end=" ")
    print()
    print("="*(len(page_chamjo)*2-1))
    for j in range(page_num):
        for i in range(len(page_chamjo)):
            print(result[j][i+1], end=" ")
        print()
