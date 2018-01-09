import calendar
print(calendar.month(2017,7))

from math import pi
print(pi)

a = 1
b = "hoge"
c = 'fuga'
d = True
e = None

def myFunc(v1, v2):
	return v1 + v2

ret = myFunc(a, 20);

a += 1
a = 3 // 2
a = 2 ** 3 # 8

print("---------------------- 3 if")
"hoge" if a == 8 else "fuga"

str = "hello" + "world"
list1 = "ab.cd.ef".split(".") 
print(list1)

print("---------------------- list & dictionary")
list2 = ["hoge", 10, True]
dict1 = {"k1":"v1", "k2":"v2", "k3":"v3", }
print(dict1["k1"])

print("---------------------- tuple")
tuple1 = ("hoge", 999, False)
print(tuple1[1])

print("---------------------- set")
set1 = {1,2,3,4,1,3,4,}
print(set1)

class Member:
	# member val
	LANG = "JP"
	# cons
	def __init__(self):
		self.name = ""
	# getter
	def getName(self):
		return self.name
	# setter
	def setName(self, name):
		self.name = name

print("---------------------- class")
taro = Member()
taro.setName("taro")
print(taro.getName())
print(Member.LANG)

print("---------------------- error handling")
try:
	x = 10 / 0
except Exception as e:
	print(e) # division by zero
else:
	print("exception have not raise")
finally:
	print("finally")

def hogehoge():
	pass # not implementation

print("---------------------- closure")
def counter():
	count = 0

	def inner_counter():
		nonlocal count
		count += 1
		return count

	return inner_counter

cnt = counter()
print(cnt())
print(cnt())
print(cnt())
