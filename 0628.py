# ���� - ����ڿ��� ���� 2���� �Է¹޾Ƽ�, ���� ����� ������ּ���.

line = input().strip().split()

i = 0
sum = 0
while i < len(line):
	line[i] = int(line[i])
	sum += line[i]
	i += 1

print(sum)