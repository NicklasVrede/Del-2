import DictBinTree as dbt
import sys

T = dbt.createEmptyDict()

n = 0
for line in sys.stdin:
    dbt.insert(T, int(line))
    n = n+1

print()
print(dbt.orderedTraversal(T))