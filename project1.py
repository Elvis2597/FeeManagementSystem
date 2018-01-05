from prettytable import PrettyTable

import datetime
class Fee:
   def getfee(self,admn,tran,tutionfee,annFee,recNo):
      self.admn=admn
      self.qt=input('Enter Quarter Number              :')
      self.recNo=recNo
      self.date=datetime.date.today()
      self.time1=datetime.datetime.now()
      self.c=datetime.datetime.strftime(self.time1,'%I:%m:%S')
      if self.qt==1:
         self.mode=raw_input('Enter Mode Of Payment(cash/cheque):')
         self.tof=tran+tutionfee+annFee
         if self.mode=='cash':
            
            self.bank='NA'
            self.chequeno='NA'
         elif self.mode=='cheque':
            self.bank=raw_input('Enter Bank Name                    :')
            self.chequeno=input('Enter Cheque Number               :')
           
      elif self.qt==2 or 3 or 4:
         self.mode=raw_input('Enter Mode Of Payment(cash/cheque):')
         self.tof=tran+tutionfee
         if self.mode=='cash':
            
            self.bank='NA'
            self.chequeno='NA'
         elif self.mode=='cheque':
            self.bank=raw_input('Enter Bank Name                    :')
            self.chequeno=input('Enter Cheque Number               :')
      else:
         print'WRONG QUARTER NUMBER'

       
    
            
      
   def showFee(self):
      x=PrettyTable(['ReceiptNumber','Admission Number','Quarter','Totalfee','Mode','Bank','ChequeNumber','Date','Time'])
      x.add_row([self.recNo,self.admn, self.qt,self.tof,self.mode,self.bank,self.chequeno, self.date.strftime('%d %b %Y'),self.c])
      print x    
      



