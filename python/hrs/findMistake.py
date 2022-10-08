from typing import List

def findMistakes(submissions: List[List[str]]) -> List[str]:
    rv = []
    mistakeMap = {}
    num_rows = len(submissions)
    num_cols = len(submissions[0])
    for col in range(num_rows):
        max_heap = []
        for row in range(len(submissions)):
            if submissions[row][col] in max_heap:
                
            

            # curr_row = submissions[row]
            
            # mistakeMap[col][curr_row[col]] = mistakeMap[col][curr_row[col]].gets
            # if curr_row[col] not in mistakeMap[col]:
            #     mistakeMap[col][curr_row[col]] = 1
            # else:
            #     mistakeMap[col][curr_row[col]] += 1




    

