# ForwardChaining

This is a Python program that solves problems with forward chaining.



## Problem Description

Forward chaining is a method of deduction to find terminal state. It starts with state we have. It'll try to find a rule whose LHS is/are in facts. When it finds a rule, RHS of the rule is added to facts. This process to find a rule is one iteration. When a rule is applied once, it'll be skipped in next iteration. Then try next iteration to
find a rule till facts include goal or check all rules but there is no rules for goal. Forward chaining is data-oriented method, in the sense of using knowledge we have in advance and expending it to get a goal. This aspects contrast to the method of backward chaining that will be mentioned after forward chaining.



## Pseudo code

```
variables
	Fact: list, consists of elements that now I have.
	Goal: list, termial state.
	Path: list.
	Yes: bool.
	count: int, number of interation
	apply: bool, represents whether each iteration finds a rule applied.
	FlagYes: bool, represents if each rule has a flag

setting initial values
	Yes= False
	count=0

[main program]
repeat if Fact does not have Goal and each interation finds a rule corresponds to Fact
	start iteration, count the number of iteration
	set apply=False
	repeat until the iteration finds a rule or all rules are considered.
	set FlagYes=False
	if FlagYes=False. i.e there is a flag in the rule.
		if the rule has flag1
			skip the rule, because flag1 raised
		elif the rule has flag2
			skip ther rule, because flag2 raised
	else. i.e there is no flag in the rule.
		if RHS of the rule is already in Fact
			add the rule and flagnum2 in Flag
		else
			the rule applied.
			apply=True
			
	if apply=True
		add the rule and flagnum1 in Flag
		add RHS of the rule in Fact
		add rule number in Path
	else if there is no rule
		Yes=True
```



## Input & Output

- Input : A text file that contains rules, fact and goal to deal with. 

  Example of Input - Testcase 1

  ```
  Test 1. Initial fact in right hand side
  1) Rules
  L A
  K L
  A D
  M D
  Z F B
  F C D
  D A
  2) Facts
  A B C
  3) Goal
  Z
  
  ```

  

- Output : Data, Trace and Results

  Example of Output - Testcase 1

  ```
  /opt/anaconda3/bin/python3.8 /Users/johyeonyoon/PycharmProjects/ai/Forward-chaining/forwardChaining.py
  file:test1.txt
  PART1. Data
   1)Rules
       R 1 : A  -> L
       R 2 : L  -> K
       R 3 : D  -> A
       R 4 : D  -> M
       R 5 : F  B  -> Z
       R 6 : C  D  -> F
       R 7 : A  -> D
  
   2)Facts
       A  B  C  
  
   3)Goal
       Z
  
  PART2. Trace
   ITERATION 1
       R 1 :A -> L, apply, Raise flag1. Facts  A  B  C  L  
   ITERATION 2
       R 1 :A -> L, skip, because flag1 raised
       R 2 :L -> K, apply, Raise flag1. Facts  A  B  C  L  K  
   ITERATION 3
       R 1 :A -> L, skip, because flag1 raised
       R 2 :L -> K, skip, because flag1 raised
       R 3 :D -> A, not applied, because of lacking  D
       R 4 :D -> M, not applied, because of lacking  D
       R 5 :F B -> Z, not applied, because of lacking  F
       R 6 :C D -> F, not applied, because of lacking  D
       R 7 :A -> D, apply, Raise flag1. Facts  A  B  C  L  K  D  
   ITERATION 4
       R 1 :A -> L, skip, because flag1 raised
       R 2 :L -> K, skip, because flag1 raised
       R 3 :D -> A not applied, because RHS in facts. Raise flag2
       R 4 :D -> M, apply, Raise flag1. Facts  A  B  C  L  K  D  M  
   ITERATION 5
       R 1 :A -> L, skip, because flag1 raised
       R 2 :L -> K, skip, because flag1 raised
       R 3 :D -> A, skip, because flag2 raised
       R 4 :D -> M, skip, because flag1 raised
       R 5 :F B -> Z, not applied, because of lacking  F
       R 6 :C D -> F, apply, Raise flag1. Facts  A  B  C  L  K  D  M  F  
   ITERATION 6
       R 1 :A -> L, skip, because flag1 raised
       R 2 :L -> K, skip, because flag1 raised
       R 3 :D -> A, skip, because flag2 raised
       R 4 :D -> M, skip, because flag1 raised
       R 5 :F B -> Z, apply, Raise flag1. Facts  A  B  C  L  K  D  M  F  Z  
  
  PART3. Results
      1) Goal Z achieved
      2) Path:R 1  R 2  R 7  R 4  R 6  R 5  
  Process finished with exit code 0
  
  ```

  
