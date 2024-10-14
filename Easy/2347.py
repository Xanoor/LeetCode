#Two solutions

class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        rank_counts = [0] * 14
        for rank in ranks:
            rank_counts[rank] += 1
        max_count = max(rank_counts)

        if len(set(suits)) == 1: return "Flush"
        elif max_count >= 3: return "Three of a Kind"
        elif max_count == 2: return "Pair"
        return"High Card"
    
#print(Solution.bestHand(Solution, [2,10,7,10,7], ["a","b","a","d","b"]))
#39ms 16.6Mb

class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        rank_counts = [0] * 14
        flush = True 
        
        for i in range(len(ranks)):
            rank_counts[ranks[i]] += 1
            if suits[i] != suits[0]: 
                flush = False 
        max_count = max(rank_counts)

        if flush:
            return "Flush"
        elif max_count >= 3:
            return "Three of a Kind"
        elif max_count == 2:
            return "Pair"
        return "High Card"

#print(Solution.bestHand(Solution, [2,10,7,10,7], ["a","b","a","d","b"]))
#36ms 16.5Mb

