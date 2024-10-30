import sys
input = sys.stdin.readline

point = []
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

point.append([x1, y1])
point.append([x2, y2])
point.append([x3, y3])
point.append([x4, y4])

def ccw(p1, p2, p3):
    temp = (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    else:
        return -1

def checkCross(p1, p2, p3, p4):
    is_result = False
    result = 0
    p123 = ccw(p1, p2, p3)
    p124 = ccw(p1, p2, p4)
    p341 = ccw(p3, p4, p1)
    p342 = ccw(p3, p4, p2)

    if p123 * p124 == 0 and p341 * p342 == 0:
        is_result = True
        if min(p1[0], p2[0])<=max(p3[0],p4[0]) and min(p3[0],p4[0])<=max(p1[0],p2[0]) and min(p1[1],p2[1])<=max(p3[1],p4[1]) and min(p3[1],p4[1])<=max(p1[1],p2[1]):
            result = 1

    if p123 * p124 <= 0 and p341 * p342 <= 0:
        if not is_result:
            result = 1
        
    return result   

print(checkCross(point[0], point[1], point[2], point[3]))
