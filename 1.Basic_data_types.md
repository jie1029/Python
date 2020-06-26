# 파이썬의 자료형

**파이썬의 모든 것은 객체(object)로 구현되어 있습니다.**

이는 C와 같은 정적 타입 언어(static type language)를 먼저 경험한 분들에게 익숙하지 않은 말일 수 있습니다. 아래의 코드를 인터프리터에서 실행해보세요.

```python
>>> var = 1
>>> dir(var)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>>
```



dir() 은 파이썬에서 제공하는 내장 함수입니다.

해당 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드를 가지고 있는지 나열해 줍니다. 즉, 위의 var 변수는 결국 어떠한 변수와 메소드를 포함하는 객체임을 알 수 있고 파이썬의 모든 것은 객체이므로 dir()을 통해 변수와 메소드를 파악할 수 있습니다.

다시한번 정리하면, 정수 1은 단순한 (일반적으로) 4byte의 데이터가 아닌 어떠한 객체입니다. 이를 조금 더 명확하게 하기위해서는 아래의 코드를 수행할 수 있습니다.

```python
>>> type(var)
<class 'int'>
>>> id(var)  # 매번 다른 결과를 출력합니다.
140736024191376
>>>
```



type()은 파이썬에서 제공하는 내장 함수입니다. 해당 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤  클래스에 속하는지 출력해 줍니다. 즉, 정수 1은 ```'int'``` 라는 이름의 class 임을 확인할 수 있습니다.

당연하게도 id() 또한 파이썬에서 제공하는 내장 함수입니다. 해당 함수는 어떤 객체가 가지는 고유의 값(아이덴티티)를 출력합니다. 여기서 말하는 고유의 값은 모든 객체는 서로 다른 id를 보유함을 의미하며, CPython의 경우 id(x)는 x가 저장된 메모리의 주소입니다.

개념을 명확하게 하기 위하여 아래의 코드를 수행할 수 있습니다.

```python
>>> var = 2
>>> id(var)
140736024191408
>>> var_2 = var
>>> id(var_2)
140736024191408
>>> var_3 = 2
>>> id(var_3)
140736024191408
>>>
```



즉,  동일한 정수의 ```'int'``` 클래스는 내부적으로 하나만 존재하고 그 값은 변하지 않습니다. ```'int'``` 뿐 아니라 ```'float', 'str', 'tuple'``` 등이 값이 변하지않는(immutable) 객체는 모두 동일합니다.

> 이를 통해서 파이썬의 변수는 어떤 객체에 대한 참조임을 알 수 있습니다.

이러한 개념은 앞으로 파이썬을 이용한 프로그래밍을 할 때, 많은 것을 바꿀 수 있으니 꼭 기억하셨으면 좋겠습니다. 또한 변하는(mutable) 객체에 대한 내용은 차후에 진행하겠습니다.



## 정수

인터프리터(혹은 코드)에서 연속된 숫자는 리터럴 정수로 간주합니다. 리터럴 정수란,  변수로서 참조되지 않은 고정된 값을 표현하는 것을 의미합니다.

```python
>>> 0b1010 # binary literal
>>> 100 # decimal literal
>>> 0o310 # octal literal
>>> 0x12c # hexadecimal literal
>>>
```

정수뿐 아니라, 실수, 문자, 논리값 등에도 리터럴은 존재합니다. 대표적으로 ```True, False```가 이에 해당합니다.



이러한 정수는 다른 언어와 마찮가지로 다양한 연산을 제공하며 (당연하게도) 연산의 우선순위가 존재합니다. 그렇다면 그러한 연산은 어떻게 수행될까요? 

객체지향의 개념에 대해서 배우신적이 있다면, 객체 사이에서  '+' 라는 연산은 내부적으로 operator+()와 같은 함수에 의해서 수행됨을 알고 계실 겁니다.  파이썬의 정수도 객체인 만큼 내부적으로 이러한 함수를 호출합니다.

