visited[], stack[] 초기화
DFS(v)
    시작점 v 방문;
    visited[v] <- true:
    while {
            if(v의 인접 정점 중 방문 안 한 정점 w가 있으면)
                push(v);
                v <- w; (w에 방문)
                visited[w] <- true;
            else
                if (스택이 비어 있지 않으면)
                    v <- pop(stack);
                else
                    break
    }
end DFS()