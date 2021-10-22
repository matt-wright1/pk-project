Examples
=========

Here are two examples of how to use the model.

.. toctree::
   :hidden:
   :maxdepth: 1

Example - Single model
------------------------
This an example for a one compartment model with intravenous bolus continuous dosing.

1. Change inputs in inputs.py. Set parameters to zero for compartments you do not want. If number of models (compartments) is set to one all the parameters for model (compartment) 2 will be ignored even if non zero.

   .. literalinclude:: ../pkmodel/examples/inputs_e1.py
       :language: python3

2. Run pk_main.py
   .. code-block:: bash
   python3 pk_main.py

3. One graph is produced as one model is bein considered
   ..image:: ../pk-model/examples/eg1.png

Example - Compare two models
-----------------------------
This a example compares two one compartment models with intravenous bolus and subcutaneous continuous dosing but respectively.

1. Change inputs in inputs.py. Set parameters to zero for compartments you do not want.

.. literalinclude:: ../pkmodel/examples/inputs_e2.py
   :language: python3

2. Run pk_main.py
   .. code-block:: bash
   python3 pk_main.py

3. Two graphs are produced to enable comparison of the models.
   ..image:: ../pkmodel/examples/eg2.png