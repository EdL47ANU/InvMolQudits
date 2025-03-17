import numpy as np
from SolutionSpace import DESearch1Bool, BOrientSearch1Bool, DEPlotter1Bool, BOrientSearch1Bool, TiFrqvsMagField, TiFrqvsMagFieldPlot, TiFrqvsOrientation, TiFrqvsOrientationPlot, BOrientationPlotter1Bool, BRotPlotter1Bool
from HamiltonianClass import H0
from SolutionSpaceHyperfine import HyperSearch, PullCorrectHyper, HyperPlotter1Bool, HyperBRotChecker1Bool, BRotPlotter1Bool, RotatingB1Data, BvsOrientationPlotterMultiple
from Consts import SpinOp2, Orientations, FibbonaciSphere, DEcm_ZfsMHZ, SpinOp4, SpinOp3
import pickle
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# git clone this https://github.com/EdL47ANU/SolutionSpace is activley worked on. 


with open('D-0.150.1450.005_B1002455_N200QuditFull.pkl', 'rb') as f:
    DCoords, ECoords, DboolsFrqTot = pickle.load(f)
DEPlotter1Bool(DCoords, ECoords, DboolsFrqTot, Verbose = 1)
exit("Plotted?")

with open('IdealDE0.13_-0.0346_B1002991_N1600.pkl', 'rb') as f:
    B, OrientationVecs, Bools = pickle.load(f)
BRotPlotter1Bool(B, OrientationVecs, Bools, 0.0)
exit("Plotted?")

D = 0.13  # Ideal mol -  
D = 0.0977 # Real Mol 
E = -0.0346 # Ideal Mol
E = 0.0250 # Real Mol
gs = 1.99 # standard small g. 
#This block does Figures 4 and 5. 
B = np.arange(0, 300, 1)
H = H0(D = DEcm_ZfsMHZ(D,E), gs = np.diag([gs, gs, gs]), coil = 0, SpinOp = SpinOp4)
Frqs, TIs, BasisMix = TiFrqvsMagField(H, B, OrientationVec = np.array([0.74888958, 0.05988857, 0.65998315]))
TiFrqvsMagFieldPlot(TIs, Frqs, BasisMix, B)
exit()

#
#RThis Bloc will run a code to find successful field orientations at a selceted D and E value, across a field range (B), sampling the orientation sphere to a value you choose (NOrient). It will save that as a .pickle, then plot it. too.  
D=0.13
E=-0.0346
B = np.arange(50, 400, 1)
NOrient = 3200
Bools, OrientationVecs = BOrientSearch1Bool(B, NOrient, Nangles = 8, D=D, E=E, gs=gs)
try:
    with open('RealDE'+str(D)+'_'+str(E)+'_B'+str(B[0])+str(B[-1])+str(B[2]-B[1])+'_N'+str(NOrient)+'.pkl', 'wb') as f:
        pickle.dump((B, OrientationVecs, Bools), f)
    print("File saved successfully")
except Exception as e:
    print("Error saving file:", e)
BRotPlotter1Bool(B, OrientationVecs, Bools, 0.0)
exit("Well Done!")
