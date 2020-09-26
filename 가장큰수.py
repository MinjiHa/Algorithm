"""
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
"""

def solution(numbers):
    answer = ''
    mylist = [(str(i)*4,str(i)) for i in numbers] #3이 30보다 앞에 와야 하므로 str(i)*4를 기준으로 sort한다.
    mylist.sort(reverse=True) # 튜플의 첫번째 값 기준으로 sort된다.

    for i in mylist:
        answer+=i[1]
    if sum(numbers)==0: # 0000이 아닌 0이 답으로 나와야 하므로 예외항목을 빼준다.
        answer='0'

    return answer
