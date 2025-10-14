# %%
from collections import deque
from typing import List

WIDTH = 8

class Point:
    def __init__(self, score=0, y1=0, x1=0, y2=0, x2=0):
        self.score = score
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2
    
    def __lt__(self, other):
        """비교 연산자 (최대값을 찾기 위한 역순)"""
        if self.score != other.score:
            return self.score < other.score
        if self.y1 != other.y1:
            return self.y1 > other.y1
        if self.x1 != other.x1:
            return self.x1 > other.x1
        if self.y2 != other.y2:
            return self.y2 > other.y2
        return self.x2 > other.x2

class JewelGame:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.q = [deque() for _ in range(8)]  # 각 열마다 큐
        self.score_table = [0, 0, 0, 1, 4, 9, 9, 9, 9]  # 연속 개수별 점수
    
    def init(self, N: int, mJewels: List[List[int]]):
        """초기화: 8x8 보드와 예비 보석 큐 설정"""
        # 큐 초기화
        for i in range(8):
            self.q[i].clear()
        
        # 보드 설정 (처음 8행)
        for y in range(8):
            for x in range(8):
                self.board[y][x] = mJewels[y][x]
        
        # 예비 보석들을 각 열의 큐에 저장 (8행 이후)
        for y in range(8, N):
            for x in range(8):
                self.q[x].append(mJewels[y][x])
    
    def fill_board(self):
        """빈 칸을 채우고 보석을 아래로 떨어뜨림"""
        for x in range(8):
            # 0이 아닌 보석들을 아래로 모으기
            temp = []
            for y in range(8):
                if self.board[y][x] > 0:
                    temp.append(self.board[y][x])
            
            # 보드에 다시 채우기
            for y in range(len(temp)):
                self.board[y][x] = temp[y]
            
            # 빈 칸을 큐에서 채우기
            for y in range(len(temp), 8):
                if self.q[x]:
                    self.board[y][x] = self.q[x].popleft()
    
    def check_score_swap(self, y1: int, x1: int, y2: int, x2: int) -> int:
        """스왑 후 예상 점수 계산 (실제로 제거하지 않음)"""
        ret = 0
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        points = [(y1, x1), (y2, x2)]
        
        for py, px in points:
            # 가로 방향 체크
            left_x = px
            right_x = px
            while left_x >= 0 and self.board[py][left_x] == self.board[py][px]:
                left_x -= 1
            while right_x < 8 and self.board[py][right_x] == self.board[py][px]:
                right_x += 1
            ret += self.score_table[right_x - left_x - 1]
            
            # 세로 방향 체크
            top_y = py
            bottom_y = py
            while top_y >= 0 and self.board[top_y][px] == self.board[py][px]:
                top_y -= 1
            while bottom_y < 8 and self.board[bottom_y][px] == self.board[py][px]:
                bottom_y += 1
            ret += self.score_table[bottom_y - top_y - 1]
        
        return ret
    
    def check_score(self) -> int:
        """현재 보드의 총 점수 계산 (제거하지 않음)"""
        ret = 0
        
        # 가로 체크
        for y in range(8):
            x1, x2 = 0, 0
            while x2 < 8:
                while x2 < 8 and self.board[y][x1] == self.board[y][x2]:
                    x2 += 1
                ret += self.score_table[x2 - x1]
                x1 = x2
        
        # 세로 체크
        for x in range(8):
            y1, y2 = 0, 0
            while y2 < 8:
                while y2 < 8 and self.board[y1][x] == self.board[y2][x]:
                    y2 += 1
                ret += self.score_table[y2 - y1]
                y1 = y2
        
        return ret
    
    def erase(self) -> int:
        """3개 이상 연속된 보석 제거하고 점수 반환"""
        ret = 0
        chk = [[False] * 8 for _ in range(8)]
        
        # 가로 체크
        for y in range(8):
            x1, x2 = 0, 0
            while x2 < 8:
                while x2 < 8 and self.board[y][x1] == self.board[y][x2]:
                    x2 += 1
                ret += self.score_table[x2 - x1]
                if x2 - x1 >= 3:  # 3개 이상이면 제거 표시
                    for x in range(x1, x2):
                        chk[y][x] = True
                x1 = x2
        
        # 세로 체크
        for x in range(8):
            y1, y2 = 0, 0
            while y2 < 8:
                while y2 < 8 and self.board[y1][x] == self.board[y2][x]:
                    y2 += 1
                ret += self.score_table[y2 - y1]
                if y2 - y1 >= 3:  # 3개 이상이면 제거 표시
                    for y in range(y1, y2):
                        chk[y][x] = True
                y1 = y2
        
        # 실제로 보석 제거 (0으로 설정)
        for y in range(8):
            for x in range(8):
                if chk[y][x]:
                    self.board[y][x] = 0
        
        return ret
    
    def take_turn(self) -> List[int]:
        """한 턴 실행: 최적의 스왑을 찾아 실행"""
        cand = Point(0, -1, -1, -1, -1)
        
        while True:
            self.fill_board()
            
            # 연쇄 제거 (더 이상 제거할 게 없을 때까지)
            while self.check_score():
                self.erase()
                self.fill_board()
            
            # 모든 가능한 스왑을 시도하여 최적의 것 찾기
            for y in range(8):
                for x in range(8):
                    # 오른쪽과 스왑
                    if x < 7:
                        self.board[y][x], self.board[y][x + 1] = \
                            self.board[y][x + 1], self.board[y][x]
                        
                        tmp = Point(self.check_score_swap(y, x, y, x + 1), 
                                   y, x, y, x + 1)
                        if cand < tmp:
                            cand = tmp
                        
                        self.board[y][x], self.board[y][x + 1] = \
                            self.board[y][x + 1], self.board[y][x]
                    
                    # 아래와 스왑
                    if y < 7:
                        self.board[y][x], self.board[y + 1][x] = \
                            self.board[y + 1][x], self.board[y][x]
                        
                        tmp = Point(self.check_score_swap(y, x, y + 1, x), 
                                   y, x, y + 1, x)
                        if cand < tmp:
                            cand = tmp
                        
                        self.board[y][x], self.board[y + 1][x] = \
                            self.board[y + 1][x], self.board[y][x]
            
            # 가능한 스왑이 없으면 보드를 전체 리셋
            if cand.score == 0:
                for y in range(8):
                    for x in range(8):
                        if self.q[x]:
                            self.board[y][x] = self.q[x].popleft()
            else:
                break
        
        # 최적의 스왑 실행
        self.board[cand.y1][cand.x1], self.board[cand.y2][cand.x2] = \
            self.board[cand.y2][cand.x2], self.board[cand.y1][cand.x1]
        
        # 스왑 후 연쇄 제거 및 점수 계산
        ret_score = 0
        while self.check_score():
            ret_score += self.erase()
            self.fill_board()
        
        return [ret_score, cand.y1, cand.x1, cand.y2, cand.x2]


# 사용 예시
game = JewelGame()

# 테스트 데이터
N = 10
mJewels = [
    [1, 2, 3, 4, 5, 1, 2, 3],
    [2, 3, 4, 5, 1, 2, 3, 4],
    [3, 4, 5, 1, 2, 3, 4, 5],
    [4, 5, 1, 2, 3, 4, 5, 1],
    [5, 1, 2, 3, 4, 5, 1, 2],
    [1, 2, 3, 4, 5, 1, 2, 3],
    [2, 3, 4, 5, 1, 2, 3, 4],
    [3, 4, 5, 1, 2, 3, 4, 5],
    [4, 5, 1, 2, 3, 4, 5, 1],
    [5, 1, 2, 3, 4, 5, 1, 2],
]

game.init(N, mJewels)
result = game.take_turn()
print(f"점수: {result[0]}, 스왑: ({result[1]}, {result[2]}) ↔ ({result[3]}, {result[4]})")
# %%