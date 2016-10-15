#coding=utf-8
import os
import re
import glob
import string
import math
import sys


def cif_to_pw(cif):
	if not os.path.isfile(cif) :
		print cif + " doesn\'t exist"
	else :
		at_po=[]
		cif_file=open(cif,'r')
		txt = cif.replace("cif","pw.in")
		in_file=open(txt,'a')

		for eachline in cif_file:
			b=re.split(r'[\s]+',eachline)
			if len(b) > 6 :
				at_po.append(b[1:5])
			elif b[0]=="_cell_length_a" :
				A=float(b[1])
			elif b[0]=="_cell_length_b" :
				B=float(b[1])	
			elif b[0]=="_cell_length_c" :
				C=float(b[1])
			elif b[0]=="_cell_angle_alpha" :
				a_=float(b[1])
			elif b[0]=="_cell_angle_beta" :
				b_=float(b[1])
			elif b[0]=="_cell_angle_gamma" :
				c_=float(b[1])

		B=float(B) / float(A)
		C=float(C) / float(A)
		A=float(A) / 0.5291772
		a_=math.cos(float(a_)/180*math.pi)
		a_=round(a_,8)
		b_=math.cos(float(b_)/180*math.pi)
		b_=round(b_,8)
		c_=math.cos(float(c_)/180*math.pi)
		c_=round(c_,8)
	

		at_po = sorted(at_po ,key = lambda x : x[3])
		nat= len(at_po)
		ntyp=[]
		for z in xrange(nat):
			ntyp.append(at_po[z][0])
			if z < n :
				at_po[z].append('0   0   0')
			else :
				at_po[z].append('')

		ntyp = set(ntyp)

		start_mag=""
		for i in xrange(len(ntyp)):
			start_mag+="   starting_magnetization(%d) = 0.2,\n" %(i+1)

		at_po_line=map(lambda x : "	".join(x), at_po)
		at_po_line="\n".join(at_po_line)

		at_psudo=[]
		for at in ntyp:
			at_psudo.append(psudo_dict[at])
		at_psudo="\n".join(at_psudo)


		pw_input='''\
 &CONTROL
                 calculation = 'relax' ,
                restart_mode = 'from_scratch' ,
                      outdir = '/HOME/whu_slchen_1/WORKSPACE/pwscf/tmp/' ,
                  pseudo_dir = '/HOME/whu_slchen_1/WORKSPACE/pwscf/pseudo/' ,
                      prefix = '%s' ,
                      nstep  = 600,
 /
 &SYSTEM
                       ibrav = 14,
                   celldm(1) = %f ,
                   celldm(2) = %f ,
                   celldm(3) = %f ,
                   celldm(4) = %f ,
                   celldm(5) = %f ,
                   celldm(6) = %f ,
                         nat = %d,
                        ntyp = %d,
                     ecutwfc = 30,
                     ecutrho = 300,
                 occupations = 'smearing' ,
                     degauss = 0.01,
                    smearing = 'methfessel-paxton' ,
                       nspin = 2,
%s

 /
 &ELECTRONS
            electron_maxstep = 200,
                    conv_thr = 1.D-6,
                 mixing_beta = 0.4,
                 mixing_mode = 'local-TF' ,
 /
 &IONS
                ion_dynamics = 'bfgs' ,
 /
ATOMIC_SPECIES
%s
ATOMIC_POSITIONS crystal
%s
K_POINTS automatic
  5 5 1   0 0 0
'''  %(txt[:-3], A,B,C,a_,b_,c_, nat,len(ntyp), start_mag, at_psudo, at_po_line)

		
		in_file.write(pw_input)



