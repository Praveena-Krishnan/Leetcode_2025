class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0

        while start < n:
            curr_gas = 0
            count = 0
            i = start

            while count < n:
                curr_gas += gas[i] - cost[i]
                if curr_gas < 0:
                    break
                i = (i + 1) % n
                count += 1

            if count == n:  # completed full circle
                return start
            else:
                # skip all stations from 'start' to 'i'
                # because they cannot be valid start points
                start = start + count + 1

        return -1
