# 문제 : 구구단 8단을 출력해주세요.
# 조건 : 숫자 1 이외의 값을 사용할 수 없습니다. 소스코드를 수정해주세요.
# 조건 : for, while문을 사용할 수 없습니다.

"""
출력 양식 
== 8단 ==
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
"""

dan = 7
dan = dan + 1

# 수정가능 시작
i = 1

s = ("== {}단 ==".format(dan))
s += ("\n{} * {} = {}".format(dan, i, dan*i))
s += ("\n{} * {} = 16".format(dan, i+1, dan*(i+1)))
s += ("\n{} * {} = 24".format(dan, i+2, dan*(i+2)))
s += ("\n{} * {} = 32".format(dan, i+3, dan*(i+3)))
s += ("\n{} * {} = 40".format(dan, i+4, dan*(i+4)))
s += ("\n{} * {} = 48".format(dan, i+5, dan*(i+5)))
s += ("\n{} * {} = 56".format(dan, i+6, dan*(i+6)))
s += ("\n{} * {} = 64".format(dan, i+7, dan*(i+7)))
s += ("\n{} * {} = 72".format(dan, i+8, dan*(i+8)))

print(s)

# 수정가능 끝