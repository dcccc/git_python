#!/bin/sh
echo "--------------------------------------"
echo "       Task in running"

echo "--------------------------------------"

pidof pw.x | sed 's/ /\n/g' | sort > tmp3

a=$(cat tmp3 | wc -l)

for i in `seq 1 4 $a`
do
b=$(awk 'NR == '$i'' tmp3)
lsof -p $b | grep /home/ | tail -n 1 >> tmp1
done

cut -d / -f 4 tmp1 | sed 's/igk/in/g'




pidof dmol3.exe | sed 's/ /\n/g' | sort > tmp3

aa=$(cat tmp3 | wc -l)

for i in `seq 1 4 $aa`
do
b=$(awk 'NR == '$i'' tmp3)
lsof -p $b | grep /home/ | head -n 1 >> tmp2
done

cut -d / -f 6 tmp2


echo "--------------------------------------"

echo "core in using     $a + $aa"

echo "--------------------------------------"

rm tmp3 tmp1 tmp2


