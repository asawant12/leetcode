# https://leetcode.com/problems/k-closest-points-to-origin/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
from queue import PriorityQueue
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_to_distance_mapping = {}
        k_closest = []
        q = PriorityQueue()
        for point in points:
            x2 = point[0]
            y2 = point[1]
            distance = math.sqrt((x2*x2) + (y2*y2))
            if distance not in points_to_distance_mapping:
                points_to_distance_mapping[distance] = [(x2,y2)]
            else:
                points_to_distance_mapping[distance].append((x2,y2))
            q.put(distance)
        while k > 0:
            dist = q.get()
            points = points_to_distance_mapping[dist]
            k_closest.extend(points)
            k -= len(points)
        return k_closest


        