dir()을 출력하신다면  ```__add__, __radd__``` 라고 적힌 함수들을 확인할 수 있습니다. 해당 함수는 파이썬에서 '+' 연산자에 대응하여 정수형 클래스에서 호출하는 함수입니다.



> 추후에 다시 나오겠지만, ``__function__``와 같이 두 개의 언더바(_) 사이에 있는 함수들은 파이썬에서 특별하게 취급됩니다.

 

그 외에도 다음과 같은 내용들은 언젠가 도움이 됩니다.

- divmod()

  ```python
  >>> quotient, remainder = divmod(5, 3)
  >>> quotient
  1
  >>> remainder
  2
  >>>
  ```

  몫과 나머지 연산을 동시에 수행할 수 있습니다.

- 진수

  ```python
  >>> 0b1000
  8
  >>> 0o10
  8
  >>> 0x8
  8
  ```

  일반적으로 생략된 진수는 10진수로 간주합니다. 10진수 이외의 진수는 사용빈도가 낮지만 코드 목적에 따라서 사용되는 경우가 있습니다. 

- 형변환(typecasting)

  정적 타입 언어에서의 형변환은 변수에 할당된 메모리 크기를 바꾸고 각 자료형에 알맞게 바꾸는 것을 의미합니다. 파이썬의 형변환도 동일한 의미를 지니지만 내부적으로 생성자를 호출하게됩니다.

  ```python
  >>> integer = int(3)
  >>> real_number = float(integer)  # 실수형변환
  >>>
  ```

  그러나, 형변환이라는 표현으로 굳어져있습니다.

- 정수의 크기

  다른 정적언어와 일부 동적언어, 심지어 파이썬2에서 ```int```의 크기는 32비트로 제한되어있습니다. 이는 int가 [-2147483648, 2147483647] 범위까지만 저장할 수 있음을 의미합니다. 

  이러한 문제를 해결하기 위해서 더 넓은 범위의 자료형이 사용되지만 파이썬3에서는 ```int```의  크기를 유연하게 바꾸었습니다.

  ```python
  >>> googol = 10**100  # 제곱연산
  10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
  >>> googol * googol
  100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
  >>>
  ```



## 부동소수점수

부동소수점수, 즉 실수는 일반적으로 정수 연산과 매우 유사하게 처리됩니다. 차이점이 있다면 클래스의 명칭이 ```float``` 이라는 점입니다. 

또한 다음과 같은 형태로 형변환이 가능합니다.

```python
>>> float(98)
98.0
>>> float('123.12')
123.12
```

' ' 나 " "로 감싸진 문자열을 실수로 만들 수 있습니다. 이는 정수에서도 동일하게 적용됩니다.



부동소수점수를 사용하면 다음과 같은 문제에 직면하게 됩니다.

```python
>>> n1 = 0.1
>>> n2 = 0.2
>>> n1 + n2 == 0.3  # 등호연산은 True, False와 같은 bool 값을 반환합니다.
False
>>> 1.0000000000000001
1.0
```

이는 n1 + n2가 부동소수점 오차로 인하여 ```0.30000000000000004``` 와 같이 계산되기 때문입니다. 이러한 부동소수점 문제는 일반적으로 다음과 같이 해결합니다.

```python
>>> n1 = 0.1
>>> n2 = 0.2
>>> n3 = n1 + n2
>>> abs(n3 - 0.3) <= 1e-9
True
```

이는 계산 결과와 목표 값의 오차가 1e-9 (0.000000001) 이하라면 True를 반환하도록 합니다. 



해당 문제를 해결하는 혹은 연관된 함수에는 다음이 존재합니다.

