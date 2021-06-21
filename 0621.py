# div 함수 구현
def div(a, b):
	return a//b

print("4를 3으로 나눈 몫은 {} 입니다.".format(div(4, 3)))
# 출력 => 4를 3으로 나눈 몫은 1 입니다.

#===================================================================

# 문제 : 1부터 1000사이에 존재하는 소수들의 개수를 출력해주세요.

num = 1
count = 1000

while num <= 1000:    # 1부터 1000까지 숫자를
	i = 2                  
	while i < num:      # 2부터 그 숫자의 전 숫자까지
		if num % i == 0:  # 나눴을때 나머지가 0이 되는 수가있으면 소수가 아니므로
			count -= 1      # 1000개에서 1을 빼고
			break           # 반복문을 나간다. (나가지 않으면 다음수도 나누면서 계속 카운트)
		i += 1
	num += 1

print(count)

'''
함수 ver
'''

def count_prime_number(start_num, end_num):
	count = end_num - start_num + 1
	while start_num <= end_num:
		i = 2
		while i < start_num:
			if start_num % i == 0:
				count -= 1
				break
			i += 1
		start_num += 1
	
	return count

print(count_prime_number(1,1000))