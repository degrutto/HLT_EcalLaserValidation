#!/bin/bash -ex
file=`ls RunFiles/`
echo $file
if [ -f ToRun/$file ]
then
echo ToRun/$file
    year=`grep "year" ToRun/$file | awk '{print $2}'`
    week=`grep "week" ToRun/$file | awk '{print $2}'`
    sqliteRef=`grep "run1" ToRun/$file | awk '{print $2}'`
    sqliteNew=`grep "run2" ToRun/$file | awk '{print $2}'`
    label=`grep "type" ToRun/$file | awk '{print $2}'`
cp ToRun/$file RunFiles/.
rm ToRun/$file
echo "./runHLTEcalLaserValidation_2021.sh $sqliteRef $sqliteNew $label $week"
./runHLTEcalLaserValidation_2021.sh $sqliteRef $sqliteNew $label $week $(getconf _NPROCESSORS_ONLN)
#./runHLTEcalLaserValidation_2021.sh $sqliteRef $sqliteNew $label $week 
else
echo "No new files"
fi
