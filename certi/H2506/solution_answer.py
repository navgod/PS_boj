from heapq import heappop, heappush
 
 
class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5
 
 
class Item:
    def __init__(self, idx, ca, co, pr):
        self.idx = idx
        self.ca = ca
        self.co = co
        self.pr = pr
        self.alive = True
         
    def add(self, am):
        self.pr -= am
        return self.pr > 0
     
    def __lt__(self, o):
        return self.pr < o.pr if self.pr != o.pr else self.idx < o.idx
         
buc = [[list() for _ in range(6)] for __ in range(6)]
 
 
cdb = dict()
 
 
base = [[0 for _ in range(6)] for __ in range(6)]
buc_len = [[0 for _ in range(6)] for __ in range(6)]
 
 
def init() -> None:
    for i in range(1, 6):
        for j in range(1, 6):
            buc[i][j].clear()
            base[i][j] = buc_len[i][j] = 0
             
    cdb.clear()
 
 
def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    p = Item(mID, mCategory, mCompany, mPrice - base[mCategory][mCompany])
    heappush(buc[mCategory][mCompany], p)
     
    cdb[mID] = p
    buc_len[mCategory][mCompany] += 1
 
 
    return buc_len[mCategory][mCompany]
 
 
def closeSale(mID : int) -> int:
    try:
        p = cdb[mID]
    except KeyError:
        return -1
 
 
    if not p.alive:
        return -1
     
    p.alive = False
    buc_len[p.ca][p.co] -= 1
     
    return p.pr + base[p.ca][p.co]
 
 
def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    base[mCategory][mCompany] -= mAmount
    
    while len(buc[mCategory][mCompany]) > 0:
        p = buc[mCategory][mCompany][0]
        if not p.alive:
            heappop(buc[mCategory][mCompany])
            continue
        
        if p.pr + base[mCategory][mCompany] <= 0:
            heappop(buc[mCategory][mCompany])
            p.alive = False
            buc_len[mCategory][mCompany] -= 1
            continue
 
 
        break
                
    return buc_len[mCategory][mCompany]
     
def show(mHow : int, mCode : int) -> RESULT:
    con = list()
    if mHow == 0:
        for i in range(1, 6):
            for j in range(1, 6):
                bck = []
                c = 0
                while c <= 5 and len(buc[i][j]) > 0:
                    p = heappop(buc[i][j])
                    if not p.alive:
                        continue
                    c += 1
                    con.append((p.pr + base[i][j], p.idx))
                    bck.append(p)
                for p in bck:
                    heappush(buc[i][j], p)
                 
    elif mHow == 1:
        for i in range(1, 6):
            bck = []
            c = 0
            while c <= 5 and len(buc[mCode][i]) > 0:
                p = heappop(buc[mCode][i])
                if not p.alive:
                    continue
                c += 1
                con.append((p.pr + base[mCode][i], p.idx))
                bck.append(p)
            for p in bck:
                heappush(buc[mCode][i], p)
    else:
        for i in range(1, 6):
            bck = []
            c = 0
            while c <= 5 and len(buc[i][mCode]) > 0:
                p = heappop(buc[i][mCode])
                if not p.alive:
                    continue
                c += 1
                con.append((p.pr + base[i][mCode], p.idx))
                bck.append(p)
            for p in bck:
                heappush(buc[i][mCode], p)
 
 
    con.sort()
 
 
    IDs = [0 for _ in range(5)]
    cnt = min(5, len(con))
     
    for i in range(cnt):
        IDs[i] = heappop(con)[1]
 
 
    return RESULT(cnt, IDs)