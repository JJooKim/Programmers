import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    s1, s2 = 0, 0
    while(len(scoville) != 0):
        s1 = hq.heappop(scoville)
        if s1 >= K or len(scoville) == 0: #확인
            if s1 >= K:
                return answer
            else:
                return -1
            
        
        s2 = hq.heappop(scoville)
        hq.heappush(scoville, (s1 + (s2*2)))
        answer +=1
    
    return -1
    