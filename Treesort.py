import DictBinTree as dbt
import sys

T = dbt.DictBinTree()

n = 0
for line in sys.stdin:
    T.insert(int(line))
    n = n+1

print()
res = T.orderedTraversal()

for i in range(n):
    print(res[i])