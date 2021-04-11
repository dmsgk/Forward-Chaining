from collections import deque
import copy

file=open(input('file:'))
line=file.readlines()
line=list(map(lambda s: s.strip(),line))

R = []
for i in range(len(line)):
    k=i+1
    if line[i]=='1) Rules':
        while line[k] != '2) Facts':
            r = deque(line[k].split())
            rhs = r.popleft()
            r.append(rhs)
            R.append(list(r))
            k = k + 1
    elif line[i]=='2) Facts':
        Fact=line[k].split()
    elif line[i]=='3) Goal':
        Goal=line[k]

# ------------------------------
print('PART1. Data')
print(' 1)Rules')
for i in range(len(R)):
    print('     R', i+1, ': ', end='')
    for j in range(len(R[i])-1):
        print(R[i][j], end= ' ')
    print('->', R[i][-1])

print()
print(' 2)Facts')
print('     ', end='')
for i in Fact:
    print(i,' ',end='')
print();print()

print(' 3)Goal')
print('     ', Goal)

# -------------------------------------
Path=[]
Flag=[]
origin_fact = copy.deepcopy(Fact)

print('PART2. Trace')
# 초기값 설정
count=0
Yes = False
while Goal not in Fact and Yes==False: #fact에 최종 원소가 추가되거나 끝까지 했는데도 안 될 때.
    count += 1
    print(' ', end='')
    print('ITERATION',count)
    K=-1
    apply = False
    while K<len(R)-1 and not apply: #하나의 적용되는 규칙을 발견할 때까지
        K=K+1
        print('     R', K + 1, ': ', end='')
        for i, v in enumerate(R[K]):     # K번째 규칙 프린트(R[K])
            if i < len(R[K]) -1:
                print(v, '', end='')
            else:
                print('->',v, end='')

        if str(K+1) in Flag: #깃발 있는 경우
            b = Flag.index(str(K+1)) +1
            if Flag[b]==[1]:
                print(', skip, because flag1 raised')
            elif Flag[b]==[2]:
                print(', skip, because flag2 raised')

        else: #깃발 없다.
            for i, v in enumerate(R[K]):  # k번째 규칙의 좌변이 모두 있는지.
                if i == len(R[K]) -1:
                    continue

                if v in Fact:
                    if R[K][-1] in Fact:  # 우변이 이미 있는 경우
                        print(' not applied, because RHS in facts. Raise flag2')
                        Flag.append(str(K + 1));  Flag.append([2])
                        break
                    elif v == R[K][-2]:
                        apply = True
                        P=K+1
                        break
                else:
                    print(', not applied, because of lacking ', v)
                    break

            if apply:
                Fact.append(R[P-1][-1])
                Flag.append(str(P)); Flag.append([1])
                Path.append(P)
                print(', apply, Raise flag1. Facts ', end='')
                for i in Fact:
                    print(i,' ', end='')
                print()
            elif K== len(R)-1:
                Yes=True


print()
print('PART3. Results')
if Goal in origin_fact:
    print('    ', end='')
    print('Goal A in facts. Empty path.')
else:
    if Goal in Fact:
        print('    ',end='')
        print('1) Goal',Goal,'achieved')
        print('    ', end='')
        print('2) Path:', end='')
        for i in Path:
            print('R', i, ' ', end='')
    else:
        print('1) Goal',Goal,' not achieved')