* import decimal

  decimal 모듈에 포함된 Decimal 객체는 빠르고 정확한 부동 소수 산술을 지원합니다.

  부동소수점이 갖는 대부분의 문제를 해결할 수 있고 공식 문서에 따르면 float 자료형을 그대로 사용할 때 보다 더 많은 이점이 있다고 합니다.

  ```python
  >>> 1.1 + 2.2
  3.3000000000000003
  >>> 0.1 + 0.2 - 0.4
  -0.09999999999999998
  >>>
  >>> import decimal
  >>> decimal.Decimal('1.1') + decimal.Decimal('2.2')
  Decimal('3.3')
  >>> decimal.Decimal('0.1') + decimal.Decimal('0.2') - decimal.Decimal('0.4')
  Decimal('-0.1')
  >>>
  ```

  단, Decimal 객체를 생성하기 위한 값을 일반 실수형을 넣는다면 동일한 문제가 발생함으로 꼭 문자열로 형변환해야 한다.

* from math import isclose

  isclose 함수는 위에서 abs를 활용한 단순한 오차율 비교를 math 모듈에서 조금 더 엄밀하게 제공하는 함수입니다. decimal을 사용할 만큼 엄격한 상황이 아니라면 이를 활용하는 것이 가장 바람직 합니다.

  ```python
  >>> from math import isclose
  >>> n = 0.1 + 0.2
  >>> isclose(n, 0.3)
  True
  >>>
  ```

* float.as_integer_ratio()

  해당 함수는 근본적으로 부동소수점 문제를 해결하지는 않지만 동일한 결과를 출력하는 (손실 없는) 정수를 반환합니다.

  ```python
  >>> import math
  >>> pi = math.pi
  >>> type(pi)
  float
  >>> pi
  3.141592653589793
  >>> pi.as_integer_ratio()
  (884279719003555, 281474976710656)
  >>> pi == (884279719003555 / 281474976710656)
  True
  >>>
  ```



## 수학함수

위에서 보았듯 ```math``` 모듈에는 다양한 수학에 관련된 함수 및 값이 존재합니다.

*  pi와 e(자연상수)

  ```python
  >>> import math
  >>> math.pi
  3.141592653589793
  >>> math.e
  2.718281828459045
  ```

* 절대값 반환

  ```python
  >>> math.fabs(-98.6)
  -98.6
  ```

* 내림, 올림

  ```python
  >>> math.floor(98.6)
  98
  >>> math.ceil(98.6)
  99
  ```

  참고로 반올림은 내장함수 ```round()```를 사용할 수 있습니다.

* 팩토리얼

  ```python
  >>> math.factorial(0)
  1
  >>> math.factorial(10)
  3628800
  ```

* 로그

  ```python
  >>> math.log(1.0)
  0.0
  >>> math.log(math.e)
  1.0
  ```

  이 때, 로그의 밑은 자연상수 입니다. 밑을 바꾸고 싶다면 두 번째 인자를 입력할 수 있습니다.

  ```python
  >>> math.log(8, 2)
  3.0
  ```

* 거듭제곱

  ```python
  >>> math.pow(2, 3)
  8.0
  >>> 2**3
  8
  ```

그 외에도 제곱근(sqrt) 함수, sin(), asin() 과 같은 일반적인 삼각함수를 모두 제공합니다. 더 자세한 내용을 원한다면 ```import math; dir(math)``` 를 수행하고 공식문서를 참고하세요.



또한 파이썬은 복소수를 지원합니다. 복소수는 아래와 같은 형태로 선언할 수 있습니다.

```python
>>> 5 + 8j
(5+8j)
>>> (1j)**2
(1+0j)
```

여기서 5는 복소수의 실수, 8은 허수를 의미합니다. 즉, j는 -1의 제곱근으로 정의되어 있습니다.

만약 복소수 연산과 같이 복잡한 수학 합수를 원한다면 표준 cmath 모듈을 참고하면 됩니다.



## 문자열

파이썬3에서는 유니코드(Unicode)를 표준으로 지원합니다. 이는 파이썬2와 3가 분리된 가장 큰 이유 중 하나입니다. 파이썬에서 문자열은 시퀀스(Sequence)이자 불변(immutable) 객체입니다.



객체가 불변임을 보이기 위해서는 위와 동일한 과정을 수행할 수 있습니다.

