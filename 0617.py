for dan in range(2,10):
	print("== {}´Ü ==\n".format(dan))
	for i in range(2,10):
		print("= {}-{} ´Ü =".format(dan, i))
		for j in range(2,10):
			print("{} x {} x {} = {}".format(dan, i , j, dan*i*j))
		print("")
