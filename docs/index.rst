.. Pharmokinetic Model documentation master file, created by
   sphinx-quickstart on Thu Oct 21 16:44:09 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pharmokinetic Model's documentation!
===============================================
This documentation is for the Pharmokinetic Model package.
See below for quickstart and examples and use the sidebar to explore different classes and functions.

Scientific background
------------------------
This Python library specifies, solves, and visualise the solution of a Pharmokinetics(PK) model. 

The Pharmokinetics model provides a quantitative basis for describing
- delivery of a drug to a patient
- diffusion of that drug through the plasma/body tissue
- and the subsequent clearance of the drug from the patient's system 

This package solves a pharmokinetic model to calculate drug quantities in a central and peripheral compartments as a function of time based on a given dosing strategy. The package outputs either a figure with a single plot displaying drug dose in each compartment over time if one model is being examined or two subplots if two models are being compared. All parameters in the system are fully adjustable. 
More detail on this model can be found .. _here http://www.python.org/https://sabs-r3.github.io/software-engineering-projects/01-introduction/index.html. 

Adjustable parameters
^^^^^^^^^^^^^^^^^^^^^
The following parameters are adjustable in the inputs.py file.


**Time**

Length of time to solve for the amount of drug in each compartment.

**Central Compartment**

+ Volume (mL)
+ Initial drug amount (ng)
+ Clearance (mL/h)

**Peripheral Compartments**

+ Number of peripheral compartments (1, 2)
+ Volume (mL)
+ Initial drug amount (ng)
+ Flux to central compartment (mL/h)

**Dosing**

+ Continuous dosing amount (ng/hr)
+ Instantaneous dosing amount (ng)
+ Instantaneous dose times (hr)
+ Subcutaneous/intravenous bolus dosing
    + For subcutaneous dosing the absorption rate (/h) can also be adjusted

Quickstart
----------
----------

1. Install this package
   .. code-block:: bash

   pip3 install -i https://test.pypi.org/simple/pkmodel

2. Edit your system parameters in inputs.py
3. Run pk_main.py
4. Save the resulting figure in a directory of your choice. If you want to change the title of the plot you will need to do this manually in plot.py

Examples
--------
---------

.. toctree::
    :hidden:
   
    examples

The :doc:`examples` section contains two example uses of the package to help you get started.

Exploration
-----------
-----------

.. toctree::
    :hidden:
   
    documentation

The :doc:`documentation` section contains the documentation for the classes and functions within the package.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
