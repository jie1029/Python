def time_ellipse(function):
	import time
	def inner_function(*args, **kwargs):
		start  = time.time()
		result = function(*args, **kwargs)
		end    = time.time()
		print(function.__name__, 'time: ', end - start)
		return result
	return inner_function

def sort_by(number):
	return int(str(number)[::-1])
	
@time_ellipse
def number_list_sort_1(numbers):
	'''2.1번 과제, 숫자 정렬 (단 reverse로 읽기)'''
	return sorted(numbers, key=sort_by)
# number_list_sort_1 time:  7.408191680908203

@time_ellipse
def number_list_sort_2(numbers):
	'''2.1번 과제, 숫자 정렬 (단 reverse로 읽기)'''
	return sorted(numbers, key=lambda n: int(str(n)[::-1]))

# 매번 숫자를 문자열로 뒤바꾸는게 불편하다면?
# 혹은 리스트의 길이가 매우 크고, 길이가 길어서 불필요한 리소스를 소모하는 것 같다면?
# number_list_sort_2 time:  7.513734579086304

@time_ellipse
def number_list_sort_3(numbers):
	pair_list = []
	for number in numbers:
		pair_list.append((number, int(str(number)[::-1])))
	pair_list.sort(key=lambda x: x[1])
	
	result = []
	for pair in pair_list:
		result.append(pair[0])
		
	return result
# number_list_sort_3 time:  13.232463598251343
# number_list_sort_3 time:  15.298054933547974 => str -> int 과정 없애면

@time_ellipse
def number_list_sort_4(numbers):
	pair_list = [(n, int(str(n)[::-1])) for n in numbers]
	pair_list.sort(key=lambda x: x[1])
	return [n for n, _ in pair_list]

# number_list_sort_4 time:  12.846261739730835

############################################################################
############################################################################
############################################################################

def solution2_2(the_list = None): #기본인자는 None을 주는것을 권장
	# if the_list == None:
	if isinstance(the_list, type(None)): # 파이썬에서 타입 비교는 isinstance()를 권장
		the_list = []
	
	the_list += [0, 1, 2]
	return the_list

############################################################################
############################################################################
############################################################################

def myCounter_1(numbers, max_value):
	result = {}
	for value in range(max_value):
		result[value] = numbers.count(value)
	return result
	
def myCounter_1(numbers, max_value):
	result = {}
	
	for value in range(max_value):
		result[value] = 0	    
	for value in numbers:
	    result[value] += 1
	    
	return result
	
def myCounter_2(numbers, max_value):
	return {v: numbers.count(v) for v in range(max_value)}

# collection의 Counter를 사용할 수 도 있음 (이번 문제에는 적용하기 조금 애매함)

############################################################################
############################################################################
############################################################################

# 대놓고 set쓰라는 문제

def string_difference(A, B)
	return list(set(A) - set(B))


############################################################################
############################################################################
############################################################################

def solution2_5(A, B):
	length = len(A) if len(A) < len(B) else len(B)
	result = {}
	for index in range(length) 
		result[A[index]] = B[index]
	return result
	
def solution2_5_2(A, B):
	result = {}
	for key, value in zip(A, B):
		result[key] = value
	return result
	
def solution2_5_3(A, B):
	return {key: value for (key, value) in zip(A, B)}
	
def solution2_5_4(A, B):
	return dict(zip(A, B))
	