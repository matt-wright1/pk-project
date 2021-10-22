"""Main code to run the whole model"""
#from pkmodel.dose import Dose

#import functions

#from create_model import * #  function to store the initial inputs into classes

#import all the initial input values for the model
from pkmodel.inputs import * # imports a dictionary of all the imputs for the models, and an integer for the number of models
from pkmodel.createmodel import create_model
from pkmodel.solver import solve

#put the model data into classes and create a solution class with a time array of the solution
number_of_models = 1
if number_of_models == 2:
    model1, model2, solution1, solution2 = create_model(2, model_1_inputs, model_2_inputs)
else:
    model, solution = create_model(1, model_1_inputs)

sol = solve(model, solution)

if __name__ == '__main__':
    pk_main()