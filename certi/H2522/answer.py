from collections import defaultdict
import heapq
  
def init(N, K, mId, sCity, eCity, mTime):
    global nN, graph, road_profile
    nN = N
    graph, road_profile = defaultdict(list), defaultdict(list)
    for i in range(K):
        graph[sCity[i]].append((eCity[i],mTime[i]))
        road_profile[mId[i]] = (sCity[i],eCity[i],mTime[i])
    #print(dict(graph))
  
  
def add(mId, sCity, eCity, mTime):
    #print("ADD", sCity, eCity, mTime)
    graph[sCity].append((eCity,mTime))
    road_profile[mId] = (sCity,eCity,mTime)
    #print(dict(graph))
  
  
def remove(mId):
    #print("REMOVE",mId)
    (sCity, eCity, mTime) = road_profile[mId]
    del road_profile[mId]
    graph[sCity].remove((eCity,mTime))
    #print(dict(graph))
  
  
def calculate(sCity, eCity):
    #print("CALCULATE",sCity, eCity)
    def bfs(start, end, skip=None):
        INF = 999999999
        distances = [INF]*nN
        visited = [False]*nN
        distances[start]=0
        pq = [(0,start)]
        prev=[-1]*nN
        while pq:
            current_dist, current_node = heapq.heappop(pq)
              
            if visited[current_node] : continue
            if current_node == end:
                path = []
                t = current_node
                while t != -1:
                    path.append(t)
                    t = prev[t]
                return current_dist, path
            for new_node, weight in graph[current_node]:
                if skip != None and current_node == skip[0] and new_node == skip[1]: 
                    continue# 이렇게하면 끊어진 도로를 피해서 스킵 노드로 가능 경우가 계산이 안됨. 노드를 제외하는 것이 아니라 경로를 제외해야 함. 
                new_dist = distances[current_node] + weight
                if new_dist < distances[new_node]:
                    distances[new_node] = new_dist
                    heapq.heappush(pq, (new_dist, new_node))
                    prev[new_node] = current_node
  
        return -1,[]
      
    min_time, min_path = bfs(sCity, eCity, None)
  
    if min_time == -1: 
        #print(-1)
        return -1
      
    ans = -1
    for i in range(1, len(min_path)):
        new_min_time, new_path = bfs(sCity, eCity, (min_path[i],min_path[i-1]))
        if new_path == []:
            ans = -1
            return ans
        ans = max(ans, new_min_time)
        #print('\tSkip',min_path[i],ans,new_path)
  
    if ans != -1:
         #print(ans-min_time, min_path)
         return ans-min_time
    #print(ans)
    return ans