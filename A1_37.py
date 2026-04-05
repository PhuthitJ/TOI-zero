n = int(input())
roman = []
while n >= 1000:
	roman.append('M')
	n -= 1000
if n >= 900:
	roman.append('CM')
	n -= 900
if n >= 500:
	roman.append('D')
	n -= 500
if n >= 400:
	roman.append('CD')
	n -= 400
while n >= 100:
	roman.append('C')
	n -= 100
if n >= 90:
	roman.append('XC')
	n -= 90
if n >= 50:
	roman.append('L')
	n -= 50
if n >= 40:
	roman.append('XL')
	n -= 40
while n >= 10:
	roman.append('X')
	n -= 10
if n >= 9:
	roman.append('IX')
	n -= 9
if n >= 5:
	roman.append('V')
	n -= 5
if n >= 4:
	roman.append('IV')
	n -= 4
while n >= 1:
	roman.append('I')
	n -= 1
print(''.join(roman))
