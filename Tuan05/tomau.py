def docTapTin(fpath="TOMAU.INP"):
    with open(fpath, "rt") as file:
        lines = file.readlines()

    n = int(lines[0])
    edges = []

    for line in lines[1:]:
        u, v = map(int, line.split())
        edges.append((u, v))

    return n, edges


def InDapAn(k, groups):
    print(k)
    for g in groups:
        print(*g)


def LietKeToMau(n, edges):

    adj = [[] for _ in range(n+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    color = [0]*(n+1)

    def hopLe(u, c):
        for v in adj[u]:
            if color[v] == c:
                return False
        return True

    def Try(u, k):
        if u > n:
            return True

        for c in range(1, k+1):
            if hopLe(u, c):
                color[u] = c
                if Try(u+1, k):
                    return True
                color[u] = 0

        return False

    for k in range(1, n+1):
        if Try(1, k):
            groups = [[] for _ in range(k)]
            for i in range(1, n+1):
                groups[color[i]-1].append(i)
            return k, groups


def main(sfile, **kwargs):
    n, edges = docTapTin(sfile)

    k, groups = LietKeToMau(n, edges)

    InDapAn(k, groups)

    kwargs.get("debug",{}).update(locals())


def test1(**kwargs):
    n, edges = docTapTin("TOMAU.INP")

    print('-'*5, 'DOC FILE', '-'*5)
    print(f'n = {n}, edges = {edges}')
    print('Ket qua:')

    k, groups = LietKeToMau(n, edges)

    InDapAn(k, groups)

    kwargs.get("debug",{}).update(locals())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, default="help", help='test1, main')
    parser.add_argument('--file', type=str, default="TOMAU.INP", help='file path')
    args, _ = parser.parse_known_args()
    params  = vars(args)

    if params['action'] == "test1":
        test1(debug=globals())
    elif params['action'] == "main":
        main(sfile=params['file'], debug=globals())
    else:
        parser.print_help()