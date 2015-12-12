      implicit real*8 (a-h,o-z)
      dimension dump(20),num(2),x(100),y(100),z(100),chg(100,100,800)
      dimension chgt(1000),a(3,3)

      write(*,*) 'Choose input file (LOCPOT=1, CHGCAR=2):'
      read(*,*) input
      if (input.eq.1) then
      open(15,file='LOCPOT')
      write(6,*) ' Enter fermi energy: '
      read(*,*) ef
      elseif (input.eq.2) then
      open(15,file='CHGCAR')
      ef=0.0
      elseif ((input.ne.1).and.(input.ne.2)) then
      write(*,*) ' INPUT ERROR, input must equal to 1 or 2 '
      stop
      endif


      write(*,*) 'Spin polarized calculation? (no=1, yes=2):'
      read (*,*) ispin
      if (ispin.eq.1) then
       if (input.eq.1) open(16,file='workfn.dat')
       if (input.eq.2) open(16,file='chgave.dat')
      elseif (ispin.eq.2) then
       if (input.eq.1) then
       open(16,file='workfn-up.dat')
       open(26,file='workfn-dn.dat')
       elseif (input.eq.2) then
       open(16,file='chgave-up.dat')
       open(26,file='chgave-dn.dat')
       endif
      elseif ((ispin.ne.1).and.(ispin.ne.2)) then
      write(*,*) ' INPUT ERROR, ispin must equal to 1 or 2 '
      stop
      endif


      open(19,file='atom.dat')


      read(15,1) dump
      read(15,*) scale
      do i=1,3
      read(15,*) (a(i,j),j=1,3)
      enddo
1    format(20a4)
      aa=sqrt(a(3,1)**2+a(3,2)**2+a(3,3)**2)
      read(15,2) num(1),num(2)
c     write(6,2) num(1),num(2)
2    format(2i4)
      ity=1
      if (num(2) .gt. 0) ity=2
      natm=0
      do i=1,ity
      natm=natm+num(i)
      enddo
      read(15,1) dump
c     write(6,1) dump
      zero=0.0
      do i=1,natm
      read(15,*) x(i),y(i),z(i)
      enddo
      do i=1,natm
      x(i)=z(i)
      do j=i,natm
      if (z(j) .lt. x(i))  then
      x(i)=z(j)
      z(j)=z(i)
      z(i)=x(i)
      endif
      enddo
c     if (a(3,3) .eq. 0) a(3,3)=a(3,2)
      write(19,30) z(i)*aa*scale,zero
30   format(2f10.5)
      enddo
      nat=natm/2+1
      do i=1,nat
c     write(6,4) i,z(i)
   4  format(i5,f10.5)
      enddo
      read(15,1) dump

      do 600 is = 1,ispin
      read(15,*) nx,ny,nz
c     write(6,*) nx,ny,nz
      nn=nx*ny
      read(15,*) (((chg(j,k,iz),j=1,nx),k=1,ny),iz=1,nz)
c     write(6,5) (((chg(j,k,iz),j=1,nx),k=1,ny),iz=1,nz)
   5  format(5(e18.11,1x))
      do i=1,nz
      chgt(i)=0.0
      do j=1,nx
      do k=1,ny
      chgt(i)=chgt(i)+chg(j,k,i)
      enddo
      enddo
      x1=float(i-1)/float(nz)
      chgt(i)=chgt(i)/float(nn)-ef
      write(6+10*is,10) x1*aa*scale,chgt(i)               
10   format(2f12.5)
       enddo

      if (input.eq.1)then
      emax=-9999.0
      do i=1,nz
      if (chgt(i) .gt. emax) emax=chgt(i)
      enddo
      workfn=emax
c     write(6,201) ef
      write(6,301) workfn
      endif
c201  format(' fermi energy =',f10.5)
301  format(' workfunction =',f10.5)

      if ((is.eq.1).and.(ispin.eq.2))then
       if (input.eq.1) then
       read(15,*) (ttt,i=1,natm)

       elseif (input.eq.2) then
       do nn=1,natm
       read(15,'(24x,2i4)') nn1,nn2
       read(15,*) (ttt,i=1,nn2)
       enddo
       read(15,*) (ttt,i=1,natm)
       endif
      endif
600  continue
      stop  
      end