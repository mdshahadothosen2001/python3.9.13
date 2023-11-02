n = int(input())
english = list(map(str, input().strip().split()))[:n]
b = int(input())
french = list(map(str, input().strip().split()))[:b]
resut = [x for x in english if x not in french]
print(len(resut))

"""
Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output
4
"""