# 전화번호 목록
# 접두어 맞는 지 찾기

# 내 풀이
class Num:
    def __init__(self):
        self.link = [None]*10
        self.end = False


def hash2(phone_book):
    # 종료: 접두어 맞는 것 하나만 찾으면.
    phone_book = sorted(phone_book)
    head = Num()
    for ph in phone_book:
        temp = head
        for i in range(len(ph)):
            n = int(ph[i])
            if temp.link[n] != None and temp.link[n].end == True:
                return False
            elif temp.link[n] == None:
                temp.link[n] = Num()
            temp = temp.link[n]
        temp.end = True

    return True

# 다른 사람 풀이1
def ans_hash2_1(phone_book):
    # zip 이용하고 startwith
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True

# 다른 사람 풀이2
def ans_hash2_2(phone_book):
    # hash 제대로 이용
    hash_map = {}
    for ph_num in phone_book:
        hash_map[ph_num] = 1
    for ph_num in phone_book:
        temp = ""
        for n in ph_num:
            temp += n
            if temp in hash_map and temp != ph_num:
                return False
    return True


phone_book = ['119', '97674223', '1195524421']
print(ans_hash2_1(phone_book))
