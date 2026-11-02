class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = {}
        offsets = [(0,-1),(0,1),(1,0),(-1,0)]
        result = set()
        visited = {}

        for word in words:
            current = trie
            for w in word:
                current[w] = current.get(w, {})
                current = current[w]
            current['*'] = {}
        
        def dfs(i, j, current, visited, word):

            # search in trie
            if i < 0 or j < 0 or \
                i >= len(board) or \
                j >= len(board[i]) or \
                (i,j) in visited or \
                board[i][j] not in current:
                return

            visited[(i,j)] = 1
            current = current[board[i][j]]
            word += board[i][j]
            
            if "*" in current:
                result.add(word)

            dfs(i, j+1, current, visited, word)
            dfs(i+1, j, current, visited, word)
            dfs(i, j-1, current, visited, word)
            dfs(i-1, j, current, visited, word)

            del visited[(i,j)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, trie, visited, "")
        
        return list(result)
            


        
        
        





                












        # for word in words:
        #     c = 0   
        #     for i in range(len(board)):
        #         for j in range(len(board[i])):
        #             if word[c] == board[i][j]:
        #                 _search((i,j), c+1, {(i,j)})
        

        # def _search(start, idx, visited):
        #     i, j = start

        #     offsets = [(0,-1),(0,1),(1,0),(-1,0)]

        #     for (offset_i, offset_j) in offsets:
        #         if (0 <= i + offset_i <= len(board)) \
        #             and (0 <= j + offset_j <= len(board)):

        #             if board[i+offset_i][j+offset_j] == word
