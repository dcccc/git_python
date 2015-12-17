#!/bin/sh
a=$1

python /home/flw/work/script/cif2poscar.py  $a PCo.cif
mv *.POSCAR POSCAR

aa=$(awk 'NR==6' POSCAR | tr -s " ")
len=$(awk 'NR==6' POSCAR | tr -s " " | sed 's/ /\n/g' | wc -l) 
len=$(echo "($len)-1"  |bc -l )

for i in $aa
do 
    cc=$(echo "/home/flw/work/psudopotential/paw_pbe/"${i}"/POTCAR.Z" )
    dd=$(echo  "/home/flw/work/psudopotential/paw_pbe/"${i}"/POTCAR" )
    if [ -a  $cc ] ; then 
            zcat $cc >> POTCAR
    elif [ -a $dd ] ; then
           cat $dd >> POTCAR
fi
done

if [ -n  $2 ] ; then
mpirun -np $2 /home/flw/work/vasp/vasp.5.2/vasp > out &
else 
mpirun -np 4 /home/flw/work/vasp/vasp.5.2/vasp > out &
fi
