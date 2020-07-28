class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Time: O(len(tasks))
        # Space: O(26)
        
        freq = [0]*26
        for task in tasks:      # O(len(tasks))
            freq[ord(task) - ord('A')] += 1
        freq.sort()     # O(1)
        cycles = freq[-1] - 1
        idleSlots = cycles*n
        for i in range(24, -1, -1):     # O(1)
            idleSlots -= min(cycles, freq[i])
        return len(tasks) if idleSlots<0 else idleSlots + len(tasks)