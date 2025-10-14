import heapq
adj = []
n = 0
def init(N, K, sBuilding, eBuilding, mDistance):
	global adj, n
	adj = [[] for _ in range(N)]
	for i in range(K):
		u , v, d = sBuilding[i], eBuilding[i], mDistance[i]
		adj[u].append((d,v))
		adj[v].append((d,u))
	n = N
	return


def add(sBuilding, eBuilding, mDistance):
	global adj
	u , v, d = sBuilding, eBuilding, mDistance
	adj[u].append((d,v))
	adj[v].append((d,u))
	return


def calculate(M, mCoffee, P, mBakery, R):
	b_dist = [float('inf')] * n
	c_dist = [float('inf')] * n
	pq = []
	for i in range(M):
		coffee = mCoffee[i]
		c_dist[coffee] = 0
		heapq.heappush(pq,(0,0,coffee))
	for i in range(P):
		bakery = mBakery[i]
		b_dist[bakery] = 0
		heapq.heappush(pq,(0,1,bakery))
	while pq:
		dist, type, node = heapq.heappop(pq)
		
		if dist > R:
			continue
		if type == 0: # coffee
			if dist > c_dist[node]:
				continue
			for d, u in adj[node]:
				if c_dist[u] > dist + d:
					c_dist[u] = dist + d
					heapq.heappush(pq, (c_dist[u], 0, u))
		else:
			if dist > b_dist[node]:
				continue
			for d, u in adj[node]:
				if b_dist[u] > dist + d:
					b_dist[u] = dist + d
					heapq.heappush(pq, (b_dist[u], 1, u))

	ans = 2*R +1
	for i in range(n):
		if 0 < b_dist[i] <=R and 0 < c_dist[i] <= R:
			ans = min(ans, b_dist[i] + c_dist[i] )
	if ans > 2*R:
		return -1
	else:
		return ans