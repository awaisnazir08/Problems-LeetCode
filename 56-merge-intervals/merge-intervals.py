class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result list with the first interval
        merged_intervals = [intervals[0]]
        
        # Merge overlapping intervals or append new intervals
        for interval in intervals[1:]:
            if interval[0] > merged_intervals[-1][1]:
                # If the start time of the current interval is greater than the end time of the last merged interval,
                # it's a new non-overlapping interval
                merged_intervals.append(interval)
            else:
                # Merge the current interval with the last merged interval
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        return merged_intervals