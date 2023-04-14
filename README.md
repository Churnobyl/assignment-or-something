## Methods of string
- count - 문자열 내의 특정 문자의 개수를 세는 메소드
~~~
text = 'aabbcccdddd'
print(text.count('d'))
~~~
> 출력: 4

<br>

- find - 문자열 내에서 특정 문자열이 **처음 나오는** 위치를 찾아주는 메소드(없으면 -1 리턴)
~~~
text = 'aabbcccdddd'
print(text.find('d'))
~~~
> 출력: 7

<br>

- index - 문자열 내에서 특정 문자열이 **처음 나오는** 위치를 찾아주는 메소드(없으면 ValueError 리턴)
~~~
text = 'aabbcccdddd'
print(text.index('d'))
~~~
> 출력: 7

<br>

- join - 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메소드
~~~
people = ['철수', '영희', '민수']
print('@'.join(people))
~~~
> 출력: "철수@영희@민수"

<br>

- upper - 문자열을 전부 대문자로 바꾸는 메소드
~~~
text = 'aAbBcC'
print(text.upper())
~~~
> 출력: "AABBCC"

<br>

- lower - 문자열을 전부 소문자로 바꾸는 메소드
~~~
text = 'aAbBcC'
print(text.lower())
~~~
> 출력: "aabbcc"

<br>

- replace - 문자열 내의 특정 문자열을 다른 문자열로 바꾸는 메소드
~~~
text = 'aAbBcC'
print(text.replace('A', 'T'))
~~~
> 출력: "aTbBcC"

<br>

- split - 문자열을 특정 문자를 기준으로 나누는 메소드
~~~
text = 'aAbBcC'
print(text.split('b'))
~~~
> 출력: ['aA', 'BcC']

<br>

## Methods of list
- len - 리스트의 길이를 반환하는 함수
~~~
numbers = [1,2,3,4,5,6]
print(len(numbers))
~~~
> 출력: 6

<br>

- del - 리스트의 특정 요소를 삭제하는 연산자
~~~
numbers = [1,2,3,4,5,6]
del numbers[2]
print(numbers)
~~~
> 출력: [1,2,4,5,6]

<br>

- append - 리스트의 맨 뒤에 새로운 요소를 추가하는 메소드
~~~
numbers = [1,2,3,4,5,6]
print(numbers.append(7))
~~~
> 출력: [1,2,4,5,6,7]

<br>

- sort - 리스트를 오름차순으로 정렬하는 메소드
~~~
numbers = [3,2,1,4,3]
numbers.sort()
print(numbers)
~~~
> 출력: [1,2,3,3,4]

<br>

- sort - 리스트의 요소 순서를 반대로 뒤집는 메소드
~~~
numbers = [3,2,1,4,3]
numbers.reverse()
print(numbers)
~~~
> 출력: [3,4,1,2,3]

<br>

- index - 리스트에서 특정 요소의 인덱스를 반환하는 메소드
~~~
shopping_bag = ['chicken', 'apple', 'grape', 'beef']
print(shopping_bag.index('grape'))
~~~
> 출력: 2

<br>

- insert - 리스트의 특정 위치에 요소를 삽입하는 메소드
~~~
shopping_bag = ['chicken', 'apple', 'grape', 'beef']
shopping_bag.insert(2, 'soju')
print(shopping_bag)
~~~
> 출력: ['chicken', 'apple', 'soju', 'grape', 'beef']

<br>

- remove - 리스트에서 특정 요소를 제거하는 메소드
~~~
shopping_bag = ['chicken', 'apple', 'grape', 'beef']
shopping_bag.remove('apple')
print(shopping_bag)
~~~
> 출력: ['chicken', 'grape', 'beef']

<br>

- pop - 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메소드
~~~
shopping_bag = ['chicken', 'apple', 'grape', 'beef']
popped_element = shopping_bag.pop('apple')
print(popped_element)
print(shopping_bag)
~~~
> 출력: apple / ['chicken', 'grape', 'beef']

<br>

- extend - 리스트를 확장하여 새로운 요소들을 추가하는 메소드 (= +=)
~~~
shopping_bag = ['chicken', 'apple', 'grape', 'beef']
shopping_bag.extend(['cherry', 'carrot'])
~~~
> 출력: ['chicken', 'apple', 'grape', 'beef', 'cherry', 'carrot']

<br>

## Methods of dictionary

- del - 딕셔너리에서 특정 요소를 삭제
~~~
my_dict = {'chicken' : 1, 'beef' : 2, 'pork' : 3}
del my_dict['beef']
print(my_dict)
~~~
> 출력: {'chicken' : 1, 'pork' : 3}

<br>

- items - 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
~~~
my_dict = {'chicken' : 1, 'beef' : 2, 'pork' : 3}
print(my_dict.items())
~~~
> 출력: dict_items([('chicken', 1), ('beef', 2), ('pork', 3)])

<br>

- clear - 딕셔너리의 모든 요소를 삭제
~~~
my_dict = {'chicken' : 1, 'beef' : 2, 'pork' : 3}
my_dict.clear()
print(my_dict)
~~~
> 출력: {}

<br>

- get - 딕셔너리에서 지정한 키에 대응하는 값을 반환
~~~
my_dict = {'chicken' : 1, 'beef' : 2, 'pork' : 3}
print(my_dict.get('beef'))
print(my_dict.get('gogi'))
~~~
> 출력: 2 / None

<br>

- in - 해당 키가 딕셔너리 안에 있는지 확인
~~~
my_dict = {'chicken' : 1, 'beef' : 2, 'pork' : 3}
print('chicken' in my_dict)
print('gogi' in my_dict)
~~~
> 출력: True / False

<br>





