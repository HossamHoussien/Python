## Introduction

Workforce planning is a continual process used to align the needs and priorities of the organization with those of its workforce to ensure it can meet its legislative, regulatory, service and production requirements and organizational objectives. Workforce planning enables evidence based workforce development strategies
________________________________________
## Problem Definition

Consider a restaurant that is open seven days a week. Based on past experience, the number of workers needed on a particular day is given as follows:

Day	| Mon 	| Tue 	| Wed 	| Thu 	| Fri 	| Sat 	| Sun 
| ----- |:-----:|:-----:|:-----:|:-----:|:-----:|:-----:| -----:|
Number 	| 14 	| 13 	| 15 	| 16 	| 19 	| 18 	| 11 


Every worker works five consecutive days, and then takes two days off, repeating this pattern. How can we minimize the number of workers that staff the restaurant?
________________________________________
## Formulation

#### Decision Variables:
Let the days be numbers from 1 through 7, and let X_i be the number of workers who begin their five day shift on day i.
Objective Function:
The objective function is to minimize the number of workers 
∑_(i=1)^7▒X_i 

#### Constraints:
Consider the constraints for Monday’s staffing level of 14. Who works on Mondays?

Clearly, those who start their shift on Monday (X_i). 
Those who start on Tuesday (X_2) don not work on Monday nor do those who start on Wednesday (X_3)
Those who start on Thursday (X_4) do work on Monday, as do those who start on Friday, Saturday, and Sunday, and this works the same on all days.


Monday:		X_1+ X_4+ X_5+X_6+X_7≥14

Tuesday:  	X_1+ X_2+X_5+X_6+X_7≥13

Wednesday:   	X_1+X_2+X_3+X_6+X_7≥15

Thursday:   	X_1+X_2+X_3+X_4+X_5≥16

Friday:   	X_1+X_2+X_3+X_4+X_5≥19

Saturday:   	X_2+X_3+X_4+X_5+X_6≥18

Sunday:   	X_3+X_4+X_5+X_6+X_7≥11

X_1+X_2+X_3+ X_4+ X_5+X_6+X_7≥0
