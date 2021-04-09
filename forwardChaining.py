from collections import deque

file=open(input('file:'))
line=file.readlines()
line=list(map(lambda s: s.strip(),line))


Rules=[]
for i in range(len(line)):
    k=i+1
    if line[i]=='1) Rules':
        while line[k]!='2) Facts':
            Rules.append(line[k])
            k = k + 1
    elif line[i]=='2) Facts':
        Fact=line[k].split()
    elif line[i]=='3) Goal':
        Goal=line[k]

R=[]
# ------------------------------
print('PART1. Data')
print(' ',end='')
print('1)Rules')
for i in range(len(Rules)):
    rule=Rules[i].split()
    print('     ', end='')
    print('R',i+1,': ',end='')
    for i in rule[1:]:
        print(i,' ',end='')
    print('->',rule[0])
    R.append([rule[1:],rule[0]])

print()
print(' ',end='')
print('2)Facts')
print('     ', end='')
for i in Fact:
    print(i,' ',end='')
print();print()
print(' ',end='')
print('3)Goal')
print('     ', end='')
print(Goal);print()

# ///////////////////////////////////////
Path=[]
Flag=['*']
Flag = deque(Flag)
fact = Fact
for i in Fact:
    fact.append(i)
print('PART2. Trace')
# //////초기값 설정
Yes=False
count=0

while Goal not in Fact and Yes==False: #fact에 최종 원소가 추가되거나 끝까지 했는데도 안 될 때.
    count=count+1
    print(' ', end='')
    print('ITERATION',count)
    K=-1
    apply=False
    while K<len(R)-1 and apply==False: #하나의 적용되는 규칙을 발견할 때까지
        FlagYes = False
        K=K+1
        print('     ', end='')
        print('R', K + 1, ':', end='')
        for i in R[K][0]:
            print(i, '', end='')
        print('->',R[K][-1], end='')

        if str(K+1) in Flag: #깃발 있는 경우
            a=0
            for t in Flag: #인덱스 찾기
                if t!=str(K+1):
                    a += 1
                else:
                    b=a+1
                    break
            if Flag[b]==[1]:
                print(', skip, because flag1 raised')
            elif Flag[b]==[2]:
                print(', skip, because flag2 raised')

        else: #깃발 없다.
            lbool=False
            for i in R[K][0]:
                for j in i:
                    if lbool==False:
                        if j in Fact:
                            if R[K][1] in Fact:  # 우변이 이미 있는 경우
                                Flag.append(str(K+1));Flag.append([2])
                                print(' not applied, because RHS in facts. Raise flag2')
                                FlagYes = True
                                apply=False
                            else:
                                apply = True
                                P=K+1
                                break
                        else:
                            apply=False
                            print(', not applied, because of lacking ', j)
                            lbool=True
        if apply==True:
            Fact.append(R[P-1][-1])
            Flag.append(str(P));Flag.append([1])
            Path.append(P)
            if '*' in Flag:
                Flag.popleft()
            print(', apply, Raise flag1. Facts',' ', end='')
            for i in Fact:
                print(i,' ', end='')
            print()
        elif apply==False and K>len(R)-2:
            Yes=True

print()
print('PART3. Results')
if Goal in fact:
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
