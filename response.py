#Coded By Ahmet YILDIRIM
#www.mclightning.com
#mclightning34@hotmail.com
#Code license:GNU General Public License v3

import time
import serial, SendKeys
a=serial.Serial(4,9600)
yeni=0;
tuslar={76:'{SPACE}',24:'{UP}',28:'{DOWN}',72:'{LEFT}',
        52:'{RIGHT}',20:'{ENTER}',16:'%{F4}',32:'f',34:'^{UP}',66:'^{DOWN}'}
def uygulayici(tus):
    SendKeys.SendKeys(tus)
    print "Uygulandi :"+str(tus)
while 1:
    s=a.readline()
    if int(s)!=0:
        try:
            yeni=int(s)-109562800
            uygulayici(tuslar[yeni])
        except:
            print "Tanimlanmamis kod : "+s
    time.sleep(0.5)
