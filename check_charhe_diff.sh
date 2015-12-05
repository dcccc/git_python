#!/bin/sh
a=$1
b=$2
c=$3

/home/flw/work/charge_den/check2xsf -c --cube $1 ${a%.*}.cube
/home/flw/work/charge_den/check2xsf -c --cube $2 ${b%.*}.cube
/home/flw/work/charge_den/check2xsf -c --cube $3 ${c%.*}.cube

python    /home/flw/work/charge_den/cube_charhe_diff.py       ${a%.*}.cube   ${b%.*}.cube  ${c%.*}.cube


rm     ${a%.*}.cube    ${b%.*}.cube      ${c%.*}.cube