```python
>>> string = 'Snap'
>>> type(string)
<class 'str'>
>>> id(string)
1874018374384
>>> id('Snap')
1874018374384
```



시퀀스는 어떠한 요소(element)들이 연속적으로 이어져있는 자료형을 의미합니다. 일반적으로 배열과 리스트가 이에 해당합니다. 이는 문자열을 인덱싱할 수 있는 것을 의미하지만 불변이기 때문에 값을 변경할 수 없습니다.

```python
>>> string[0]
'S'
>>> string[0:2]
'Sn'
>>> string[0] = 'k'
TypeError: 'str' object does not support item assignment
```



이러한 문자열은 ' ' 나 " "를 사용해서 생성할 수 있습니다. 이렇게 두 가지의 인용부호가 있는 이유는 아래와 같습니다.

```python
>>> string2 = 'She said, "Good Bye"'
>>> print(string2)
She said, "Good Bye"
```



또한 삼중 인용부호를 이용할 수 있습니다. 삼중 인용부호는 한번에 여러 줄의 문자열을 변수에 넣을 수 있으며 공백, 라인끝 문자가 보존됩니다.

```python
>>> string3 = 'You are my best
SyntaxError: EOL while scanning string literal
>>> string3 = '''You are my best
 friend'''
>>> print(string3)
You are my best
 friend
```



문자열은 + 연산을 이용하여 결합하거나, * 연산을 이용하여 복제할 수 있습니다.

```python
>>> string4 = 'TITAN'
>>> string5 = 'RTX'
>>> string4 + string5
'TITANRTX'
>>> string4 * 3
'TITANTITANTITAN'
```

이는 내부적으로 ```__add__ , __mul__``` 함수를 호출하여 동작합니다.

```python
>>> string4.__add__(string5)
'TITANRTX'
>>> string4.__mul__(3)
'TITANTITANTITAN'
```

오브젝트의 내부에 있는 변수나 함수를 활용하고 싶다면 dot(.)을 통해서 접근할 수 있습니다.



위에서 보았듯이 내부의 각 요소, 혹은 여러 요소를 슬라이스 기능을 통해서 접근할 수 있습니다. 대괄호 내부에서 순서대로 시작위치, 종료위치, 스텝을 명시할 수 있습니다. ```[start​ : end : ​step]```

이는 다음의 규칙을 따릅니다.

* [:] 처음부터 끝까지 전체 시퀀스를 추출한다.
* [start:] start 부터 끝까지 시퀀스 추출
* [:end] 처음부터 (end-1) 오프셋까지 시퀀스를 추출한다.
* [start:end] start부터 (end-1) 오프셋까지 시퀀스를 추출한다.
* [start​ : end : step​] start부터 (end-1) 오프셋까지 step 간격으로 시퀀스를 추출한다.
* step의 default 값은 1이다.

```python
>>> alpha = 'abcdefghijklmnopqrstuvwxyz'
>>> alpha[:]
'abcdefghijklmnopqrstuvwxyz'
>>> alpha[20:]
'uvwxyz'
>>> alpha[5:8]
'fgh'
>>> alpha[::2]
'acegikmoqsuwy'
```



이 때, start, end가 음수라면 이는 오른쪽에서부터 오프셋을 계산하게 됩니다.

```python
>>> alpha[-5:-8:-1]
'vut'
>>> alpha[::-1]
'zyxwvutsrqponmlkjihgfedcba'
```

또한 범위를 넘어간다면 오류를 출력하지 않고 해당 영역을 공백으로 처리합니다.



이런 문자열의 길이는 내장함수인 ```len()```을 통해서 확인할 수 있습니다.

```python
>>> len(alpha)
26
```

이 또한 내부 메소드인 ```__len__``` 을 출력하는 것과 동일한 효과를 보입니다.

```python
>>> alpha.__len__()
26
```



문자열은 ```join, split``` 을 이용하여 특정 기준에 맞추어 합치거나 쪼갤 수 있습니다.

