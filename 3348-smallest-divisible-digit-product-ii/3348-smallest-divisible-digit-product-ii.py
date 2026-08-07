# from collections import deque
# class Solution:


#     @staticmethod
#     def smallestNumber(num: str, t: int) -> str:
#         a = b = c = d = 0
#         tt = t
#         while tt % 2 == 0: tt //= 2; a += 1
#         while tt % 3 == 0: tt //= 3; b += 1
#         while tt % 5 == 0: tt //= 5; c += 1
#         while tt % 7 == 0: tt //= 7; d += 1
#         if tt != 1:
#             return "-1"

#         digit_e2 = {2:1,3:0,4:2,5:0,6:1,7:0,8:3,9:0}
#         digit_e3 = {2:0,3:1,4:0,5:0,6:1,7:0,8:0,9:2}
#         candidates = [2,3,4,6,8,9]

#         def build_mincost(A, B, allowed):
#             INF = float('inf')
#             dist = [[INF]*(B+1) for _ in range(A+1)]
#             dist[0][0] = 0
#             q = deque([(0,0)])
#             while q:
#                 i, j = q.popleft()
#                 base = dist[i][j]
#                 for dgt in allowed:
#                     ni = min(A, i + digit_e2[dgt])
#                     nj = min(B, j + digit_e3[dgt])
#                     if dist[ni][nj] > base + 1:
#                         dist[ni][nj] = base + 1
#                         q.append((ni, nj))
#             return dist

#         minCost23 = build_mincost(a, b, candidates)
#         level_tables = [build_mincost(a, b, candidates[idx:]) for idx in range(len(candidates))]

#         def build_23(A0, B0):
#             k2 = minCost23[A0][B0]
#             res = []
#             cur_a, cur_b, remaining, min_idx = A0, B0, k2, 0
#             for _ in range(k2):
#                 for idx in range(min_idx, len(candidates)):
#                     dgt = candidates[idx]
#                     na = max(0, cur_a - digit_e2[dgt])
#                     nb = max(0, cur_b - digit_e3[dgt])
#                     if level_tables[idx][na][nb] <= remaining - 1:
#                         res.append(dgt)
#                         cur_a, cur_b = na, nb
#                         remaining -= 1
#                         min_idx = idx
#                         break
#             return res

#         def fill(L, A0, B0, C0, D0):
#             k2 = minCost23[A0][B0]
#             ones = L - (C0 + D0 + k2)
#             tail = ['5']*C0 + ['7']*D0 + [str(x) for x in build_23(A0, B0)]
#             tail.sort()
#             return '1'*ones + ''.join(tail)

#         n = len(num)
#         pre2 = [0]*(n+1); pre3 = [0]*(n+1); pre5 = [0]*(n+1); pre7 = [0]*(n+1)
#         for i, ch in enumerate(num):
#             dgt = int(ch)
#             pre2[i+1] = pre2[i] + digit_e2.get(dgt, 0)
#             pre3[i+1] = pre3[i] + digit_e3.get(dgt, 0)
#             pre5[i+1] = pre5[i] + (1 if dgt == 5 else 0)
#             pre7[i+1] = pre7[i] + (1 if dgt == 7 else 0)

#         if '0' not in num and pre2[n] >= a and pre3[n] >= b and pre5[n] >= c and pre7[n] >= d:
#             return num

#         zfirst = num.find('0')
#         max_i = n - 1 if zfirst == -1 else zfirst

#         for i in range(max_i, -1, -1):
#             ra = max(0, a - pre2[i]); rb = max(0, b - pre3[i])
#             rc = max(0, c - pre5[i]); rd = max(0, d - pre7[i])
#             low = max(1, int(num[i]) + 1)
#             remaining_length = n - 1 - i
#             for dgt in range(low, 10):
#                 na = max(0, ra - digit_e2.get(dgt, 0)); nb = max(0, rb - digit_e3.get(dgt, 0))
#                 nc = max(0, rc - (1 if dgt == 5 else 0)); nd = max(0, rd - (1 if dgt == 7 else 0))
#                 needed = nc + nd + minCost23[na][nb]
#                 if needed <= remaining_length:
#                     return num[:i] + str(dgt) + fill(remaining_length, na, nb, nc, nd)

#         minimal_full_k = c + d + minCost23[a][b]
#         L = max(n + 1, minimal_full_k)
#         return fill(L, a, b, c, d)



class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def build_end(req, size):
            res = []
            for f in range(9, 1, -1):
                while req % f == 0:
                    req //= f
                    res.append(str(f))
            if len(res) < size: res += ['1'] * (size - len(res))
            return "".join(res[::-1])        
        
        n = len(num)

        curr = t
        for f in [2, 3, 5, 7]:
            while curr % f == 0:
                curr //= f
        if curr != 1: return '-1'

        rem = [0] * (n + 1)
        rem[0] = t
        for i in range(n):
            if num[i] == '0': break
            rem[i + 1] = rem[i] // gcd(rem[i], int(num[i]))
        if rem[-1] == 1: return num

        z = num.find('0')
        start = z if z != -1 else n - 1

        for i in range(start, -1, -1):
            end_size = n - i - 1
            for d in range(int(num[i]) + 1, 10):
                last = build_end(rem[i] // gcd(rem[i], d), end_size)
                if len(last) == end_size: return num[:i] + str(d) + last
        
        return build_end(t, n + 1)

        

































