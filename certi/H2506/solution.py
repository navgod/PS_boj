# %%
import heapq

class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

def init() -> None:
    global product, information
    product = [[[] for _ in range(6)] for _ in range(6)]
    discount = [[0 for _ in range(6)] for _ in range(6)]
    information = {}
    pass

def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    mAmount = discount[mCategory][mCompany]
    product[mCategory][mCompany].append(mPrice+mAmount)
    information[mID] = (mCategory,mCompany)
    return len([1 for p in product[mCategory][mCompany] if p> mAmount])

def closeSale(mID : int) -> int:
    if mID in information:
        mCategory, mCompany = information[mID]
        mAmount = discount[mCategory][mCompany]
        price = product[mCategory][mCompany]
        if price > mAmount:
            return price- mAmount
    return -1

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    discount[mCategory][mCompany] += mAmount
    return len([1 for p in product[mCategory][mCompany] if p> mAmount])

def show(mHow : int, mCode : int) -> RESULT:
    min_price = []
    if mHow == 0:
        for i in range(1,6):
            for j in range(1,6):
                for p in product[i][j]:
                    heapq.heappush(min_price, -p)
                if len(min_price)>5:
                    heapq.heappop(min_price)
    elif mHow == 1:
        for j in range(1,6):
            for p in product[mCode][j]:
                heapq.heappush(min_price, -p)
            if len(min_price)>5:
                heapq.heappop(min_price)
    else:
        for i in range(1,6):
            for p in product[i][mCode]:
                heapq.heappush(min_price, -p)
            if len(min_price)>5:
                heapq.heappop(min_price)
    return RESULT(len(min_price), min_price)

# %%
