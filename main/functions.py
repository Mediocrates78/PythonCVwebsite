import string
import random as rnd

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

