
# [
# '-*-*-',
# '--*--',
# '----*',
# '*----',
# ]


def create_matrix(col, row):
    matrix = [['-' for r in range(row)]for c in range(col)]
    game = [[0 for r in range(row)]for c in range(col)]
    return [matrix, game]


def generate_bombs(table):
    table[0][0] = 'X'
    table[1][1] = 'X'
    table[3][3] = 'X'
    table[4][4] = 'X'
    table[2][2] = 'X'


def analize_sides(row, col):
    return ''


def add_bomb(r, c, table, game):
    if(table[r-1][c-1] == 'X'):
        game[r][c] += 1
    if((c+1 < len(table[0])) and table[r][c+1] == 'X'):
        game[r][c] += 1
    if(table[r-1][c] == 'X'):
        game[r][c] += 1


def draw_game(table, game):
    for row in range(len(table)):
        for col in range(len(table[row])):
            if(table[row][col] != 'X'):
                add_bomb(row, col, table, game)


[table, game] = create_matrix(5, 5)
generate_bombs(table)

draw_game(table, game)

for r in game:
    print(r)
