class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        backup = {}
        def DFS(s):
            if not s:
                return ['']
            if s not in backup:
                backup[s]= []
                for i in range(1,len(s)+1):
                    word = s[:i]
                    if word in wordDict:
                        sentences = DFS(s[i:])
                        for ss in sentences:
                            backup[s].append(word + ' '+ ss) 
            return backup[s]
        DFS(s)    
        return [bu[:-1] for bu in backup[s]]