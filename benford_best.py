import re


def removeCommentAndTrim(s):
    return re.sub(re.compile(r'\(\*.+\*\)'), '', s).strip()


def isNumber(s):
    return s.isdigit()


with open('sunspots.txt') as infile:
    lines = infile.readlines()

##lines = [removeCommentAndTrim(line) for line in lines]
lines = list(map(removeCommentAndTrim, lines))
##prob_lines = [line for line in lines if not re.fullmatch(re.compile(r'\d+'), line)]
##prob_lines = [line for line in lines if not line.isdigit()]
##prob_lines = [line for line in lines if not isNumber(line)]
lines = list(filter(isNumber, lines))

nums = [num[0] for num in lines]

num1s = 0
num2s = 0
num3s = 0
num4s = 0
num5s = 0
num6s = 0
num7s = 0
num8s = 0
num9s = 0

for num in nums:
    if num == '1':
        num1s = num1s + 1
    elif num == '2':
        num2s = num2s + 1
    elif num == '3':
        num3s = num3s + 1
    elif num == '4':
        num4s = num4s + 1
    elif num == '5':
        num5s = num5s + 1
    elif num == '6':
        num6s = num6s + 1
    elif num == '7':
        num7s = num7s + 1
    elif num == '8':
        num8s = num8s + 1
    elif num == '9':
        num9s = num9s + 1

print('1s', str(num1s))
print('2s', str(num2s))
print('3s', str(num3s))
print('4s', str(num4s))
print('5s', str(num5s))
print('6s', str(num6s))
print('7s', str(num7s))
print('8s', str(num8s))
print('9s', str(num9s))
