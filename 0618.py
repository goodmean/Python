# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.
def print_dan(dan):
	print("== {}단 ==".format(dan))
	i = 1
	while i <= 9:
		print("{} * {} = {}".format(dan, i, dan * i))
		i += 1

i = 1
while i < 10:
	print_dan(i)
	i += 1

# 문제 : 입력받은 정수의 모든 약수를 출력하는 함수를 구현해주세요.
def print_divisors(num):
	i = 1
	# 구현
	while i <= num:
		if num % i == 0:
			print(i)
		i += 1


print_divisors(1000)