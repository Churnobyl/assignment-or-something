## Methods of string
- count - 문자열 내의 특정 문자의 개수를 세는 메소드
~~~
text = 'aabbcccdddd'
print(text.count('d'))
~~~
> 출력: 4

- find - 문자열 내에서 특정 문자열이 **처음 나오는** 위치를 찾아주는 메소드(없으면 -1 리턴)
~~~
text = 'aabbcccdddd'
print(text.find('d'))
~~~
> 출력: 7

- index - 문자열 내에서 특정 문자열이 **처음 나오는** 위치를 찾아주는 메소드(없으면 ValueError 리턴)
~~~
text = 'aabbcccdddd'
print(text.index('d'))
~~~
> 출력: 7

- join - 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메소드
~~~
people = ['철수', '영희', '민수']
print('@'.join(people))
~~~
> 출력: "철수@영희@민수"

- upper - 문자열을 전부 대문자로 바꾸는 메소드
~~~
text = 'aAbBcC'
print(text.upper())
~~~
> 출력: "AABBCC"

- lower - 문자열을 전부 소문자로 바꾸는 메소드
~~~
text = 'aAbBcC'
print(text.lower())
~~~
> 출력: "aabbcc"

- replace - 문자열 내의 특정 문자열을 다른 문자열로 바꾸는 메소드
~~~
text = 'aAbBcC'
print(text.replace('A', 'T'))
~~~
> 출력: "aTbBcC"

- split - 문자열을 특정 문자를 기준으로 나누는 메소드
~~~
text = 'aAbBcC'
print(text.split('b'))
~~~
> 출력: ['aA', 'BcC']

## Methods of list
- len - 리스트의 길이를 반환하는 함수
~~~
numbers = [1,2,3,4,5,6]
print(len(numbers))
~~~
> 출력: 6

- len - 리스트의 길이를 반환하는 함수
~~~
numbers = [1,2,3,4,5,6]
del numbers[2]
print(numbers)
~~~
> 출력: [1,2,4,5,6]

