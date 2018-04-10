#!/bin/bash -ex
file=`ls ToRun/`
echo $file
if [ -f ToRun/$file ]
then
echo ToRun/$file
    year=`grep "year" ToRun/$file | awk '{print $2}'`
    week=`grep "week" ToRun/$file | awk '{print $2}'`
    sqliteRef=`grep "run1" ToRun/$file | awk '{print $2}'`
    sqliteNew=`grep "run2" ToRun/$file | awk '{print $2}'`
    sqlitePed=`grep "sqlite_pedes" ToRun/$file | awk '{print $2}'`
cp ToRun/$file RunFiles/.
rm ToRun/$file
echo "./runHLTEcalLaserValidation.sh $sqliteRef $sqliteNew $sqlitePed $week"
./runHLTEcalLaserValidation.sh $sqlite1 $sqlite2 $sqlitePed $week 
git commit -a -m "clean ToRun files"
git push
else
echo "No new files"
fi
