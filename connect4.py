def screen(state):
    print " " + "_".join(['_']*7) + " " 
    for line in reversed(state):
        print "|" + ".".join(line) + "|"
    print "|" + "0 1 2 3 4 5 6" + "|" 

state = [ [' ' for line in range(7)] for col in range(6)]
screen(state)

def addToCol(colnum,p):
    for i in range(6):
        if state[i][colnum] == ' ':
            state[i][colnum] = p
            break

def winner(state):

    lines = state

    columns = []    
    for col in range(7):
        column = []
        for line in state:
            column.append(line[col])
        columns.append(column)

    diagonals = []
    for col in range(7):
        diag = []
        offset = 0
        for line in state:
            if col+offset < 7:
                diag.append(line[col+offset])
            offset +=1
        diagonals.append(diag)
    for col in range(7):
        diag = []
        offset = 0
        for line in state:
            if col+offset < 7:
                diag.append(line[col+offset])
            offset -=1
        diagonals.append(diag)


    def win(l):
        s = ''.join(l)
        if 'XXXX' in s: return 'X'
        if 'OOOO' in s: return 'O'
        else: None
    
    for line in lines:
        if win(line): return win(line)
    for col in columns:
        if win(col): return win(col)
    for d in diagonals:
        if win(d): return win(d)

    return None

turn = 0
while winner(state) is None:
    player = 'X' if turn % 2 == 0 else 'O'
    column = -1
    while column<0 or column>6:
        column = input(player + ':   column: ')
    addToCol(column,player)
    screen(state)
    turn += 1

print winner(state), " is the winner"    
