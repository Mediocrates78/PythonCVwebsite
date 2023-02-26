import string
import random as rnd
import json

def find_lowest(num_list):
    try:
        my_list = [int(i) for i in num_list]
        return_list = []
        i = 0
        return_list.append("Original list: " + str(my_list))
        while len(my_list) > 1:
            i += 1
            if my_list[0] < my_list[1]:
                my_list.append(my_list[0])
                del(my_list[0])
            else:
                del(my_list[0])
            return_list.append(f"step {i}: {my_list}")
        return_list.append(f"Final result: {my_list[0]}")
        return return_list
    except:
        return(["ERROR: Please only enter numbers."])
    
def make_dicts():

    def bin_switch(num):
        if num == "0":
            num = "1"
        else:
            num = "0"
        return num

    bin_dict = {}
    char_list = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/"] \
    + [str(i) for i in range(10)] + [":", ";", "<", "=", ">", "?", "@"] + [i for i in string.ascii_uppercase] \
    + ["[", "\\", "]", "^", "_", "`"] + [i for i in string.ascii_lowercase] + ["{", "|", "}", "~"]
    bin = ["0", "0", "1", "0", "0", "0", "0", "0"]
    multi = {'2': -2, '4': -3, '8': -4, '16': -5, '32': -6 }
    for i, j in enumerate(char_list):
        bin[-1] = bin_switch(bin[-1])
        for key, value in multi.items():
            if (i + 1) % int(key) == 0 and i != 0:
                bin[value] = bin_switch(bin[value])
        if i + 1 == 32:
            bin[-7] = "1"
        bin_dict[j] = "".join(bin)
        bin_dict[" "] = "00000000"

    morse_dict = {
        "a": "01", "b": "1000", "c": "1010", "d": "100", "e": "0", "f": "0010", "g": "110", "h": "0000", 
        "i": "00", "j": "1000", "k": "101", "l": "0100", "m": "11", "n": "10", "o": "111", "p": "0110", 
        "q": "1101", "r": "010", "s": "000", "t": "1", "u": "001", "v": "0001", "w": "011", "x": "1011", 
        "y": "1011", "z": "1100"
    }
    dicts = [bin_dict, morse_dict]
    return dicts

def encoding(unenc):

    bin_dict, morse_dict = make_dicts()[0], make_dicts()[1]
    temp = ""
    encoded = ""
    for letter in unenc:
        try:
            temp += bin_dict[letter]
        except KeyError:
            encoded = f"ERROR: unknown character: {letter}"
            return encoded
    while len(temp) >= 1:
        randno1 = rnd.randint(1, 4)
        for key, value in morse_dict.items():
            if temp[0:randno1] == value:
                randno2 = rnd.randint(1, 3)
                if randno2 == 1:
                    encoded += key.upper()
                else:
                    encoded += key
                temp = temp[randno1:]
            else:
                pass
    return encoded

def decoding(enc):
    bin_dict, morse_dict = make_dicts()[0], make_dicts()[1]
    temp = ""
    decoded = ""
    enc = enc.lower()
    for letter in enc:
        temp += morse_dict[letter]
    for i in range(len(temp[::8])):
        for key, value in bin_dict.items():
            if temp[0:8] == value:
                decoded += key
        temp = temp[8:]
    return decoded

def make_sudoku():
    def find_avails(grid):
        avails = []
        temp = []
        for i in range(9):
            temp.append([i, "*", [j for j in range(9) if grid[i][j] == 0]])
        for k in range(3):
            temp2 = []
            for m in range(3):
                temp2.append(temp[k + (m * 3)])
            rnd.shuffle(temp2)
            avails.append(temp2)
        return avails

    def round_one(control, avails):
        for i in range(3):
            for j in range(3):
                avails[i][j][1] = control[i][j]
        return avails

    def control_check(control, avails):
        temp = [[], [], []]
        one = avails[0][0][2] + avails[0][1][2] + avails[0][2][2]
        two = avails[1][0][2] + avails[1][1][2] + avails[1][2][2]
        three = avails[2][0][2] + avails[2][1][2] + avails[2][2][2]
        for i in control:
            if i[0] in one:
                temp[0].append(i)
            if i[0] in two:
                temp[1].append(i)
            if i[0] in three:
                temp[2].append(i)
        for i in range(3):
            if temp[i][0] in temp[i - 1] and len(temp[i - 1]) > 1:
                temp[i - 1].remove(temp[i][0])
            if temp[i][0] in temp[i - 2] and len(temp[i - 2]) > 1:
                temp[i - 2].remove(temp[i][0])

        return [temp[0][0], temp[1][0], temp[2][0]]

    def get_plots(control, avails, num):
        control = control_check(control, avails)
        for i in range(3):
            for j in range(3):
                while avails[i][j][1] == "*":
                    if control[0][0] in avails[i][j][2]:
                        avails[i][j][1] = control[0][0]
                        del control[0][0]
                        if len(control[0]) == 0:
                            del control[0]
                    elif control[0][0] not in avails[i][j][2] and len(control[0]) != 1:
                        control[0].append(control[0].pop(0))
                    else:
                        if control[0][0] in avails[i][j - 1][2]:
                            control[0].append(avails[i][j - 1][1])
                            avails[i][j - 1][1] = control[0][0]
                            del control[0][0]
                        elif control[0][0] in avails[i][j - 2][2]:
                            control[0].append(avails[i][j - 2][1])
                            avails[i][j - 2][1] = control[0][0]
                            del control[0][0]
        return avails

    def unsolved(grid):
        new_grid = [[0 for i in range(9)] for j in range(9)]
        plots = []
        while len(plots) < 25:
            for i in range(25):
                x = rnd.randint(0, 8)
                y = rnd.randint(0, 8)
                if [x, y] in plots:
                    pass
                else:
                    plots.append([x, y])
        for i in plots:
            new_grid[i[0]][i[1]] = grid[i[0]][i[1]] 

        return new_grid

    grid = [[0 for i in range(9)] for j in range(9)]
    for num in range(1, 10):
        control = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        rnd.shuffle(control)
        avails = find_avails(grid)

        if num == 1:
            avails = round_one(control, avails)
        else:
            avails = get_plots(control, avails, num)

        for i in avails:
            for j in i:
                grid[j[0]][j[1]] = num
    unsolv = unsolved(grid)

    return unsolv

def solve(grid):
    def find_empty(grid):
        for x in range(9):
            for y in range(9):
                if grid[x][y] != 0:
                    pass
                else:
                    return [x, y]

    def valid(grid, plot, num):
        row = grid[plot[0]]
        col = [i[plot[1]] for i in grid]
        three = []
        for x in range((plot[0] // 3) * 3, ((plot[0] // 3) * 3) + 3):
            for y in range((plot[1] // 3) * 3, ((plot[1] // 3) * 3) + 3):
                three.append(grid[x][y])
        if num not in row and num not in col and num not in three:
            return True

    plot = find_empty(grid)
    if not plot:
        return True
    else:
        row, col = plot[0], plot[1]
        for num in range(1, 10):
            if valid(grid, [row, col], num):
                grid[row][col] = num
                if solve(grid):
                    return grid
            grid[row][col] = 0
        return False

        

