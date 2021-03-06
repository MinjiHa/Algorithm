"""

트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다.
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간 	다리를 지난 트럭	  다리를 건너는 트럭	  대기 트럭
0	                []         	[]        	      [7,4,5,6]
1~2	                []	        [7]	              [4,5,6]
3	                [7]	        [4]	              [5,6]
4	                [7]       	[4,5]     	      [6]
5	                [7,4]     	[5]       	      [6]
6~7	                [7,4,5]         [6]                   []
8                	[7,4,5,6]	[]	              []
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리 길이 bridge_length,
다리가 견딜 수 있는 무게 weight,
트럭별 무게 truck_weights가 주어집니다.
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

"""

def solution(bl, w, tw):
    answer = 0
    bridge = []
    while len(tw):
        answer+=1
        if len(bridge):
            for b in bridge:
                b[0]-=1
            if bridge[0][0]<=0:
                bridge.pop(0)
            if sum([b[1] for b in bridge])+tw[0]<=w:
                bridge.append([bl,tw.pop(0)])
        else:
            bridge.append([bl,tw.pop(0)])

    if len(bridge):
        answer+=bridge[-1][0]
    
    return answer
    
    
"""
while문을 돌때마다 1초가 지난다고 가정하였기 때문에 대기트럭배열에 트럭이 있는 한 시간은 계속 지나간다.
시간이 지날 때마다 총 시간 answer는 1씩 증가하고
다리위의 각 트럭무게 앞에 붙은 시간은 다리길이로 시작해서 1씩 감소한다.
각 트럭이 가지고 있는 시간이 0이 될 때 다리를 다 건넌 것이 되므로
while문의 시작에(bridge의 요소가 있을 때) bridge위의 트럭중 다리위 시간이 0초 남은 요소를 pop으로 제거해준다.
그 후 다리를 건너는 트럭 배열 bridge위의 트럭 무게의 합과 대기0번 트럭무게의 합이 다리의 최대 하중 w를 넘지 않는다면 대기0번을 다리에 실어주는 방법으로 문제를 풀었다.
트럭이 모두 출발하여 대기트럭의 배열이 비게 되었을 때,
다리에 오른 트럭 중 가장 마지막 트럭에게 필요한 시간을 answer에 더해주면 모든 트럭이 다리를 건너는 데 필요한 총 시간이 나온다.
"""

# 효율성을 개선한 코드

def solution(bl, w, tw):
    answer = 0
    bridge = []
    while len(tw):
        answer+=1
        if len(bridge):
            if bridge[0][0]<=1:
                bridge.pop(0)
            for b in bridge:
                b[0]-=1
            if sum([b[1] for b in bridge])+tw[0]<=w:
                bridge.append([bl,tw.pop(0)])
        else:
            bridge.append([bl,tw.pop(0)])

    if len(bridge):
        answer+=bridge[-1][0]
    
    return answer

"""
while문을 들어왔을 때는 이미 1초가 지나간 상황으로, 다리위의 트럭 중 0초가 아닌 1초가 남아있는 트럭을 미리 제거해 준 뒤(어치피 다음코드로 1을 빼서 0이 될 것이기 때문)
다리위의 모든 트럭에 대해서 다리를 지나기 위해 남아있는 시간을 1씩 빼주게 되면 미리 제거된 트럭에 대해서는 시간을 빼주는 연산을 할 필요가 없으므로 위의 코드보다 조금더 효율이 좋아진다.
"""
