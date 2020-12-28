class Solution:
    def assignBikes(self, workers, bikes):
        #(distance,i,j)
        from heapq import heappop,heappush,heapify
        pq = []
        res = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                heappush(pq,(distance,i,j))
        k = 0
        while k < len(workers):
            cur = heappop(pq)
            res.append(cur[2])
            for item in pq:
                if item[1] == cur[1]:
                    pq.remove(item)
                if item[2] == cur[2]:
                    pq.remove(item)
            heapify(pq)
            k += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.assignBikes([[0,0],[2,1]],[[1,2],[3,3]]))