```python
>>> string = 'Hi my name is Bob'
>>> string.split(' ')
['Hi', 'my', 'name', 'is', 'Bob']
```

split 함수는 위와 같이 특정 조건에 맞추어 문자열을 쪼개고 이를 리스트로 반환합니다. 가장 일반적으로 쓰이는 경우는 인의적으로 split하기 쉽게 저장한 데이터나 입력에 대한 처리를 진행할 때 입니다.

```python
>>> input_value = input("Input: ")
Input: 10 30 100
>>> input_value
'10 30 100'
>>> split_list = input_value.split(' ')
>>> split_list
['10', '30', '100']
```

이러한 과정은 일반적으로 ```map()``` 함수와 함께 한 줄로 처리됩니다.



join함수는 기준이되는 조건 문자열에서 사용됩니다. 리스트의 각 요소를 하나의 문자열로 묶어서 반환합니다.

```python
>>> blank = ''
>>> blank.join(split_list)
'1030100'
>>> double_colon = '::'
>>> double_colon.join(split_list)
'10::30::100'
```



그 외에도 아래와 같은 함수들이 존재하고 더 많은 함수들이 존재합니다.

* startwith, endswith

  ```python
  >>>  # 문자열의 시작/끝이 입력 문자열인가?
  >>> alpha = 'abcdefghijklmnopqrstuvwxyz'
  >>> alpha.startwith('abc')
  True
  >>> alpha.endswith('xya')
  False
  ```

* find, rfind

  ```python
  >>>  # 문자열에서 입력 문자열을 찾는다.
  >>> decalcomany = 'abcabccbacba'
  >>> decalcomany.find('abc')
  0
  >>> decalcomany.rfind('abc')
  3
  ```

* count

  ```python
  >>>  # 문자열에서 단어의 개수를 반환한다.
  >>> decalcomany.count('ab')
  2
  ```

* isalnum

  ```python
  >>>  # 문자열이 문자와 숫자로만 이루어져있는가?
  >>> decalcomany.isalnum()
  True
  ```

* strip

  ```python
  >>>  # 문자열의 양 끝에서 특정 단어를 삭제한다.
  >>> decalcomany.strip('a')
  'bcabccbacb'
  >>>  # lstrip, rstrip 또한 존재한다.
  ```

* captialize, title

  문자열을 첫번째 단어, 모든 단어의 첫 글자를 대문자로 만든다.

* upper, lower, swapcase

  모든 문자를 대문자(upper)만들거나 소문자(lower)화 한다.

  혹은 서로 바꾼다(swapcase).

* center, ljust, rjust

  ```python
  >>>  # 문자열을 입력한 숫자크기의 공백에서 지정위치(center, left, right)에 삽입한다.
  >>> decalcomany.center(30)
  '         abcabccbacba         '
  >>> decalcomany.rjust(30)
  '                  abcabccbacba'
  >>> decalcomany.ljust(30)
  'abcabccbacba                  '
  ```

  이러한 문자열 정렬(alignment)함수는 차후에 나오는 formatting에 굉장히 편리합니다.

* replace

  ```python
  >>>  # 특정 단어를 입력 단어로 대체합니다.
  >>>  # 기본적으로 모든 단어를 대체하며, 인자를 통해 N 회 반복할 수 있습니다.
  >>> decalcomany.replace('abc', 'kkk')
  'kkkkkkcbacba'
  >>> decalcomany.replace('abc', 'kkk', 1)
  'kkkabcbcabca'
  ```

  이러한 replace() 함수는 대체하고 싶은 정확한 문자열을 안다면 유용하지만 원하지 않는 데이터를 훼손할 수 있음으로 주의해야합니다.

  대체하고 싶은 문자열이 어떤 특수한 조건을 만족한다면 정규표현식(regular expression)을 사용할 수 있습니다. 이는 차후에 다루도록 하겠습니다.

그 외에도 다양한 표준 문자열 함수들이 존재합니다. 

자세한 사항은 표준 문서 웹사이트를 참고함을 추천합니다.

