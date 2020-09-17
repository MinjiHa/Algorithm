"""

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

입출력 예
numbers	    return
"17"	      3
"011"	      2

예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
(11과 011은 같은 숫자로 취급합니다.)

"""

import itertools

def solution(numbers):
    n = list(numbers)
    myn = list(numbers)
    answer=0

    for i in range(2,len(n)+1):
        myn+=list(map(''.join, itertools.permutations(n,i)))
    myn = list(set(int(k) for k in myn))

    for i in myn:
        isP = True
        for j in range(2,int(i**0.5+1)):
                if i%j==0:
                    isP=False
                    break
        if (i>2 and isP) or i==2:
            answer+=1
    return answer


"""
처음엔 myn = n 으로 얕은 복사를 했다가 애를 먹었다.
=으로 복사하면 참조가 되므로 주의하자.
"""
