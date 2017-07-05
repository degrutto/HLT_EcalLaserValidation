#!/bin/bash


echo "Running automated fast track validation script. Will compare rates and timing of menus using"
echo "reference and test sqlite files"
echo " "

echo " edit testMenu, file and sqlites files, etc.... in the first section"
sleep 5
 
###############################
testMenu=/cdaq/physics/Run2017/2e34/v1.1.5/HLT/V1
#runNumber=295606
GT=92X_dataRun2_HLT_v3
file=/store/data/Run2017B/SingleElectron/RAW/v1/000/297/227/00000/CC1B0F41-6556-E711-B091-02163E01457C.root 
sqlite1=DBLaser_293491
sqlite2=DBLaser_292925
#pathToMonitor=("HLT_Ele35_WPTight_Gsf" "HLT_PFMET110_PFMHT110_IDTight"  "HLT_Photon33"  "HLT_PFJet450" 
pathToMonitor="HLT_Ele35_WPTight_Gsf"
username=degrutto
###############################

#xrdcp root://cms-xrd-global.cern.ch/$file /tmp/$username.root

export CMSREL=CMSSW_9_2_3_patch2
export SCRAM_ARCH=slc6_amd64_gcc630
cmsrel $CMSREL
cp fastTimeAdd_new.py  $CMSREL/src/
cd $CMSREL/src
cmsenv


echo "will run : hltGetConfiguration --offline --globaltag " $GT   "--max-events 999999 --timing  --input  "$file "orcoff:"$testMenu 

#files=/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/121C5D66-3545-E711-88AA-02163E01A23B.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/7C8C77B9-4745-E711-A031-02163E014732.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/B27D2641-3545-E711-BF05-02163E013832.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/12694E0C-4745-E711-BFA8-02163E01A3E4.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/86E16272-3545-E711-AE8C-02163E0144DD.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/B63616F2-3645-E711-9A44-02163E019CF6.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/209ACC3D-3545-E711-8842-02163E011CC4.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/924D284E-3545-E711-96EB-02163E019E11.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/D89F4B60-3545-E711-A0EA-02163E01426A.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/268CA04C-3745-E711-A679-02163E0144C8.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/A090DDA5-4045-E711-BCE9-02163E011E5B.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/DAAB3C4D-3545-E711-BA41-02163E019BD0.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/3039143D-3545-E711-8334-02163E01A656.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/AE072134-3545-E711-93BD-02163E0118C9.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/F20FC453-3545-E711-9F4B-02163E0141C9.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/5CBF6E3A-3545-E711-B611-02163E011F15.root,/store/data/Run2017A/HLTPhysics/RAW/v1/000/295/606/00000/AE610938-3545-E711-9CD0-02163E014474.root


#hltGetConfiguration --offline --globaltag "auto:hltonline"   --max-events 999999  --input  'file:/tmp/'$username'.root'  orcoff:$testMenu > hlt.py

hltGetConfiguration --online --globaltag $GT   --max-events -1  --input $file orcoff:$testMenu > hlt.py
more fastTimeAdd_new.py >> hlt.py

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
