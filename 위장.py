"""
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.

입출력 예
clothes	                                                                       return
[[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	5

설명
headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses

"""



def solution(clothes):
    myhash = {}
    for item in clothes:
        c = item[0]
        s = item[1]
        if s not in myhash.keys():
            myhash[s] = [c]
        else : myhash[s] = myhash.get(s) + [c]
    
    answer = 1
    for key in myhash:
        answer *= (len(myhash[key])+1)
    
    return answer-1
  
    
    
"""
옷의 종류를 key로 하는 해시를 만들어 옷을 담고
각 key에 들어가있는 요소의 갯수 +1을 서로 곱한다.
이렇게 되면 해당 종류의 옷을 입지 않는 경우의 수를 함께 구할 수 있다.
다만 '스파이는 하루에 최소 한 개의 의상은 입습니다.'라는 조건이 있기 때문에 구한 값에서 '모든 옷을 입지 않는 경우의 수' 1을 빼서 return 해주어야 한다.

위의 코드는 해시를 사용한 코드이고, Counter를 사용하면 해시를 쓰지 않고도 각 종류의 옷의 갯수를 셀 수 있다.
"""



def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
  
    
    
"""
Counter와 reduce를 사용한 사람의 코드이다.
reduce를 사용하여 for문을 돌리지 않고 각요소+1 의 값을 모두 곱했다.
"""



import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1



"""
위의 코드와 같은 내용이다. 모듈 임포트 부분을 함수 밖으로 빼고 Counter 와 reduce를 한줄로 합쳤다.
"""
