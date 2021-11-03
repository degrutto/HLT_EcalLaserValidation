#!/bin/bash -ex

sleep 5
 
###############################
#testMenu=/cdaq/physics/Run2018/2e34/v2.0.1/HLT/V1
#GT=101X_dataRun2_HLT_v7
#GT=101X_dataRun2_HLT_SiPixelQualityv9_v1
reference=$1
listaFiles=files_Run_323775.txt
sqlite=DBLaser_${2}_moved_to_1
sqlitePED=Pedes_${2}
sqlitePULSE=ecaltemplates_popcon_run_${2}
sqliteTIME=ecaltimingic_popcon_run_${2}
pathToMonitor=("HLT_Ele32_WPTight_Gsf_v" "HLT_Ele35_WPTight_Gsf_v" "HLT_Ele35_WPTight_Gsf_L1EGMT_v" "HLT_Ele38_WPTight_Gsf_v" "HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v" "HLT_Photon33_v" "HLT_PFMET120_PFMHT120_IDTight_v" "HLT_PFMET100_PFMHT100_IDTight_PFHT60_v" "HLT_PFMETTypeOne120_PFMHT120_IDTight_v" )
maxEvents=2000
max_file_num=5
###############################
jobs_in_parallel=$5
if [ "$jobs_in_parallel" = "" ] ; then jobs_in_parallel=1; fi

#export CMSREL=CMSSW_10_1_4
#export SCRAM_ARCH=slc6_amd64_gcc630
#scram -a $SCRAM_ARCH project $CMSREL
export CMSREL=CMSSW_12_0_1
export SCRAM_ARCH=slc7_amd64_gcc900
scram -a $SCRAM_ARCH project $CMSREL

#listaFiles 
cp $listaFiles $CMSREL/src/.
#hlt.py made from recipe: https://twiki.cern.ch/twiki/bin/view/CMS/SteamHLTRatesCalculation
#hltGetConfiguration  /dev/CMSSW_12_0_0/GRun --full --offline --no-output --data --process MYHLT --type GRun --prescale 2.0e34+ZB+HLTPhysics --globaltag auto:run3_hlt_GRun --max-events -1 > hlt.py and changes therin

cp hlt.py $CMSREL/src/.
cp output_ref_${1}_${3}.log $CMSREL/src/. #only for the first time test to be commented
#cp output_sqlite.log $CMSREL/src/. #only for the first time test to be commented
cd $CMSREL/src
eval `scram runtime -sh`


