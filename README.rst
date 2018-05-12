risk-rolled
============

risk-rolled is a simple python terminal application that
makes playing risk significantly faster.  It provides a simple
and intuitive CLI that automatically "rolls the dice" and finds the wins/losses.

Example
--------

::
	ruler@dayley-Inspiron-3558 ~/risk-rolled $ ./risk_rolled 
	a,attack -> run an attack
	q,quit   -> quit the cli
	h,help   -> print this help message
	    
	Enter Command: a
	Input Attacking Armies: 5
	Input Defending Armies: 3
	Input Attacking Dice [1, 3]: 3
	Input Defending Dice [1, 2]: 2
	Attacking With 3 Dice
	Defending With 2 Dice
	[4, 2, 1]
	[4, 2]
	Attacker Lost: 2
	Defender Lost: 0
	Attacker Armies Remaining: 3
	Defender Armies Remaining: 3
	Continue Attacking? (Y/n): y
	Attacking With 2 Dice
	Defending With 2 Dice
	[2, 2]
	[6, 2]
	Attacker Lost: 2
	Defender Lost: 0
	Attacker Armies Remaining: 1
	Defender Armies Remaining: 3
	Attackers Repulsed!
	Enter Command: a
	Input Attacking Armies: 5
	Input Defending Armies: 2
	Input Attacking Dice [1, 3]: 3
	Input Defending Dice [1, 2]: 2
	Attacking With 3 Dice
	Defending With 2 Dice
	[6, 2, 2]
	[4, 2]
	Attacker Lost: 1
	Defender Lost: 1
	Attacker Armies Remaining: 4
	Defender Armies Remaining: 1
	Continue Attacking? (Y/n): 
	Attacking With 3 Dice
	Defending With 1 Dice
	[5, 5, 4]
	[4]
	Attacker Lost: 0
	Defender Lost: 1
	Attacker Armies Remaining: 4
	Defender Armies Remaining: 0
	Attackers Won!
	Enter Command: q

Installation
--------------

Simply clone the git repository.
PyPi Package coming soon!
