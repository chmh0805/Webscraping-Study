# re : regular expression(정규 표현식)

import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")
# . (ca.e): 하나의 문자를 의미 > care, cafe, case | caffe (X)
# ^ (^de): 문자열의 시작을 의미 > desk, destination | fade (X)
# $ (se$): 문자열의 끝을 의미 > case, base | seoul (X)

# print(m.group()) # 매치되지 않으면 에러가 발생
# print(m.group(p.match("caffe")))

def print_match(m):
    if m:
        print("m.group() :", m.group()) # 일치하는 문자열 부분만 반환
        print("m.string() :", m.string) # 입력받은 문자열 반환
        print("m.start() :", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() :", m.end()) # 일치하는 문자열의 끝 index
        print("m.span() :", m.span()) # 일치하는 문자열의 시작과 끝 index
        print("\n")
    else:
        print("매칭되지 않음")

# # match : 주어진 문자열의 처음부터 일치하는지 확인
# m1 = p.match("good care")
# m2 = p.match("careless")

# # search : 주어진 문자열 중에 일치하는 것이 있는지 확인
# m1 = p.search("good care")
# m2 = p.search("careless")

# print_match(m1)
# print_match(m2)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 1. p = re.compile("원하는 정규식(형태)")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트"형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, case, cafe (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)