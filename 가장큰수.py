def solution(numbers):
    answer = ''
    mylist = [(str(i)*4,str(i)) for i in numbers] #3이 30보다 앞에 와야 하므로 str(i)*4를 기준으로 sort한다.
    mylist.sort(reverse=True) # 튜플의 첫번째 값 기준으로 sort된다.

    for i in mylist:
        answer+=i[1]
    if sum(numbers)==0: # 0000이 아닌 0이 답으로 나와야 하므로 예외항목을 빼준다.
        answer='0'

    return answer
