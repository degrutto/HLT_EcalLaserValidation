#!/bin/bash


echo "Running automated fast track validation script. Will compare rates and timing of menus using"
echo "reference and test sqlite files"
echo " "

echo " edit testMenu, file and sqlites files, etc.... in the first section"
sleep 5
 
###############################
testMenu=/cdaq/cosmic/commissioning2017/CRAFT/v1.0/HLT/V1
runNumber=293492
GT=90X_dataRun2_HLT_v2
file=/store/data/Commissioning2017/Cosmics/RAW/v1/000/293/492/00000/0E623A39-9B33-E711-B263-02163E019C0D.root
sqlite1=DBLaser_293491
sqlite2=DBLaser_292925
pathToMonitor="HLT_L1SingleEG5_v1"
username=degrutto
###############################

xrdcp root://cms-xrd-global.cern.ch/$file /tmp/$username.root


export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSSW_9_0_2_patch1
cp fastTimeAdd.py  CMSSW_9_0_2_patch1/src/
cd CMSSW_9_0_2_patch1/src
cmsenv


echo "wille run : hltGetConfiguration --offline --globaltag " $GT   "--max-events 999999 --timing  --input  "$file "orcoff:"$testMenu 

hltGetConfiguration --offline --globaltag $GT   --max-events 999999 --timing  --input  'file:/tmp/'$username'.root'  orcoff:$testMenu > hlt.py
more fastTimeAdd.py >> hlt.py

sed 's/TOADAPT/'$sqlite1'/g' hlt.py  > hlt_sqlite1.py
sed 's/TOADAPT/'$sqlite2'/g' hlt.py  > hlt_sqlite2.py




cmsRun hlt_sqlite1.py >&log_sqlite1.log 
cmsRun hlt_sqlite2.py >&log_sqlite2.log 

more log_sqlite1.log | grep $pathToMonitor >  $pathToMonitor\_sqlite1.log 
more log_sqlite2.log | grep $pathToMonitor >  $pathToMonitor\_sqlite2.log 

awk 'NR==1 {print "pass ",$5," over ",$6," for reference path using  sqlite1"} ' $pathToMonitor\_sqlite1.log > diff.txt
awk 'NR==1 {print "pass ",$5," over ",$6," for reference path using  sqlite2"} ' $pathToMonitor\_sqlite2.log >> diff.txt


awk 'NR==3 {print "timing " $2," for reference path using sqlite1"} ' $pathToMonitor\_sqlite1.log >> diff.txt
awk 'NR==3 {print "timing " $2," for reference path using sqlite2"} ' $pathToMonitor\_sqlite2.log >> diff.txt


echo " difference in counts and timing using the two sqlite files is "
more diff.txt

#wget https://raw.githubusercontent.com/cms-steam/TimingScripts/master/MenuValidation/TimingAndRates.py 
#wget https://raw.githubusercontent.com/cms-steam/TimingScripts/master/MenuValidation/TimingAndRates.cc .
#python TimingScripts/Scripts/plotPath_Timing.py --inputfiles DQM_XXXX.root --process TIMING --runs XXX --paths HLT_XXXXX


#python TimingAndRates.py --run 293492 --data --lumis 999999 --inputfile DQM_V0001_R000293645__HLT__FastTimerService__All.root
