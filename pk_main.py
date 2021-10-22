"""Main code to run the whole model"""

#import functions
from create_model import * #  function to store the initial inputs into classes

#import all the initial input values for the model
from inputs import * # imports a dictionary of all the imputs for the models, and an integer for the number of models

#put the model data into classes and create a solution class with a time array of the solution
if number_of_models == 2:
    model1, model2, solution1, solution2 = create_model(2, model_1_inputs, model_2_inputs)
else:
    model1, solution1 = create_model(1, model_1_inputs)

if __name__ == '__pk_main__'
    pk_main()