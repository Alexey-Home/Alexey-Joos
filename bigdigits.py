import sys
import digitss




try:
	digits=input()
	row=0
	while row<7:
		line=""
		column=0
		while column<len(digits):
			number=int(digits[column])
			digit=digitss.Digits[number]
			line+=digit[row]+" "
			column+=1
		print(line)
		row+=1
except IndexError:
        print("usage: bigdigits.py <number>")
except ValueError as err:
	print(err, "in", digits)
		


