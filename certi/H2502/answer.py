import heapq
from typing import List

# 전역 변수로 adjacency list 선언
adj = [[] for _ in range(1005)]

def init(N: int, K: int, sCity: List[int], eCity: List[int], mLimit: List[int]) -> None:
    """
    그래프를 초기화하는 함수
    N: 도시 수
    K: 도로 수  
    sCity: 시작 도시 배열
    eCity: 끝 도시 배열
    mLimit: 용량 제한 배열
    """
    # adjacency list 초기화
    for i in range(1005):
        adj[i].clear()
    
    # 도로 정보 추가 (양방향)
    for i in range(K):
        u = sCity[i]
        v = eCity[i]
        wt = mLimit[i]
        adj[u].append((v, wt))
        adj[v].append((u, wt))

def add(sCity: int, eCity: int, mLimit: int) -> None:
    """
    새로운 도로를 추가하는 함수
    """
    u = sCity
    v = eCity
    wt = mLimit
    adj[u].append((v, wt))
    adj[v].append((u, wt))

def calculate(sCity: int, eCity: int, M: int, mStopover: List[int]) -> int:
    """
    시작 도시에서 목적지까지의 최대 용량 경로를 찾는 함수
    sCity: 시작 도시
    eCity: 목적지 도시
    M: 경유지 수
    mStopover: 경유지 배열
    """
    # 거리 배열 초기화 (최대 용량을 저장)
    dist = [float('-inf')] * 1005
    
    # 우선순위 큐 (최대 힙)
    pq = []
    
    # 시작 도시에서 직접 연결된 노드들 초기화
    for node, wt in adj[sCity]:
        heapq.heappush(pq, (-wt, node))  # 음수로 저장하여 최대 힙 구현
        dist[node] = wt
    
    dist[sCity] = float('inf')
    
    # 다익스트라 알고리즘 (최대 용량 버전)
    while pq:
        neg_wt, node = heapq.heappop(pq)
        wt = -neg_wt  # 다시 양수로 변환
        
        # 현재 노드에서 인접한 모든 노드 확인
        for current_node, current_wt in adj[node]:
            # 경로상 최소 용량이 현재까지의 최대 용량
            weight_carry = min(wt, current_wt)
            
            if dist[current_node] < weight_carry:
                heapq.heappush(pq, (-weight_carry, current_node))
                dist[current_node] = weight_carry
    
    # 목적지와 모든 경유지 중 최소 용량 찾기
    maxi = float('inf')
    
    for i in range(M):
        x = mStopover[i]
        maxi = min(maxi, dist[x])
    
    maxi = min(maxi, dist[eCity])
    
    # 경로가 없는 경우
    if maxi == float('-inf'):
        return -1
    
    return int(maxi)