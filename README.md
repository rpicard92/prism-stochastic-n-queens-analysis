# prism-stochastic-n-queens-analysis
These files are meant to be used in conjunction with the PRISM Probabilistic Model Checker.

## Git Directory Information:
1) The Python files at the top level directiory may be run with the command "(insert_path_to_top_level_git_directory_with_the_python_files)\python (insert_python_file_name).py (insert_number_of_queens)" from the Windows/Linux Terminals (Assuming python is installed on the local machine). The Python files generate the PRISM model files (.prism files) found in the gen_files directory.

Description of Python files:
a) exp_col_move.py
    Description: generates a file in ./gen_files which can run experiments. The file will contain transitions necessary for the random move algorithm on an NxN board where N is a commandline argument.
b) exp_col_swap.py
    Description: generates a file in ./gen_files which can run experiments. The file will contain transitions necessary for the random swap algorithm on an NxN board where N is a commandline argument.
c) exp_sim_anneal_atm.py
    Description: generates a file in ./gen_files which can run experiments. The file will contain transitions necessary for the simulated annealing algorithm on an NxN board where N is a commandline argument. The iteration counter, in this case, is based on the number of attempted swaps. 
d) exp_sim_anneal_suc.py
    Description: generates a file in ./gen_files which can run experiments. The file will contain transitions necessary for the simulated annealing algorithm on an NxN board where N is a commandline argument. The iteration counter, in this case, is based on the number of successful swaps. 
e) gen_col_move.py
    Description: generates a file in ./gen_files which can run simulations, but not experiments. The file will contain transitions necessary for the random move algorithm on an NxN board where N is a commandline argument.
f) gen_col_swap.py
    Description: generates a file in ./gen_files which can run simulations, but not experiments. The file will contain transitions necessary for the random swap algorithm on an NxN board where N is a commandline argument.
g) gen_sim_anneal.py
    Description: generates a file in ./gen_files which can run simulations, but not experiments. The file will contain transitions necessary for the simulated annealing algorithm on an NxN board where N is a commandline argument.

2) The ./gen_files directory contains the PRISM model files that have been generated using the python files, as well as a prop.props property file.

## Running a PRISM experiment.
1) Start PRISM (GUI)
2) At the top toolbar click Model -> Open model, then navigate to the ./gen_files directory and open the "exp" model file (e.g. exp_col_move4.prism) you wish to run. (Note for experiments you must select a file with "exp" in the title. If you select another file you will only be able to run simulations, not experiments. If you wish to just run simulations then these other files are a little less computationally expensive.)
3) At the top toolbar click Properties -> Open properties list, then navigate to the ./gen_files directory and open the "prop.props" property file.
4) At the bottom of the PRISM GUI click the Properties tab to open up the properties and experiments view.
4) At the top toolbar click Properties -> New experiment. 
5) On the pop up menu, change the radio dial button from "Single Value" to "Range: Start End Stop".
6) In the start box type 0.
7) In the end box type the transition number (iteration) integer value you wish to end at (recommended to start with 20 and progress from there).
8) In the step box type the integer step values at which you want to find the propability at and record a data point for (recommended to start with 5). 
9) Ensure the create "Use Graph" button at the bottom of the window is checked and the "Use Simulation" button is unchecked, then click "Okay". PRISM will run the experiment and you can see the propability of the property being satisfied as a function of the number of transitions (iterations).