psudo_dict={'Ag':'Ag     107.8682     Ag.pbe-d-rrkjus.UPF',
'Al':'Al     26.9815386     Al.pbe-n-rrkjus_psl.0.1.UPF',
'Ar':'Ar     39.948     Ar.pbe-n-rrkjus_psl.0.3.0.UPF',
'As':'As     74.9216     As.pbe-n-rrkjus_psl.0.2.UPF',
'Au':'Au     196.966569     Au.pbe-nd-rrkjus.UPF',
'B':'B     10.811     B.pbe-n-rrkjus_psl.0.1.UPF',
'Be ':'Be      9.012182     Be.pbe-n-rrkjus_psl.0.2.UPF',
'Bi':'Bi     208.9804     Bi.pbe-dn-rrkjus_psl.0.2.2.UPF',
'Br':'Br     79.904     Br.pbe-n-rrkjus_psl.0.2.UPF',
'C':'C     12.017     C.pbe-rrkjus.UPF',
'Cd ':'Cd      112.411     Cd.pbe-dn-rrkjus_psl.0.3.1.UPF',
'Cl ':'Cl      35.453     Cl.pbe-n-rrkjus_psl.0.3.0.UPF',
'Co':'Co     58.933195     Co.pbe-nd-rrkjus.UPF',
'Cu':'Cu     63.546     Cu.pbe-d-rrkjus.UPF',
'F':'F     18.9984032     F.pbe-n-rrkjus_psl.0.1.UPF',
'Fe':'Fe     55.845     Fe.pbe-nd-rrkjus.UPF',
'Ga':'Ga     69.723     Ga.pbe-dn-rrkjus_psl.0.2.UPF',
'Ge':'Ge     72.64     Ge.pbe-dn-rrkjus_psl.0.3.1.UPF',
'H':'H     1.00794     H.pbe-rrkjus.UPF',
'Hg':'Hg     200.59     Hg.pbe-dn-rrkjus_psl.0.2.2.UPF',
'I ':'I      126.90447     I.pbe-n-rrkjus_psl.0.2.UPF',
'In':'In     114.818     In.pbe-d-rrkjus.UPF',
'Ir':'Ir     192.217     Ir.pbe-n-rrkjus.UPF',
'Li':'Li     6.941     Li.pbe-s-rrkjus_psl.UPF',
'Mo':'Mo     95.94     Mo.pbe-spn-rrkjus_psl.0.3.0.UPF',
'N':'N     14.0067     N.pbe-rrkjus.UPF',
'Na':'Na     22.98976928     Na.pbe-spn-rrkjus_psl.0.2.UPF',
'Nb':'Nb     92.90638     Nb.pbe-spn-rrkjus_psl.0.3.0.UPF',
'Ni':'Ni     58.6934     Ni.pbe-nd-rrkjus.UPF',
'O':'O     15.9994     O.pbe-rrkjus.UPF',
'P':'P     30.973762     P.pbe-n-rrkjus_psl.0.1.UPF',
'Pa':'Pa     231.03588     Pa.pbe-dn-rrkjus_psl.0.2.2.UPF',
'Pb':'Pb     207.2     Pb.pbe-nd-rrkjus.UPF',
'Pd':'Pd     106.42     Pd.pbe-nd-rrkjus.UPF',
'Pt':'Pt     195.084     Pt.pbe-nd-rrkjus.UPF',
'Rh':'Rh     102.9055     Rh.pbe-spn-rrkjus_psl.0.3.0.UPF',
'Ru':'Ru     101.07     Ru.pbe-spn-rrkjus_psl.0.3.0.UPF',
'S':'S     32.065     S.pbe-n-rrkjus_psl.0.1.UPF',
'Sc':'Sc     44.955912     Sc.pbe-spn-rrkjus_psl.0.2.3.UPF',
'Se':'Se     78.96     Se.pbe-n-rrkjus_psl.0.2.UPF',
'Si':'Si     28.0855     Si.pbe-n-rrkjus_psl.0.1.UPF',
'Sn':'Sn     118.71     Sn.pbe-dn-rrkjus_psl.0.2.UPF',
'Sr':'Sr     87.62     Sr.pbe-spn-rrkjus_psl.0.2.3.UPF',
'Ta ':'Ta      180.94788     Ta.pbe-spn-rrkjus_psl.0.2.UPF',
'Te':'Te     127.6     Te.pbe-dn-rrkjus_psl.0.3.1.UPF',
'Tl ':'Tl      204.3833     Tl.pbe-dn-rrkjus_psl.0.2.3.UPF',
'W':'W     183.84     W.pbe-spn-rrkjus_psl.0.2.3.UPF',
'Y':'Y     88.90585     Y.pbe-spn-rrkjus_psl.0.2.3.UPF',
'Zn':'Zn     65.409     Zn.pbe-dn-rrkjus_psl.0.2.2.UPF',
'Zr':'Zr     91.224     Zr.pbe-spn-rrkjus_psl.0.2.3.UPF'}



if len(sys.argv) < 3  :
	print '''
	          Usage
	          python cif_to_pw(piliang)-2.py n   all/cif_file1 cif_file2……
	          n is the number of the nonmovale atom
	          all    --all the xx.cif in current directory will be converted
	          cif_file1 cif_file2……     --the cif_files will be converted
	      '''
	sys.exit()
elif len(sys.argv) == 3 and sys.argv[2] == "all":
	os.chdir(os.getcwd())
	a = glob.glob("*.cif")
elif len(sys.argv) >= 3 and sys.argv[2] != "all":
	a = sys.argv[2:]
else :
	sys.exit()


n = int(sys.argv[1])

if len(a) == 0 :
	print "there is no file to be converted"
	sys.exit()

for i in a:
	cif_to_pw(i)