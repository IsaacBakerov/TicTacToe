cells = [" " for x in range(1, 10)]

zone = f"""
--------- 
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
---------"""
print(zone)

legal = ["1", "2", "3"]
illegal = ["0", "4", "5", "6", "7", "8", "9"]

row1 = [cells[6], cells[7], cells[8]]
row2 = [cells[3], cells[4], cells[5]]
row3 = [cells[0], cells[1], cells[2]]
column1 = [cells[6], cells[3], cells[0]]
column2 = [cells[7], cells[4], cells[1]]
column3 = [cells[8], cells[5], cells[2]]
dgnl1 = [cells[6], cells[4], cells[2]]
dgnl2 = [cells[8], cells[4], cells[0]]
x = 0
o = 0
m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for t in m:
        cords = input("Enter the coordinates: ").split()

        # not correct
        if cords[0] not in legal or cords[1] not in legal:
            if cords[0] in illegal or cords[1] in illegal:
                print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
            m += [m[len(m)-1] + 1]
        # correct
        else:
            if cords == ["1", "1"]:
                if cells[6] == " ":
                    if t % 2 == True:
                        cells[6] = "X"
                    else:
                        cells[6] = "O"
                else:
                    while cells[6] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["1", "1"]:
                            break

            elif cords == ["1", "2"]:
                if cells[7] == " ":
                    if t % 2 == True:
                        cells[7] = "X"
                    else:
                        cells[7] = "O"
                else:
                    while cells[7] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["1", "2"]:
                            break

            elif cords == ["1", "3"]:
                if cells[8] == " ":
                    if t % 2 == True:
                        cells[8] = "X"
                    else:
                        cells[8] = "O"
                else:
                    while cells[8] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["1", "3"]:
                            break

            elif cords == ["2", "1"]:
                if cells[3] == " ":
                    if t % 2 == True:
                        cells[3] = "X"
                    else:
                        cells[3] = "O"
                else:
                    while cells[3] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["2", "1"]:
                            break

            elif cords == ["2", "2"]:
                if cells[4] == " ":
                    if t % 2 == True:
                        cells[4] = "X"
                    else:
                        cells[4] = "O"
                else:
                    while cells[4] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["2", "2"]:
                            break

            elif cords == ["2", "3"]:
                if cells[5] == " ":
                    if t % 2 == True:
                        cells[5] = "X"
                    else:
                        cells[5] = "O"
                else:
                    while cells[5] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["2", "3"]:
                            break

            elif cords == ["3", "1"]:
                if cells[0] == " ":
                    if t % 2 == True:
                        cells[0] = "X"
                    else:
                        cells[0] = "O"
                else:
                    while cells[0] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["3", "1"]:
                            break

            elif cords == ["3", "2"]:
                if cells[1] == " ":
                    if t % 2 == True:
                        cells[1] = "X"
                    else:
                        cells[1] = "O"
                else:
                    while cells[1] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["3", "2"]:
                            break

            elif cords == ["3", "3"]:
                if cells[2] == " ":
                    if t % 2 == True:
                        cells[2] = "X"
                    else:
                        cells[2] = "O"
                else:
                    while cells[2] != " ":
                        print("This cell is occupied! Choose another one!")
                        cords = input("Enter coordinates:").split()
                        if cords != ["3", "3"]:
                            break



        zone = f"""
        --------- 
        | {cells[0]} {cells[1]} {cells[2]} |
        | {cells[3]} {cells[4]} {cells[5]} |
        | {cells[6]} {cells[7]} {cells[8]} |
        ---------"""
        print(zone)
        print(m)


if cells[0] == cells[1] == cells[2] == "X":
    print("X wins")
elif cells[0] == cells[1] == cells[2] == "O":
    print("O wins")
elif cells[3] == cells[4] == cells[5] == "X":
    print("X wins")
elif cells[3] == cells[4] == cells[5] == "O":
    print("O wins")
elif cells[6] == cells[7] == cells[8] == "X":
    print("X wins")
elif cells[6] == cells[7] == cells[8] == "O":
    print("O wins")
elif cells[0] == cells[3] == cells[6] == "X":
    print("X wins")
elif cells[0] == cells[3] == cells[6] == "O":
    print("O wins")
elif cells[1] == cells[4] == cells[7] == "X":
    print("X wins")
elif cells[1] == cells[4] == cells[7] == "O":
    print("O wins")
elif cells[2] == cells[5] == cells[8] == "X":
    print("X wins")
elif cells[2] == cells[5] == cells[8] == "O":
    print("O wins")
elif cells[0] == cells[4] == cells[8] == "X":
    print("X wins")
elif cells[0] == cells[4] == cells[8] == "O":
    print("O wins")
elif cells[6] == cells[4] == cells[2] == "X":
    print("X wins")
elif cells[6] == cells[4] == cells[2] == "O":
    print("O wins")
else:
    print("Draw")
