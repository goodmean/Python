# ���� : ����Ʈ�� ������� '��', 'ȭ', '��', '��', '��'�� �ѹ��� ����ּ���. 'ȭ'�� ����Ʈ �ȿ� �ִ��� if������ üũ ��, �ִٸ� �������ּ���.

a = ['��', 'ȭ', '��', '��', '��']

if 'ȭ' in a:
	a.remove('ȭ')

print(a)

#v1
a = ['��', 'ȭ', '��', '��', '��']
a.remove('��')
print(a)

#v2
a = ['��', 'ȭ', '��', '��', '��']
del a[4]
print(a)

#v3
a = ['��', 'ȭ', '��', '��', '��']
del a[a.index('��')]
print(a)