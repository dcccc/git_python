#coding:utf-8
import re ,os
import glob
import sys


if len(sys.argv) > 3  :
	"  usage:   python   pw_cord_update.py   pw.in file  pw.out file"
	sys.exit()

def sed_line(in_file,out_file):
	line_num_out = os.popen("sed -n -e '/ATOMIC_POSITIONS/='  "+out_file+ "  | tail -n 1").readlines()
	line_num_out= line_num_out[0]
	line_num_out=int(line_num_out.strip())
	line_num_in=os.popen("sed -n -e '/ATOMIC_POSITIONS/='  "+in_file).readlines()
	line_num_in= line_num_in[0]
	line_num_in=int(line_num_in.strip())
	atom_num=os.popen("grep nat  "+in_file).readlines()
	atom_num=atom_num[0]
	atom_num=int(re.split(r"\s",atom_num.strip())[-1][-3:-1])
	os.popen("sed -n '1,%dp' %s > %s_tmp " %(line_num_in,in_file,in_file ))
	os.popen("sed -n '%d,%dp' %s >> %s_tmp " %(line_num_out+1, line_num_out+atom_num,out_file,in_file ))
	os.popen("sed -n '%d,%dp' %s >> %s_tmp " %(line_num_in+atom_num+1,line_num_in+atom_num+2,in_file,in_file ))
	os.popen("rm %s " %(in_file ))
	os.popen("mv %s_tmp %s " %(in_file ,in_file))


if len(sys.argv)==3:
	sed_line(sys.argv[1],sys.argv[2])
elif sys.argv[1]=="all":
	out=glob.glob("*.out")
	for i in out :
		if os.path.isfile(i[:-4]+".in") :
			sed_line(i[:-4]+".in",i)
		else :
			print i[:-4]+".in" + "   doesn't exist!"


