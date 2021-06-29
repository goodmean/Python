# 문제 - 사용자에게 숫자 2개를 입력받아서, 더한 결과를 출력해주세요.

line = input().strip().split()

i = 0
sum = 0
while i < len(line):
	line[i] = int(line[i])
	sum += line[i]
	i += 1

print(sum)