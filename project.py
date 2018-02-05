from prettytable import PrettyTable
import time,datetime
import pickle
import os
from Tkinter import*
import time
class student:
   def Input(self):
      self.name=raw_input('Enter the name                     :')
      self.admn=input('Enter the admission number         :')
      self.fname=raw_input('Enter Fathers Name                 :')
      self.Class=raw_input('Enter the class                    :')
      self.section=raw_input('Enter Class Section                :')
      self.rollno=input('Enter RollNumber of the Student    :')
      self.address=raw_input('Enter Address of the Student       :')
      self.phone=input('Enter Phone number                 :')
      self.calfee()
      self.transport=raw_input('Enter mode of transport(bus/onfoot):')
      self.trans()
      
   def calfee(self):
      if self.Class=='LKG' and self.Class=='UKG':
         self.tutionfee=2000
         self.annual=30000
      if self.Class in '1234':
         self.tutionfee=3000
         self.annual=30000
      if self.Class in '5678':
         self.tutionfee=3200
         self.annual=30000
      if self.Class=='9' or self.Class=='10':
         self.tutionfee=3500
         self.annual=30000
      if self.Class=='11' or self.Class=='12':
         self.tutionfee=4000
         self.annual=30000
   def trans(self):
      if self.transport=='bus':
         self.routeno=input('Enter route Number                 :')
         self.tran=input('Enter Bus fee                      :')
         return self.tran
      if self.transport=='onfoot':
         self.tran=0
   def show(self):
      x=PrettyTable(['Name', 'Admn', 'Class', 'Fname', 'Section',  'RollNo', 'Address', 'transport', 'Phone', 'Tution', 'Transport'])
      x.add_row([self.name,self.admn,self.Class,self.fname,self.section,self.rollno,self.address,self.transport,self.phone,self.tutionfee,self.tran])
      print x
      return ''
      

   def __str__(self):
      x=PrettyTable(['Admission number.', 'Name', 'Class','Section'])
      x.add_row([self.admn,self.name,self.Class,self.section])
      print x
      return ''

def createstudent():
   for i in '\t\t\tCreate Student Data\n':
      print i,
      time.sleep(0.2)
   
   n=input("Enter no. of students              :")
   f1=open('student.txt','ab')
   for i in range(n):
      print
      print'\t\tFor Student',i+1
      s=student()
      s.Input()
      pickle.dump(s,f1)
   f1.close()
   print'____________________________________________________________________________________________________________________'

def display():
   for i in '\t\t\tDisplay Student Data\n':           
      print i,
      time.sleep(0.2 )
   f1=open('student.txt','rb')
   x=PrettyTable(['Name', 'Admn', 'Class', 'Fname', 'Section',  'RollNo', 'Address', 'transport', 'Phone', 'Tution', 'Transport'])
   
   while 1:
      try:
         obj=pickle.load(f1)
         x.add_row([obj.name,obj.admn,obj.Class,obj.fname,obj.section,obj.rollno,obj.address,obj.transport,obj.phone,obj.tutionfee,obj.tran])
      except EOFError:
         break
   print x
   print'________________________________________________________________________________________________________________________________________________'
    
def search():
##   for i in '\t\t\tSearch Student Data\n':
##         
##      print i,
##      time.sleep(0.2 )                                
   f=open('student.txt','rb')
   adm=input('Enter Admission number to search  :')
   while 1:
      try:
         obj=pickle.load(f)
         if adm==obj.admn:
            f.close()
            return obj
            
            
      except EOFError:
         break
   f.close()
   print'____________________________________________________________________________________________________________'
   
def delete():
   for i in '\t\t\tDelete Student Data\n':
      print i,
      time.sleep(0.2 )
   f1=open('student.txt','rb')
   f2=open('student1.dat','wb')
   adm=input('Enter Admission number to delete  :')       
   while 1:
      try:
         obj=pickle.load(f1)
         if adm!=obj.admn:
            pickle.dump(obj,f2)
            
      except EOFError:
         break
   f1.close()
   f2.close()
   os.remove('student.txt')
   os.rename('student1.dat','student.txt')
   print'____________________________________________________________________________________________________________'
   
           
