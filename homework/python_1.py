def solution1_1(number):
	from math import log10
	return 1 if number == 0 else int(log10(number)) + 1

def solution1_2(number):
	return len(str(number))
	
def solution1_3(number):
	answer = 0
	while number:
		number //= 10
		answer += 1
	return answer

def solution2_1(word):
	answer = 0
	code   = '22233344455566677778889999'
	for letter in word:
		answer += int(code[ord(letter)-ord('A')])
	return answer + len(word)

def solution2_2(inp):
    a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    b = 0
    for j in range(len(inp)):
        for i in a:
            if inp[j] in i: # in-> 하나의 반복문
                b += a.index(i)+3
                # break
    return b
    
def solution2_3(str):
	str = list(str)
	sum = 0
	for idx in str:
		if idx == 'S' or idx == 'V' or idx == 'Y' or idx == 'Z':
			result = ord(idx)-64
			result = math.ceil(result/3) + 1
		else :
			result = ord(idx)-64
			result = math.ceil(result/3) + 2

		sum += result
	return sum
	
 def solution3_2(str1):
	 if len(str1)%2 == 0:
		back = str1[len(str1):len(str1)//2+1:-1]
		front = str1[:len(str1)//2:]
		if back == front:
			print(True)
		else:
			print(False)
	else:
		back = str1[len(str1):len(str1)//2+2:-1]
		front = str1[:len(str1)//2:]
		if back == front:
			print(True)
		else:
			print(False)

# 1.3 알파벳 좌우대칭 판별
def solution3_1(word):
	pos = len(word)//2
	return word[:pos] == word[-1:-(pos+1):-1]



# 1.4 알파벳 좌우대칭 판별(대소문자)
def solution4_1(word):
	word = word.lower() # upper()
	pos  = len(word)//2
	return word[:pos] == word[-1:-(pos+1):-1]



# 1.5 가운데 글자 반환
def solution5_1(word):
	pos = len(word)//2
	if len(word) % 2:
		return word[pos-1:pos+1]
	else:
		return word[pos]
	# return word[pos-1:pos+1] if len(word) % 2 == 0 else word[pos]

# 1.6 범위 덧셈
def solution6_1(start, end):
	start, end = (start, end) if start < end else (end, start)
	return sum(range(start, end+1))

def my_sum(number):
	number = abs(number)
	return (number+1) * number // 2	

def solution6_2(start, end):
	start, end = (start, end) if start < end else (end, start)
	if end < 0:
		return -my_sum(start) + my_sum(end+1)
	elif start > 0:
		return -my_sum(start-1) + my_sum(end)
	else:
		return my_sum(end)-my_sum(start)	
	

def solution6_3(num1, num2):
    if num1 <= num2:
        return int(num2*(num2+1)/2 - abs((num1*(num1-1)/2)))
    else:
        return solution2(num2, num1)

	
	
	
	
	
	
	
	
	