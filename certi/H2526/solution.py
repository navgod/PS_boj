from collections import defaultdict, deque
from bisect import insort_left
 
class RESULT_E:
    def __init__(self, success, locname):
        self.success = success
        self.locname = locname
 
class RESULT_S:
    def __init__(self, cnt, carlist):
        self.cnt = cnt
        self.carlist = carlist # [str] * 5
 
def init(N : int, M : int, L : int) -> None:
    global car_info, car_sort, slot_lst, sect_size, limit, used
    global INF, del_used
    INF = float("inf")
    limit = L
    car_info = defaultdict(lambda: (INF, None, None))       # 차번호 : (time_in, sect, slot)
    car_sort = defaultdict(list)    # 차 뒷번호 : (차 전체번호, time_in)
    used = deque()      # 자리 중에 쓰고있는 것들.. deque((car_info))
    del_used = defaultdict(int)      # 얘는 (time_in, slot, sect) : int -> 이게 왜 int지?
    sect_size = dict()      # sect 별 남은 빈 슬롯 수
    slot_lst = defaultdict(list)    # 남아있는 슬롯 리스트
 
    abc = [chr(i) for i in range(65, 65+26)]
    for i in range(N):
        sect_size[abc[i]] = M
        for j in range(M):
            slot_lst[abc[i]].append(str(j).zfill(3))
     
     
def enter(mTime : int, mCarNo : str) -> RESULT_E:
    ## 빈 슬롯이 가장 많은 구역 중 영역의 대문자가 가장 앞선 구역
    ## 선택된 구역에서 숫자번호가 가장 앞선 빈 슬롯
    ## 빈슬롯 없으면 주차 실패
     
    cur_time, iid = mTime, mCarNo
 
    ## 기존에 입차되어있던 차들 확인
    while used and (cur_time - used[0][0] >= limit or del_used[used[0]] > 0):
        if del_used[used[0]] > 0:   # 이미 출차된 경우
            del_used[used.popleft()] -= 1
        elif cur_time - used[0][0] >= limit:    # 견인해야하는 상태
            _, sect, slot = used.popleft()      # 견인함
            sect_size[sect] += 1
            slot_lst[sect].append(slot)
     
    # 이번에 들어온 친구가 이미 있었는지, 이미 출차 혹은 견인되었는지 체크
    # 이미 출차 혹은 견인되었으면 다시 재입차 가능
    if cur_time - car_info[iid][0] >= limit:
        del car_info[iid]
     
    ## 입차 우선순위 고려
    # 빈 슬롯이 많을수록, 섹션 알파벳이 작을수록.
    minn = (9999, "Z")
    for sect, empty in sect_size.items():
        minn = min(minn, (-empty, sect))
     
    if minn[0] == 0:    # 빈자리가 없었다는 것임.
        return RESULT_E(0, "")
     
    else:
        _, sect = minn
        sect_size[sect] -= 1
 
        ## 섹션은 안 상태고, remain_slot에서 제일 작은게 결국 들어갈 slot임.
        slot = min(slot_lst[sect])
        slot_lst[sect].remove(slot)
 
        ## search 할 때 필요한 sorted list
        used.append((cur_time, sect, slot))     # 입차했다는 것을 used에 확인
        car_info[iid] = (cur_time, sect, slot)
        insort_left(car_sort[iid[-4:]], (iid, cur_time))
 
        return RESULT_E(1, sect + slot)
 
def pullout(mTime : int, mCarNo : str) -> int:
    cur_time, iid = mTime, mCarNo
     
    ## 차량이 출차하면 빈슬롯이 되고, 다시 차량 보관 가능
    if cur_time - car_info[iid][0] >= limit:    # 견인되어있는 상태이면
        time_in = car_info[iid][0]
        time_ban = time_in + limit
        del car_info[iid]       # 현재 차량정보에서 지우고, 왜 그럼 여기서 used에서는 안지우는거지?
        return -1 * (limit + (cur_time - time_ban) * 5)
     
    elif car_info[iid][0] == INF:       # 아예 없는 상태이면
        return -1
     
    else:       # 정상 출차
        time_in, sect, slot = car_info[iid]
        sect_size[sect] += 1
        slot_lst[sect].append(slot)
        del_used[(time_in, sect, slot)] += 1        # 출차 체크 (del_used의 value값은 0아님 1이네.)
        del car_info[iid]
        return cur_time - time_in
         
def search(mTime : int, mStr : str) -> RESULT_S:
    cur_time = mTime
    key = mStr
    temp_park = []      # 주차되어있는 차량
    temp_ban = []       # 견인된 차량
 
    for iid, time_in in car_sort[key]:
        if time_in == car_info[iid][0]:    # 유효 데이터??
            # car_sort에는 모든 차량정보가 다 들어감.
            # car_info에는 현재 차량정보가 들어가있음.
            # 그래서 car_sort를 순회하면서, car_info[iid][0]을 비교해서 이미 출차된 차량인지 확인해야함.
            if cur_time - time_in < limit:
                temp_park.append(iid)
            else:
                temp_ban.append(iid)
        if len(temp_park) == 5:
            break
     
    if len(temp_park) < 5:
        for temp in temp_ban:
            temp_park.append(temp)
            if len(temp_park) == 5:
                break
 
    return RESULT_S(len(temp_park), temp_park)