def modify():
   for i in '\t\t\tModify Student Data\n':
      print i,
      time.sleep(0.2 )
   f1=open('student.txt','rb')
   f2=open('student1.dat','wb')
   adm=input('Enter Admission number to modify  :')        
   while 1:
      try:
         obj=pickle.load(f1)
         if adm!=obj.admn:
            pickle.dump(obj,f2)
         else:
            ch1='y'

            while ch1=='y':
               
               
                              
               obj.show()
               print'\t\t\t\t1.Name'
               print'\t\t\t\t2.Father\'s Name'
               print'\t\t\t\t3.Class'
               print'\t\t\t\t4.Section'
               print'\t\t\t\t5.Roll Number'
               print'\t\t\t\t6.address'
               print'\t\t\t\t7.phone'
               ch=input('Enter the object to modify      :')
               if ch==1:
                  obj.name=raw_input('Enter the correct name          :')
                  pickle.dump(obj,f2)
               elif ch==2:
                  obj.fname=raw_input('Enter correct father\'s name     :')
                  pickle.dump(obj,f2)
               elif ch==3:
                  obj.Class=raw_input('Enter New Class                :')
                  pickle.dump(obj,f2)
               elif ch==4:
                  obj.section=raw_input('Enter New Section               :')
                  pickle.dump(obj,f2)
               elif ch==5:
                  obj.rollno=input('Enter New Roll Number           :')
                  pickle.dump(obj,f2)
               elif ch==6:
                  obj.address=raw_input('Enter Corrected address         :')
                  pickle.dump(obj,f2)
               elif ch==7:
                  obj.phone=input('Enter correct Phone Number      :')
                  pickle.dump(obj,f2)
               ch1=raw_input('Do you Want To modify more(y/n) :')
               print'_________________________________________________________________________________________________________________________________'
   

      except EOFError:
         break
   f1.close()
   f2.close()
   os.remove('student.txt')
   os.rename('student1.dat','student.txt')
   print'____________________________________________________________________________________________________________________________________________________'
##def append():
##   for i in '\t\t\tAppend Student Data\n':
##      print i,
##      time.sleep(0.2 )
##   f1=open('student.txt','ab')
##   obj=student()
##   obj.Input()                                            
##   pickle.dump(obj,f1)
##   while 1:
##      try:
##         print obj
##         break
##      except EOFError:
##         break
##   f1.close()

from project1 import *
def receipt():
   f2=open('fee.txt','rb')
   while 1:
      try:
          obj=pickle.load(f2)
          

      except EOFError:
         break
   return obj.recNo+1
   f2.close()


def FeeManager():
   print'\t\t\t\tPay Student Fee'
   f2=open('fee.txt','ab')
   f3=open('fee1.txt','ab')
   f4=open('fee2.txt','ab')
   f5=open('fee3.txt','ab')
   
   x=search()
   
      
   Fobj=Fee()

   RNO=receipt()
      
   Fobj.getfee(x.admn,x.tran,x.tutionfee,x.annual,RNO)
   Fobj.showFee()
   if Fobj.qt==1:
         
      pickle.dump(Fobj,f2)
      f2.close()
   

   elif Fobj.qt==2:
      pickle.dump(Fobj,f3)
      f3.close()
   elif Fobj.qt==3:
      pickle.dump(Fobj,f4)
      f4.close()
   elif Fobj.qt==4:
      pickle.dump(Fobj,f5)
      f5.close()

def DefaulterMenu():
   print'\t\t\tDefaulter\'s List '
   print'\t\t\t*********************************'
   print'\t\t\t*\t1. Quater Number 1      *'
   print'\t\t\t*\t2. Quater Number 2      *'
   print'\t\t\t*\t3. Quater Number 3      *'
   print'\t\t\t*\t4. Quater Number 4      *'
   print'\t\t\t*********************************'
   ch=input("Enter your choice                :")
   if ch==1:
      defaulter("fee.txt")
   elif ch==2:
      defaulter('fee1.txt')
   elif ch==3:
      defaulter('fee2.txt')
   elif ch==4:
      defaulter('fee3.txt')
   else:
      print'Wrong Quarter Number'
      
   
