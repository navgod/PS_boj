import heapq
n = 0
def init(N, K, sCity, eCity, mLimit):
	global cities, adj, n
	n = N
	adj = [[] for _ in range(N)]
	for i in range(K):
		u, v, d = sCity[i], eCity[i], mLimit[i]
		adj[u].append((d,v))
		adj[v].append((d,u))
 
def add(sCity, eCity, mLimit):
	u , v, d = sCity, eCity, mLimit
	adj[u].append((d,v))
	adj[v].append((d,u))

def calculate(sCity, eCity, M, mStopover):
	dist = [float('-inf')]*n
	dist[sCity] = float('inf')
	pq = []
	
	for d, node in adj[sCity]:
		heapq.heappush(pq, (-d,node))
		dist[node] = d
	
    
	while pq:
		nwt, node = heapq.heappop(pq)
		wt = -nwt

		for next_weight, next_node in adj[node]:
			weight_carry = min(wt, next_weight)

			if dist[next_node] < weight_carry:
				heapq.heappush(pq, (-weight_carry,next_node))
				dist[next_node] = weight_carry
	
	maxi = float('inf')

	for i in range(M):
		x = mStopover[i]
		maxi = min(maxi, dist[x])
	
	maxi = min(maxi,dist[eCity])

	if maxi == float('-inf'):
		return -1
	return maxi