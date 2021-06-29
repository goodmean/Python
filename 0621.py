# div �Լ� ����
def div(a, b):
	return a//b

print("4�� 3���� ���� ���� {} �Դϴ�.".format(div(4, 3)))
# ��� => 4�� 3���� ���� ���� 1 �Դϴ�.

#===================================================================

# ���� : 1���� 1000���̿� �����ϴ� �Ҽ����� ������ ������ּ���.

num = 1
count = 1000

while num <= 1000:    # 1���� 1000���� ���ڸ�
	i = 2                  
	while i < num:      # 2���� �� ������ �� ���ڱ���
		if num % i == 0:  # �������� �������� 0�� �Ǵ� ���������� �Ҽ��� �ƴϹǷ�
			count -= 1      # 1000������ 1�� ����
			break           # �ݺ����� ������. (������ ������ �������� �����鼭 ��� ī��Ʈ)
		i += 1
	num += 1

print(count)

'''
�Լ� ver
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