def defaulter(Qtrfilename):
  
   f1= open('student.txt','rb')

   while 1:
      try:
         fobj2=pickle.load(f1)
         SearchD(fobj2,Qtrfilename)         
      except EOFError:
         break
   f1.close()

def SearchD(obj,Qtrfilename):
   f1=open(Qtrfilename)
   flag=0
   while 1:
      try:
         fobj=pickle.load(f1)

         if fobj.admn==obj.admn:
            flag=1
      except EOFError:
         break
   if flag==0:
      print obj
   f1.close()
def viewmenu():
   print'\t\t\tFee Payment Record'
   ch=input("Enter the Quarter Number          :")
   if ch==1:
      view("fee.txt")
   elif ch==2:
      view('fee1.txt')
   elif ch==3:
      view('fee2.txt')
   elif ch==4:
      view('fee3.txt')
   else:
      print'Wrong Quarter Number'
def view(qtrfile):
   f1=open(qtrfile)
   admn=input('Enter Admission number            :')
   while 1:
      try:
         obj=pickle.load(f1)
         if admn==obj.admn:
            obj.showFee()
            break
   
     
      except EOFError:
         print'Fee Not Paid '
          
         break

         
   f1.close()
def Exit():
   exit()
   
   
         
print'************************************************************************************************************'
print'                                    @@@@@@@ @@@@@@@ @@@@@@@                                                 ' 
print'                                    @@      @@      @@                                                      '                                     
print'                                    @@@@@@  @@@@@@  @@@@@@                                                  '
print'                                    @@      @@      @@                                                      '                
print'                                    @@      @@@@@@@ @@@@@@@                                                 '
print'                                                                                                            '
print'   @@@@  @@@@  @@@@@  @@     @@  @@@@@   @@@@@   @@@@@@ @@@@  @@@@ @@@@@@ @@     @@ @@@@@@                  '
print'   @@  @@  @@ @@   @@ @@@@   @@ @@   @@ @@       @@     @@  @@  @@ @@     @@@@   @@   @@                    '
print'   @@      @@ @@@@@@@ @@  @@ @@ @@@@@@@ @   @@@@ @@@@@  @@      @@ @@@@@  @@  @@ @@   @@                    '
print'   @@      @@ @@   @@ @@    @@@ @@   @@ @@    @@ @@     @@      @@ @@     @@    @@@   @@                    '
print'   @@      @@ @@   @@ @@     @@ @@   @@  @@@@@@  @@@@@@ @@      @@ @@@@@@ @@     @@   @@                    '         
print'************************************************************************************************************' 
   

root=Tk()
root.title('Main Menu')
root.geometry('200x450')
app=Frame(root)
app.grid()
label=Label(app,text='Fee Management')
label.grid(padx=10,pady=10)
label.config(width=30)
button=Button(app,text='Create',command=createstudent)
button.grid(padx=30,pady=10)
button.config(width=15)
button1=Button(app,text='Display',command=display)
button1.grid(padx=30,pady=10)
button1.config(width=15)
button2=Button(app,text='Search',command=search)
button2.grid(padx=30,pady=10)
button2.config(width=15)
button3=Button(app,text='Modify',command=modify)
button3.grid(padx=30,pady=10)
button3.config(width=15)
button4=Button(app,text='Delete',command=delete)
button4.grid(padx=30,pady=10)
button4.config(width=15)
button5=Button(app,text='Pay Fee',command=FeeManager)
button5.grid(padx=30,pady=10)
button5.config(width=15)
button6=Button(app,text='Fee Defaulter',command=DefaulterMenu)
button6.grid(padx=30,pady=10)
button6.config(width=15)
button7=Button(app,text='Fee Details',command=viewmenu)
button7.grid(padx=30,pady=10)
button7.config(width=15)
button8=Button(app,text='Exit',command=Exit)
button8.grid(padx=30,pady=10)
button8.config(width=15)
mainloop()
   





