# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions


source /opt/intel/composer_xe_2015.1.133/bin/ifortvars.sh ia32
source /opt/intel/composer_xe_2015.1.133/bin/ifortvars.sh intel64
source /opt/intel/composer_xe_2015.1.133/bin/iccvars.sh  ia32
source /opt/intel/composer_xe_2015.1.133/bin/iccvars.sh  intel64

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/openmpi-1.5/lib:

export PATH=/opt/openmpi-1.5/bin:$PATH

export PATH=/home/tools/espresso-5.0.1/bin:$PATH


export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/accelrys/MaterialsStudio7.0/lib

export PATH=/home/cyt/Accelrys/MaterialsStudio7.0/etc/DMol3/bin:$PATH

export PATH=/home/cyt/Accelrys/MaterialsStudio7.0/etc/CASTEP/bin:$PATH

export PATH=/home/cyt/Accelrys/MaterialsStudio7.0/etc/QMERA/bin:$PATH

export PATH=/usr/local/MATLAB/R2014a/bin:$PATH

alias tl="top -b -n 1 | grep pw.x |wc -l"

alias t10="tail -n 10"

alias pw4="mpirun -np 4 pw.x"

alias gp="grep ! "

alias   topl="/home/flw/work/task_name.sh"


alias   topm="/home/flw/work/task_name1.sh"
