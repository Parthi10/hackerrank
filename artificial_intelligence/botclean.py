#!/usr/bin/python

# Head ends here

def get_dirt_position(board):
    global bot_r, bot_c
    dist=10000
    next_goal=[0,0]
    for row in range(5):
        if 'd' in board[row]:
            for col in range(5):
                if board[row][col] == 'd':
                    d = manhattan_dist(row,col)
                    if d<dist:
                        dist=d
                        next_goal = [row,col]
    return next_goal

def manhattan_dist(row,col):
    global bot_r,bot_c
    return abs(bot_r-row)+abs(bot_c-col)

def clean_the_dirt(dirt_r,dirt_c):
    global bot_r, bot_c
    if bot_r == dirt_r and bot_c == dirt_c:
        print("CLEAN")
    elif bot_c < dirt_c:
        print("RIGHT")
    elif bot_c > dirt_c:
        print("LEFT")
    elif bot_r < dirt_r:
        print("DOWN")
    elif bot_r > dirt_r:
        print("UP")


def next_move(bot_r, bot_c, board):
    dirt_r, dirt_c = get_dirt_position(board)
    clean_the_dirt(dirt_r,dirt_c)

# Tail starts here
if __name__ == "__main__":
    bot_ = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    global bot_r, bot_c
    bot_r,bot_c = bot_[0], bot_[1]
    next_move(bot_r,bot_c, board)
