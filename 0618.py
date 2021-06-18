# ���� : �Լ��� ����ؼ� �ڵ差�� Ȯ �ٿ��ּ���.
def print_dan(dan):
	print("== {}�� ==".format(dan))
	i = 1
	while i <= 9:
		print("{} * {} = {}".format(dan, i, dan * i))
		i += 1

i = 1
while i < 10:
	print_dan(i)
	i += 1

# ���� : �Է¹��� ������ ��� ����� ����ϴ� �Լ��� �������ּ���.
def print_divisors(num):
	i = 1
	# ����
	while i <= num:
		if num % i == 0:
			print(i)
		i += 1


print_divisors(1000)