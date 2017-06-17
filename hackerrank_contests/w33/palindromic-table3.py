from collections import defaultdict

def check_palindrome(digits):
    digit_count = defaultdict(int)
    for digit in digits:
        digit_count[digit] += 1
        odd_count = 0
        for digit in digit_count:
            if digit_count[digit] & 1: #digit_count[digit] is odd
            odd_count += 1
            if odd_count <= 1:
                return True
            else:
                return False
                
n, m = map(int, input().strip().split(' '))
mat = [[x for x in input().strip().split(' ')] for y in range(n)]

ans_max = 0

ans = 0
coordi = []
for x1 in range(n-1):
    for y1 in range(m-1):
        temp_ans = get_all_about_this_sub_matrix(x1, y1)
        if ans < temp_ans[0]:
            ans = temp_ans
            coordi =[x1,y1, temp_ans[1][0], temp_ans[1][1]]

def get_pal_count_and_odd_list(x,y, temp_mat):
    if x!=0 and y!=0:
        pal_count1, odd_list1 = temp_mat[x-1][y]
        pal_count2, odd_list2 = temp_mat[x][y-1][1]
    elif x==0 and y!=0:
        pal_count1, odd_list1 = 0, []
        pal_count2, odd_list2 = temp_mat[x][y-1]
    elif x!=0 and y==0:
        pal_count1, odd_list1 = temp_mat[x-1][y]
        pal_count2, odd_list2 = 0, []
    else:
        pal_count1, odd_list1 = 0, []
        pal_count2, odd_list2 = 0, []
    return [[pal_count1, odd_list1], [pal_count2, odd_list2]]

def get_all_about_this_sub_matrix(x1, y1):
    temp_mat = [[0, [] for x in range(n)] for y in range(m)]

    for x in range(x1, n):
        for y in range(y1, m):
            digit = mat[x1][y1]
            pal_n_lists = get_pal_count_and_odd_list(x,y,temp_mat=)
            pal_count1, odd_list1 = pal_n_lists[0]
            pal_count2, odd_list2 = pal_n_lists[1]
            odds = odd_list1 + odd_list2
            if

for x2 in range(n-1, -1, -1):
    for y2 in range(m-1, -1, -1):
        print(x2, y2)
        digits = get_the_digits(0,0,x2, y2)
        if check_palindrome(digits):
            l = len(digits)
            if ans_max < l:
                ans_max = l
                cordi = [0,0, x2, y2]
print(ans_max)
print(" ".join(map(str, cordi)))
