from tkinter import *

win = Tk()

main_frame = Frame(win)
main_frame.pack()

grid_frame = Frame(main_frame)
grid_frame.grid(row=0, column=0)

select_frame = Frame(main_frame)
select_frame.grid(row=1, column=0, sticky="ew")
select_frame.grid_columnconfigure(0, weight=1)
select_frame.grid_columnconfigure(1, weight=1)

row_labels = []
col_labels = []
plots = []


def get_coords():
    srow, scol, erow, ecol = 0, 0, 0, 0
    for a, b in enumerate(plots):
        for c, d in enumerate(b):
            if d.cget("bg") == "red":
                srow = a
                scol = c
            if d.cget("bg") == "blue":
                erow = a
                ecol = c
    coords = [srow, scol, erow, ecol]
    return coords


def get_steps(coords):
    rows = sorted([coords[0], coords[2]])
    cols = sorted([coords[1], coords[3]])
    row_steps = [i for i in range(rows[0], rows[1])]
    col_steps = [i for i in range(cols[0], cols[1])]
    if len(row_steps) > len(col_steps):
        while len(col_steps) < len(row_steps):
            col_steps = col_steps + col_steps
        col_steps = sorted([i for i in col_steps[:len(row_steps)]])
    elif len(col_steps) > len(row_steps):
        while len(row_steps) < len(col_steps):
            row_steps = row_steps + row_steps
        row_steps = sorted([i for i in row_steps[:len(col_steps)]])
    else:
        pass
    if coords[0] > coords[2]:
        row_steps.reverse()
    if coords[1] > coords[3]:
        col_steps.reverse()
    steps = list(zip(row_steps, col_steps))
    return steps


def pathfind(plots):
    coords = get_coords()
    steps = get_steps(coords)
    for num, step in enumerate(steps):
        plots[step[0]][step[1]].config(text=str(num + 1))


def clicked(row, col):
    if plots[row][col].cget("bg") == "white":
        plots[row][col].config(bg="red")
    elif plots[row][col].cget("bg") == "red":
        plots[row][col].config(bg="blue")
    else:
        plots[row][col].config(bg="white")


for i in range(20):
    row_labels.append(Label(grid_frame, text=i + 1))
    col_labels.append(Label(grid_frame, text=i + 1))
    row_labels[i].grid(row=i + 1, column=0)
    col_labels[i].grid(row=0, column=i + 1)
    plots.append([])
    for j in range(20):
        button = Button(grid_frame, width=2, bg="white", command=lambda row=i, col=j: clicked(row, col))
        plots[i].append(button)
        plots[i][j].grid(row=i + 1, column=j + 1)

instr_label01 = Label(select_frame, text="Click once to select the start point (Red square)", padx=20)
instr_label02 = Label(select_frame, text="Click twice to select the end point (Blue square)", padx=20)
instr_label03 = Label(select_frame, text="If you have multiple red or blue squares, it will pathfind between the lowest.", padx=20)
instr_label01.grid(row=0, column=0, sticky="w")
instr_label02.grid(row=1, column=0, sticky="w")
instr_label03.grid(row=2, column=0, sticky="w")

start_button = Button(select_frame, text="Begin", command=lambda:pathfind(plots))
start_button.grid(row=3, column=0)


if __name__ == '__main__':
    win.title("Pathfinder")
    win.geometry("600x650")
    win.mainloop()
