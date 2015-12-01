#!/bin/sh
ls > tmp

a = $(cat tmp | wc -l)

for i in 'seq 1 $(a-1)'
do
	b = $(head -n $i tmp | sed 's/\.{'in' 'out'}//g')
	c = $(head -n $(i+1) tmp | sed 's/\.{'in' 'out'}//g')
	d = $(top | grep pw.x | wc -l)

	if  [ $(d) < 24 ] && [ $b != $c ]
		then 
		





	
LP=$(echo "3.36+($i*0.01)"  |bc -l )
inbohr=$(echo "$LP/0.529177249"   |bc -l )

sed '10s/7.18/'$inbohr'/' Ni.scf.in  > temp


mpirun -np 4 pw.x  < temp > Ni.scf.out"$LP" 

grep ! Ni.scf.out"$LP" | sed 's/!    total energy              = /latticeparameter='$LP'/' >>  results

done
