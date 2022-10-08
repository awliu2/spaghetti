from typing import List

def cyclicPath(path: List[str]):
    
    visited = []

    visited = []
    
    row = 0
    col = 0

    directions = {
        'north': [0, 1],
        'south': [0, -1],
        'east': [1, 0],
        'west': [-1, 0] 
    }
    visited.append([row, col])
    for dir in path:
        #visited.append([row, col])
        row += directions[dir][0] 
        col += directions[dir][1]
        visited.append([row, col])
    
    print(visited)


    
    max_overlap = 0
    optimal_l = 0
    optimal_r = 0

    for r in range(len(visited)):
        l = 0
        for l in range(0, r):
            if visited[l] == visited[r]:
                print(l, r)
                if r - l + 1 > max_overlap:
                    optimal_l = l
                    optimal_r = r
                    max_overlap = r - l + 1
            
    print(optimal_l)
    print(optimal_r)
    print(max_overlap)

    return path[0:optimal_l] + path[optimal_r:]




path = ['north', 'east', 'south','west']
print(cyclicPath(path))


