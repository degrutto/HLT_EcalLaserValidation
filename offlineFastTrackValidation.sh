#!/bin/bash


echo "Running automated fast track validation script. Will compare rates and timing of menus using"
echo "reference and test GTs"
echo " "

echo " edit testMenu, file and GTs, SCRAM and CMSSW release etc.... in the first section"
sleep 5
 
###############################
testMenu=/cdaq/cosmic/commissioning2017/CRAFT/v1.0/HLT/V1
GT1=92X_dataRun2_HLT_v2
GT2=90X_dataRun2_HLT_v2
file=/store/data/Commissioning2017/ZeroBias1/RAW/v1/000/293/767/00000/2AFEE1FB-6636-E711-A878-02163E0140DD.root 
username=degrutto


xrdcp root://cms-xrd-global.cern.ch/$file /tmp/$username.root


export SCRAM_ARCH=slc7_amd64_gcc630
cmsrel CMSSW_9_2_0
cp fastTimeService.py  CMSSW_9_0_2_patch1/src/
cd CMSSW_9_0_2_patch1/src
cmsenv
###############################

echo "wille run : hltGetConfiguration --offline --globaltag " $GT   "--max-events 999999 --timing  --input  "$file "orcoff:"$testMenu 

hltGetConfiguration --offline --globaltag $GT1   --max-events 999999 --timing  --input  'file:/tmp/'$username'.root'  orcoff:$testMenu > hltGT1.py
more fastTimeService.py >> hltGT1.py

hltGetConfiguration --offline --globaltag $GT2   --max-events 999999 --timing  --input  'file:/tmp/'$username'.root'  orcoff:$testMenu > hltGT2.py
more fastTimeService.py >> hltGT2.py





cmsRun hltGT1.py >&log_GT1.log 
cmsRun hltGT2.py >&log_GT2.log 





echo " difference in counts and timing using the two GTs is "
diff log_GT1.log log_GT2.log

#wget https://raw.githubusercontent.com/cms-steam/TimingScripts/master/MenuValidation/TimingAndRates.py 
#wget https://raw.githubusercontent.com/cms-steam/TimingScripts/master/MenuValidation/TimingAndRates.cc .
#python TimingScripts/Scripts/plotPath_Timing.py --inputfiles DQM_XXXX.root --process TIMING --runs XXX --paths HLT_XXXXX


#python TimingAndRates.py --run 293492 --data --lumis 999999 --inputfile DQM_V0001_R000293645__HLT__FastTimerService__All.root