#2018 :echo "will run : hltGetConfiguration --offline --globaltag " $GT   "--max-events 999999 orcoff:"$testMenu 
#2018: hltGetConfiguration --online --globaltag $GT   --max-events $maxEvents  orcoff:$testMenu > hlt.py

        s=0
        for myfile in `less $listaFiles`  

        do
            echo $myfile 
            s=$[$s+1]
            if (( "$s" <= "$max_file_num")) || (("$max_file_num" < 0 ))
            then
		cp hlt.py hlt_${s}.py
		echo "process.source.fileNames = cms.untracked.vstring()" >> hlt_${s}.py
		echo "process.source.fileNames.extend([" >> hlt_${s}.py
		echo $myfile >> hlt_${s}.py
		echo "])" >> hlt_${s}.py

		sed -e "s,%maxevents%,$maxEvents,g" -i hlt_${s}.py
		#cat fastTimeAdd.py >> hlt.py
		echo "process.options = cms.untracked.PSet(
                wantSummary = cms.untracked.bool( True ),
                numberOfThreads = cms.untracked.uint32( $(nproc) ),
                numberOfStreams = cms.untracked.uint32( 0 ),
                sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
                )" >> hlt_${s}.py

		if [ $3 = "laser" ]
		then
		    echo "process.GlobalTag.toGet = cms.VPSet(
                    cms.PSet(record = cms.string(\"EcalLaserAPDPNRatiosRcd\"),
                    tag = cms.string(\"EcalLaserAPDPNRatios_${2}_beginning_at_1\"),
                    connect = cms.string(\"sqlite_file:${sqlite}.db\")
                              )
                    )" >> hlt_${s}.py
		    wget http://cern.ch/ecaltrg/DBLaser/${sqlite}.db
		fi
		if [ $3 = "pedestal" ]
		then
		    echo "process.GlobalTag.toGet = cms.VPSet(
                    cms.PSet(record = cms.string(\"EcalPedestalsRcd\"),
                    tag = cms.string(\"EcalPedestals_hlt\"),
                    connect = cms.string(\"sqlite_file:${sqlitePED}.db\")
                              )
                    )">> hlt_${s}.py
		    wget http://cern.ch/ecaltrg/DBPedestals/${sqlitePED}.db
		fi
		if [ $3 = "pulse" ]
		then
		    echo "process.GlobalTag.toGet = cms.VPSet(
                    cms.PSet(record = cms.string(\"EcalPulseShapesRcd\"),
                    tag = cms.string(\"EcalPulseShapes_${2}_beginning_at_1\"),
                    connect = cms.string(\"sqlite_file:${sqlitePULSE}.db\")
                              )
                    )">> hlt_${s}.py
                    wget https://emanuele.web.cern.ch/emanuele/public/ECAL/jenkins/devel/${sqlitePULSE}.db
		    #echo "process.GlobalTag.toGet = cms.VPSet(
		    #  cms.PSet(record = cms.string(\"EcalTimeCalibConstantsRcd\"),
		    #           tag = cms.string(\"EcalTimeCalibConstants_${2}_beginning_at_1\"),
		    #           connect = cms.string(\"sqlite_file:${sqliteTIME}.db\")
		    #          )
		    #)">> hlt.py
		    #wget https://emanuele.web.cern.ch/emanuele/public/ECAL/jenkins/devel/${sqliteTIME}.db

		fi

		#edmConfigDump hlt.py > hlt_config.py
		#cmsRun hlt_${s}.py >&log_sqlite_${s}.log
		touch outputDiff.log
		for path in ${pathToMonitor[*]}
		do
		    printf "checking for    %s\n" $path
		    cat log_sqlite_${s}.log | grep $path | grep TrigReport | grep -v "\-----" | awk '{if ($5 != 0) print "New normalized rate for path ", $8, $5*100000/$4}' >> output_sqlite_$path.log
		done
	fi	
	done
	for path in ${pathToMonitor[*]}
		do
	       awk -F" " '{sum+=$7}END{print "New normalized rate for path " $6,sum}' output_sqlite_${6}.log >> output_sqlite.log	
	       done

	#wget https://cmssdt.cern.ch/SDT/public/EcalLaserValidation/HLT_EcalLaserValidation/${1}_${3}/output_ref_${1}_${3}.log

touch outputDiff.log
for path in ${pathToMonitor[*]}
do
   printf "checking for    %s\n" $path
   cat output_sqlite.log | grep $path | awk '{if ($7 != 0) print "New normalized rate for path ", $6, $7}' >> outputDiff.log 
   cat output_ref_${1}_${3}.log | grep $path | awk '{if ($7 !=0)  print "Ref normalized rate for path ", $6, $7}' >> outputDiff.log 
done


if [-f ${WORKSPACE}/upload/${2}_${3} ]
then
  echo "dir is already existing"
  touch ${WORKSPACE}/upload/${2}_${3}/.jenkins-upload
else
    mkdir ${WORKSPACE}/upload/${2}_${3}
    touch ${WORKSPACE}/upload/${2}_${3}/.jenkins-upload
fi

#we need to make a tar gz of this one
cp output_sqlite_*.log ${WORKSPACE}/upload/${2}_${3}/.
cp output_sqlite.log  ${WORKSPACE}/upload/${2}_${3}/output_ref_${2}_${3}.log 
cp outputDiff.log ${WORKSPACE}/upload/${2}_${3}/outputDiff.log



