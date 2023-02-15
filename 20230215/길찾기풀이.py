# [1] 연결정보 저장 : adj 리스트
# [2] s <- 기준점 설정
# [3] while True:       # 탐색종료 stack이 빌 때 까지
# [4] for   # 연결된 & 미방문(e)
# [5] stack.push(s)         # 되돌아올 위치 push
# [6] s를 e로 갱신, visited[s] <- True
# [7] break             # 새 기준점부터 탐색
# [8] else              # 현 기준점 기준 더 이상 탐색 x
# [9] if stack == 1:
# [10]  s <- stack.pop()
# [11] else:
# [12] break        # 완전 종료