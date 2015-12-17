# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions



source /opt/intel/composer_xe_2013.2.146/bin/ifortvars.sh ia32
source /opt/intel/composer_xe_2013.2.146/bin/ifortvars.sh intel64
source /opt/intel/composer_xe_2013.2.146/bin/iccvars.sh  ia32
source /opt/intel/composer_xe_2013.2.146/bin/iccvars.sh  intel64

export PATH=/opt/openmpi/bin:$PATH

export LD_LIBRARY_PATH=/opt/openmpi/lib:$LD_LIBRARY_PATH

export PATH=/opt/intel/composer_xe_2013.2.146/bin:$PATH

export PATH=/opt/espresso-5.2.0/bin:$PATH
