# ���� : 1���� 1000���̿� �����ϴ� �Ҽ����� ������ ������ּ���.

'''
# �Լ� �̿���� ����, ���� ���� ����
i = 1
c = 0

while i <= 1000:
  
  i_is_prime_number = True

  if i <= 1:
    i_is_prime_number = False
  
  if i_is_prime_number:
    j = 2
    while j < i:
      if i % j == 0:
        i_is_prime_number = False
        break
      j += 1

  if i_is_prime_number:
    c += 1

  i += 1

print("c : {}".format(c))
'''

def is_prime_number(num):
  if num == 1:
    return False

  i = 2
  while i < num:
    if num % i == 0:
      return False
    i += 1
    
  return True

count = 0

i = 1

while i <= 1000:
  if is_prime_number(i):
    count += 1
  i += 1

print("1���� 1000���̿� �����ϴ� �Ҽ����� ���� : {}".format(count))