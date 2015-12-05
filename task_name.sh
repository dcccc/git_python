#!/bin/sh
echo "--------------------------------------"
echo "       Task in running"

echo "--------------------------------------"

pidof pw.x | sed 's/ /\n/g' | sort > tmp2

a=$(cat tmp2 | wc -l)

for i in `seq 1 4 $a`
do
b=$(awk 'NR == '$i'' tmp2)
lsof -p $b | grep /home/ | tail -n 1 >> tmp1
done

cut -d / -f 4 tmp1 | sed 's/igk/in/g'

echo "--------------------------------------"

echo "core in using     $a"

echo "--------------------------------------"
rm tmp2 tmp1


