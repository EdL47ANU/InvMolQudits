# InvMolQudits
InverseDesignOfMolecularQudits

Depoendancies: Numpy, Matplotlib, pickle (for data storage and reading. 

Consts, has a list of Spin matrices. Tools used for checking the validity of the orientation distributions of the magnetic field and generating their orthogonal vectors. A conversion from D&E [cm^-1] calues to ZFS [MHz] matrix.  
HamiltonianClass.py makes the Hamiltonian structure that is used, it takes ZFs paramaetrs, magnetic fields in orientations in mT, the spin vector size 2-4 but easily adapatable to take higher dimensions. Threshoild values for the checking algorith for both the Transition Intensity and Frequency. 
Solution Space.py has functions that iterate over the Hamiltonian, adjusting it methodically over time and checking it against the criteria.
The Run.py is a space to define a hamiltonian and see its Zeeman plot, or other plotting tools, or call functions in solution space to apply the method. By default, i have left the method for finding the solution  space in the paper at the top of the file for convenience.
