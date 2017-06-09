#!/usr/bin/python

# Head ends here

def get_dirt_position(board):
    global bot_r, bot_c
    dirt_c_list = []
    for row in range(5):
        if 'd' in board[row]:
            for col in range(5):
                if board[row][col] == 'd':
                    dirt_c_list.append(col)
            break

    if len(dirt_c_list):
        abs_diff_list = [abs(x-bot_c) for x in dirt_c_list]
        return [row, dirt_c_list[abs_diff_list.index(min(abs_diff_list))] ]
    else:
        return [None, None]

def clean_the_dirt(dirt_r,dirt_c):
    global bot_r, bot_c
    # print("got ", bot_r,bot_c,dirt_r,dirt_c)
    if bot_r == dirt_r and bot_c == dirt_c:
        print("CLEAN")
        board[dirt_r][dirt_c] = '-'
        return None
    else:
        if bot_r == dirt_r:
            if bot_c < dirt_c:
                print("RIGHT")
                bot_c += 1
            else:
                print("LEFT")
                bot_c -= 1

            return None

        elif bot_r != dirt_r:
            if bot_r < dirt_r:
                print("DOWN")
                bot_r += 1
            else:
                print("UP")
                bot_r -= 1

def next_move(bot_r, bot_c, board):
    dirt_r, dirt_c = get_dirt_position(board)
    if dirt_c is None:
        return None
    clean_the_dirt(dirt_r,dirt_c)

# Tail starts here
if __name__ == "__main__":
    bot_ = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    global bot_r, bot_c
    bot_r,bot_c = bot_[0], bot_[1]
    next_move(bot_r,bot_c, board)
