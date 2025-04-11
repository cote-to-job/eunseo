#시작 left * right #
#1,4,7,* 왼손
#3,6,9,# 오른손
#2,5,8,0은  현재 키패드에 더 가까운 엄지 사용

def solution(numbers, hand): 
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    col_mid = [2, 5, 8, 0]  # 가운데 
    left_pos = keypad['*']
    right_pos = keypad['#']
    result = ''

    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    for num in numbers:
        if num in [1, 4, 7]:
            result += 'L'
            left_pos = keypad[num]
        elif num in [3, 6, 9]:
            result += 'R'
            right_pos = keypad[num]
        elif num in col_mid:
            dist_l = distance(left_pos, keypad[num])
            dist_r = distance(right_pos, keypad[num])
            if dist_l < dist_r:
                result += 'L'
                left_pos = keypad[num]
            elif dist_r < dist_l:
                result += 'R'
                right_pos = keypad[num]
            else:
                if hand == 'right':
                    result += 'R'
                    right_pos = keypad[num]
                else:
                    result += 'L'
                    left_pos = keypad[num]

    return result
