for dan in range(2,10):
	print("== {}�� ==\n".format(dan))
	for i in range(2,10):
		print("= {}-{} �� =".format(dan, i))
		for j in range(2,10):
			print("{} x {} x {} = {}".format(dan, i , j, dan*i*j))
		print("")
