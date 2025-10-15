import heapq

class RESULT_E:
    def __init__(self, success, locname):
        self.success = success
        self.locname = locname

class RESULT_S:
    def __init__(self, cnt, carlist):
        self.cnt = cnt
        self.carlist = carlist # [str] * 5

class Area:
    def __init__(self, name: str, num_slots: int):
        self.name = name
        self.slots = [] # (mTime, CarNo)
        self.pullouted = []

    def __lt__(self, other):
        return self.left > other.left if self.left != other.left else self.name < other.name

parking_lot = []
parking_lot_left = []
information = {}
duration = 0
def init(N : int, M : int, L : int) -> None:
    global duration
    for i in range(N):
        heapq.heappush(parking_lot, Area(chr(ord('A')+i), M))
    duration = L

def enter(mTime : int, mCarNo : str) -> RESULT_E:
    while True:
        slots = parking_lot[0].slots

        mtime , carno = slots[0]

        if mtime < mTime:
            pa


    return RESULT_E(-1, "")

def pullout(mTime : int, mCarNo : str) -> int:
    return -1

def search(mTime : int, mStr : str) -> RESULT_S:
    return RESULT_S(-1, ["", "", "", "", ""])
