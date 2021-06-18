import random

start = input('請輸入開始數字：')
end = input('請輸入結束數字：')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜一個數字：')
	num = int(num)
	if num == r:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小') 
	print('這是你猜的第', count, '次')