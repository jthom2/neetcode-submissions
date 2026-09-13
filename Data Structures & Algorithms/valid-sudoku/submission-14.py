class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        l = len(board)

        for i, r in enumerate(board):
            if r.count(str(i+1)) > 1: return False

        mp = {}
        ap = {}

        for i in range(l):
            ap[i] = set()

            tmp = []

            for j in range(l):

                curr = board[j][i]
                if board[i].count(str(j+1)) > 1: return False
                if curr == '.': continue
                

                elif tmp.count(curr) == 0: tmp.append(curr)
                else: return False

                mp.update({(i, j): curr})
        


        for i in range(l):

            

            for j in range(l):
                curr = board[i][j]
                if curr == '.': continue
                if (i < 3):
                    if (j < 3): 
                        if curr not in ap[0]: 
                            ap[0].add(curr)
                        else:
                            print('0') 
                            return False
                    elif (2 < j < 6):
                        if curr not in ap[1]: 
                            ap[1].add(curr)
                        else:
                            print('1') 
                            return False
                    else:
                        if curr not in ap[2]: 
                            ap[2].add(curr)
                        else:
                            print('2') 
                            return False
                if (2 < i < 6):
                    if (j < 3): 
                        if curr not in ap[3]: 
                            ap[3].add(curr)
                        else:
                            print('3') 
                            return False
                    elif (2 < j < 6):
                        if curr not in ap[4]: 
                            ap[4].add(curr)
                        else:
                            print('4') 
                            return False
                    else:
                        if curr not in ap[5]: 
                            ap[5].add(curr)
                        else:
                            print('5') 
                            return False
                elif (6 < i < 9):
                    if (j < 3): 
                        if curr not in ap[6]: 
                            ap[6].add(curr)
                        else:
                            print(ap, '\n')
                            print('6') 
                            return False
                    elif (2 < j < 6):
                        if curr not in ap[7]: 
                            ap[7].add(curr)
                        else:
                            print('7') 
                            return False
                    else:
                        if curr not in ap[8]: 
                            ap[8].add(curr)
                        else:
                            print('8') 
                            return False


        return True




