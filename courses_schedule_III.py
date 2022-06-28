from operator import itemgetter

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        curr_duration = 0
        durations = []
        heapq.heapify(durations)
        courses.sort(key=itemgetter(1))
        for i in courses:
            curr_duration += i[0]
            heapq.heappush(durations, -i[0])
            if curr_duration > i[1]:
                curr_duration += heapq.heappop(durations)
                
        return len(durations)
        
      