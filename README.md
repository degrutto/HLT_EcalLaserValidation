# HLT_EcalLaserValidation
short script ecal laser calibrations fast validation at HLT

1. to be used in bash

2.  edit the first section of step.sh 

testMenu=/cdaq/cosmic/commissioning2017/CRAFT/v1.0/HLT/V1
runNumber=293492
GT=90X_dataRun2_HLT_v2
file=/store/data/Commissioning2017/Cosmics/RAW/v1/000/293/492/00000/0E623A39-9B33-E711-B263-02163E019C0D.root
sqlite1=DBLaser_293491
sqlite2=DBLaser_292925
pathToMonitor="HLT_L1SingleEG5_v1"
username=degrutto

3. also change the CMSSW relase below if needed


4. then source step.sh


in a test I did I got this finally

difference in counts and timing using the two sqlite files is 
pass  1  over  4999  for reference path using  sqlite1
pass  1  over  4999  for reference path using  sqlite2
timing 0.030172  for reference path using sqlite1
timing 0.027120  for reference path using sqlite2
