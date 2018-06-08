from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
    # Instantiate a Glop solver, naming it WorkforcePlanningProblemSolver.
    solver = pywraplp.Solver('WorkforcePlanningProblemSolver', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # Create decision variables and set min and max value for each
    x1 = solver.IntVar(0, solver.infinity(), 'Who Start Their Shift on Monday')
    x2 = solver.IntVar(0, solver.infinity(), 'Who Start Their Shift on Tuesday')
    x3 = solver.IntVar(0, solver.infinity(), 'Who Start Their Shift on Wednesday')
    x4 = solver.IntVar(0, solver.infinity(), 'Who Start Their Shift on Thursday')
    x5 = solver.IntVar(0, solver.infinity(), 'Who Start Their Shift on Friday')
    x6 = solver.IntVar(0, solver.infinity(), 'Who Start Their Shift on Saturday')
    x7 = solver.IntVar(0, solver.infinity(), 'Who Start Their Shift on Sunday')

    # Who Works on Monday ?
    # Monday + Thursday + Friday + Saturday + Sunday >= 14
    # x1 + x4 + x5 + x6 + x7 >= 14
    Monday = solver.Constraint(14, solver.infinity())
    Monday.SetCoefficient(x1, 1)
    Monday.SetCoefficient(x4, 1)
    Monday.SetCoefficient(x5, 1)
    Monday.SetCoefficient(x6, 1)
    Monday.SetCoefficient(x7, 1)

    # Who Works on Tuesday ?
    # Monday + Tuesday + Friday + Saturday + Sunday >= 13
    # x1 + x2 + x5 + x6 + x7 >= 13
    Tuesday = solver.Constraint(13, solver.infinity())
    Tuesday.SetCoefficient(x1, 1)
    Tuesday.SetCoefficient(x2, 1)
    Tuesday.SetCoefficient(x5, 1)
    Tuesday.SetCoefficient(x6, 1)
    Tuesday.SetCoefficient(x7, 1)  
    
    # Who Works on Wednesday ?
    # Monday + Tuesday + Wednesday + Saturday + Sunday >= 15
    # x1 + x2 + x3 + x6 + x7 >= 15
    Wednesday = solver.Constraint(15, solver.infinity())
    Wednesday.SetCoefficient(x1, 1)
    Wednesday.SetCoefficient(x2, 1)
    Wednesday.SetCoefficient(x3, 1)
    Wednesday.SetCoefficient(x6, 1)
    Wednesday.SetCoefficient(x7, 1)   
    
    # Who Works on Thursday ?
    # Monday + Tuesday + Wednesday + Thursday + Sunday >= 16
    # x1 + x2 + x3 + x4 + x7 >= 16
    Thursday = solver.Constraint(16, solver.infinity())
    Thursday.SetCoefficient(x1, 1)
    Thursday.SetCoefficient(x2, 1)
    Thursday.SetCoefficient(x3, 1)
    Thursday.SetCoefficient(x4, 1)
    Thursday.SetCoefficient(x7, 1)       
    
    # Who Works on Friday ?
    # Monday + Tuesday + Wednesday + Thursday + Friday >= 19
    # x1 + x2 + x3 +  x4 + x5 >= 19
    Firday = solver.Constraint(19, solver.infinity())
    Firday.SetCoefficient(x1, 1)
    Firday.SetCoefficient(x2, 1)
    Firday.SetCoefficient(x3, 1)
    Firday.SetCoefficient(x4, 1)
    Firday.SetCoefficient(x5, 1) 
    
    # Who Works on Saturday ?
    # Tuesday + Wednesday + Thursday + Friday + Saturday >= 18
    # x2 + x3 +  x4 + x5 + x6 >= 18
    Saturday = solver.Constraint(18, solver.infinity())
    Saturday.SetCoefficient(x2, 1)
    Saturday.SetCoefficient(x3, 1)
    Saturday.SetCoefficient(x4, 1)
    Saturday.SetCoefficient(x5, 1)
    Saturday.SetCoefficient(x6, 1)
    
    # Who Works on Sunday ?
    # Wednesday + Thursday + Friday + Saturday + Sunday >= 11
    # x3 +  x4 + x5 + x6 + x7 >= 15
    Sunday = solver.Constraint(11, solver.infinity())
    Sunday.SetCoefficient(x3, 1)
    Sunday.SetCoefficient(x4, 1)
    Sunday.SetCoefficient(x5, 1)
    Sunday.SetCoefficient(x6, 1)
    Sunday.SetCoefficient(x7, 1)
      

    
    # Objective function:  Minimize the Number of Workers 
    # Min x1 + x2 + x3 + x4 + x5 + x6 + x7
    objective = solver.Objective()
    objective.SetCoefficient(x1, 1)
    objective.SetCoefficient(x2, 1)
    objective.SetCoefficient(x3, 1)
    objective.SetCoefficient(x4, 1)
    objective.SetCoefficient(x5, 1)
    objective.SetCoefficient(x6, 1)
    objective.SetCoefficient(x7, 1)
    objective.SetMinimization()

    # Solve the system.
    solver.Solve()
    
    optimal_solution = x1.solution_value() + x2.solution_value() + x3.solution_value() + x4.solution_value() + x5.solution_value() + x6.solution_value() + x7.solution_value()
    print('Number of Variables =', solver.NumVariables())
    print('Number of Constraints =', solver.NumConstraints())
    print('_________________________________________________')

    # The value of each variable in the solution.
    print('Variables:')
    print(x1.name(), ' =',  x1.solution_value())
    print(x2.name(), ' =',  x2.solution_value())
    print(x3.name(), ' =',  x3.solution_value())
    print(x4.name(), ' =',  x4.solution_value())
    print(x5.name(), ' =',  x5.solution_value())
    print(x6.name(), ' =',  x6.solution_value())
    print(x7.name(), ' =',  x7.solution_value())
    print('_________________________________________________')

    # The objective value of the solution.
    print('Ojective Function:')
    print('Minimum the Number of Workers =', optimal_solution)
    

if __name__ == '__main__':
    main()
