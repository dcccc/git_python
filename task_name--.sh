#!/bin/sh
echo "---------------------------------------------------------------"
echo "       Task in running"

echo "---------------------------------------------------------------"

pidof pw.x | sed 's/ /\n/g' | sort > tmp2

a=$(cat tmp2 | wc -l)

for i in `seq 1 4 $a`
do
b=$(awk 'NR == '$i'' tmp2)
c=$(lsof -p $b | grep /home/ | tail -n 1| cut -d / -f 4 | sed 's/igk/in/g')
d=$(lsof -p $b | tail -n 1 |tr -s " "| cut -d " " -f 3)
echo ${d}" "${c}"    pid "${b}" "$(echo "1+($b)"  |bc -l )" "$(echo "2+($b)"  |bc -l )" "$(echo "3+($b)"  |bc -l ) >> tmp1
done

#cut -d / -f 4 tmp1 | sed 's/igk/in/g' 
cat tmp1

echo "---------------------------------------------------------------"

echo "core in using     $a"

echo "---------------------------------------------------------------"
rm tmp2 tmp1


