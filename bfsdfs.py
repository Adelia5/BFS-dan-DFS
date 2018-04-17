#awal = A
#tujuan = E
#jalur

#awal2 = A
#tujuan2 = E
#jalur2

#awal2 = A
#tujuan2 = E
#jalur3


peta1 =  {'A':set(['B','H','G']),
         'B':set(['A','D','F']),
         'C':set(['F']),
         'D':set(['B','E']),
         'E':set(['D']),
         'F':set(['B','C']),
         'G':set(['A']),
         'H':set(['A'])}

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:
        jalur = queue.pop(0)

        state = jalur[-1]

        if state == tujuan:
            return jalur

        elif state not in visited:
            for cabang in graf.get(state, []):
                jalur_baru = list(jalur)
                jalur_baru.append(cabang)
                queue.append(jalur_baru)
                print(queue)

            visited.add(state)

            isi = len(queue)
            if isi == 0:
                print("Tidak ditemukan")

def dfs(graf2, mulai2,tujuan2):
    stack = [[mulai2]]
    visited2 = set()

    while stack:
            jalur2 = stack.pop(-1)

            state2 = jalur2[-1]

            if state2 == tujuan2:
                return jalur2
            elif state2 not in visited2:
                for cabang2 in graf2.get(state2, []):
                    jalur_baru2 = list(jalur2)
                    jalur_baru2.append(cabang2)
                    stack.append(jalur_baru2)
                    print(stack)

                visited2.add(state2)

            isi2 = len(stack)
            if isi2 == 0:
                print("Tidak ditemukan")


print("Hasil dari BFS: ")
print(bfs(peta1,'A','E'))

print("Hasil dari DFS: ")
print(dfs(peta1,'A','E'))
