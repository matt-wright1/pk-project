[![codecov](https://codecov.io/gh/NERC-DTP-Students/pk-project/branch/master/graph/badge.svg?token=BHAWWQXNQP)](https://codecov.io/gh/NERC-DTP-Students/pk-project)
[![BCH compliance](https://bettercodehub.com/edge/badge/kyubird/pk-project?branch=master)](https://bettercodehub.com/)
[![Documentation Status](https://readthedocs.org/projects/pharmokinetic-model/badge/?version=latest)](https://pharmokinetic-model.readthedocs.io/en/latest/?badge=latest)
<div id="top"></div>




 

# Pharmokinetic Model

<p>
    A multi-compartment pharmokinetic model with adjustable dosing protocols.
    <br />
    <a href="https://pharmokinetic-model.readthedocs.io/en/latest/index.html"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/NERC-DTP-Students/pk-project/issues">Report Bug</a>
    ·
    <a href="https://github.com/NERC-DTP-Students/pk-project/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS alter this when readme is finalised -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-package">About The Package</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#quickstart">Quickstart</a></li>
        <li><a href="#Example">Example</a></li>
      </ul>
    </li>
    <li><a href="#package-contents">Package Contents</a></li>
    <ul>
        <li><a href="#roadmap">Roadmap</a></li>
    </ul>
    <li><a href="#contributing">Contributing</a></li> 
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#issues">Issues</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Package

This Python library specifies, solves, and visualise the solution of a Pharmokinetics(PK) model. 

The Pharmokinetics model provides a quantitative basis for describing
- delivery of a drug to a patient
- diffusion of that drug through the plasma/body tissue
- and the subsequent clearance of the drug from the patient's system 

This package solves a pharmokinetic model to calculate drug quantities in a central and peripheral compartments as a function of time based on a given dosing strategy. The package outputs either a figure with a single plot displaying drug dose in each compartment over time if one model is being examined or two subplots if two models are being compared. All parameters in the system are fully adjustable. 

### Model schematic
![Example schematic of model!](pk2.svg)

Basic schematic of the PK model shown here with one peripheral compartment. More detail on this model can be found <a href='https://sabs-r3.github.io/software-engineering-projects/01-introduction/index.html'>here</a>.

Image credit: <a href='https://github.com/SABS-R3/software-engineering-projects'> Martin Robins SABS-R3, Software Engineering Projects </a> 

### Adjustable input parameters
The following parameters are adjustable in the <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/inputs.py'>inputs.py</a> file.


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

<p align="right">(<a href="#top">back to top</a>)</p>






<!-- GETTING STARTED -->
## Getting Started
Full documentation is available on <a href='https://pharmokinetic-model.readthedocs.io/en/latest/'>Read The Docs </a>. See below for installation instructions and quickstart.
<!-- Installation-->
### Installation
This package is pip installable and can be installed with the following command  

`pip install `

_Add a section on how to install the code on Friday_
   





<!-- USAGE EXAMPLES -->
### Quickstart

The package is set to run with a default set of parameters defined in <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/inputs.py'>inputs.py</a> . To use the model simply define your parameters for the compartments and dosing protocol in this file, then run <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/pk_main.py'>pk_main.py</a> to produce your graphs.

### Example
An example plot is shown below
![An example plot!](eg1.png)
_For details on how this plot was created and more examples, please refer to the [Documentation](https://pharmokinetic-model.readthedocs.io/en/latest/)_

<p align="right">(<a href="#top">back to top</a>)</p>



# Package contents

This package contains classes for different aspects of the model including Dose, Compartments, Model (formed of a combination of dose and compartments) and Solution. A series of scripts create objects in these classes and find the solution as outlined in the roadmap below. To alter the model changes only need to be made to the <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/inputs.py'>inputs.py</a>  file.
To see an example of this please see the <a href='https://pharmokinetic-model.readthedocs.io/en/latest/'>documentation</a>. 

## Roadmap

This <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/pk_main.py'>pk_main.py</a>  file calls these scripts within the package in the following order to solve the system.
1. <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/input.py'>input.py</a> - imported with chosen parameters for the model
2. <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/check_inputs.py'>create_model.py</a>  - checks that the model inputs make physics sense
3. <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/createmodel.py'>create_model.py</a>  - sets up the model based on the inputs file
4. <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/solver.py'>solver.py</a> - solves the given model
5. <a href='https://github.com/NERC-DTP-Students/pk-project/tree/master/pkmodel/plots.py'>plots.py</a> - plots the output as one or two graphs depending on how many models were initialised



<p align="right">(<a href="#top">back to top</a>)</p>


## Contributing

If you would like to contribute to the project, please get in touch with one of the members of the GitHub organisation <a href="https://github.com/NERC-DTP-Students/people">NERC-DTP-Students </a> and ask to be added as a collaborator.

This project and everyone participating is expected to follow a basic Code of Conduct:
+ Treat all others with respect and dignity.
+ Offer constructive feedback to others' contributions; never be deameaning or dismissive.

Contributors deemed to be in violation of the code of conduct will be removed from the repository.

The general workflow for contributing to the project is as follows:
+ Create an issue on GitHub.
+ Ensure your local copy of the repository is up to date, and branch the repository with a sensible name beginning with the issue number, e.g. '45-solver-broken'.
+ Fix the issue, commit your changes to the branch and push to GitHub. Ensure your commit message includes the issue number, e.g. "#45 Fixed Solver file"
+ Create a pull request for your branch to be merged with the master.
+ This will be reviewed by another collaborator, and then merged with the master.
+ The branch should now be deleted.

You can find the style information in the flake8 file in the repository.

If you have any questions, please contact one of the members of the organisation, as above.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

This project was a collaborative effort by the following NERC DTP students on the DTC software engineering course. For information about this package please contact one of the listed contributors.


Project Link: [https://github.com/NERC-DTP-Students/pk-project](https://github.com/NERC-DTP-Students/pk-project)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* This package was created as part of the University of Oxford DTC Software Engineering course and is based on this <a href='https://github.com/SABS-R3/software-engineering-projects-pk'> example repository </a>
* This README has been created based on this <a href='https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md'> template</a>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Bugs -->

## Issues

There are currently no reported issues. Please report any you find <a href="https://github.com/NERC-DTP-Students/pk-project/issues">here</a>.



<p align="right">(<a href="#top">back to top</a>)</p>

