def docTapTin(fpath="MADITUAN.INP"):
    with open(fpath, "rt") as file:
        content = file.read().split()
        n = int(content[0])
        x0 = int(content[1])
        y0 = int(content[2])
    return n, x0, y0


def InDapAn(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


def LietKeMa(n, x0, y0):
    board = [[0]*n for _ in range(n)]

    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]

    board[x0][y0] = 1

    info = dict(
        board=board,
        n=n,
        dx=dx,
        dy=dy,
        cnt=0,
        isprint=False
    )

    TryMa(2, x0, y0, info)
    print(info["cnt"])

    board = [[0]*n for _ in range(n)]
    board[x0][y0] = 1

    info = dict(
        board=board,
        n=n,
        dx=dx,
        dy=dy,
        cnt=0,
        isprint=True
    )

    TryMa(2, x0, y0, info)


def TryMa(step, x, y, info):
    board, n, dx, dy = info["board"], info["n"], info["dx"], info["dy"]

    if step > n*n:
        info["cnt"] += 1
        if info["isprint"]:
            InDapAn(board)
        return

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = step
            TryMa(step+1, nx, ny, info)
            board[nx][ny] = 0


def main(sfile, **kwargs):
    n, x0, y0 = docTapTin(sfile)
    LietKeMa(n, x0, y0)
    kwargs.get("debug",{}).update(locals())


def test1(**kwargs):
    n, x0, y0 = docTapTin("MADITUAN.INP")

    print('-'*5, 'DOC FILE', '-'*5)
    print(f'n = {n}, x0 = {x0}, y0 = {y0}')
    print('Ket qua: ')
    LietKeMa(n, x0, y0)

    kwargs.get("debug",{}).update(locals())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, default="help", help='test1, main')
    parser.add_argument('--file', type=str, default="MADITUAN.INP", help='file path')
    args, _ = parser.parse_known_args()
    params  = vars(args)

    if params['action'] == "test1":
        test1(debug=globals())
    elif params['action'] == "main":
        main(sfile=params['file'], debug=globals())
    else:
        parser.print_help()