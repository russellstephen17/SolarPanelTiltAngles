# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

#H=2.04 #Jan
#H=4.41 #Feb
#H=8.1 #Mar
#H=12.07 #Apr
#H=18.46 #May
#H=16.67 #Jun
#H=14.8 #Jul
#H=12.28 #Aug
#H=8.36 #Sep
#H=5.25 #Oct
#H=2.87 #Nov
H=1.5 #Dec

#n=17 #Jan
#n=47 #feb
#n=75 #Mar
#n=105 #Apr
#n=135 #May
#n=162 #Jun
#n=198 #Jul
#n=228 #Aug
#n=258 #Sep 
#n=288 #Oct
#n=318 #Nov
n=344 #Dec
#H=5.59
lat = 54.172*math.pi/180
#lat = 45.75*math.pi/180
I0 = 1367
p=0.2
maxHT=0
maxBeta=0
for i in range(-100, 900):
    beta = 0.1*i*math.pi/180
    #beta = 68.2*math.pi/180
    
    #delta = (23.45)*math.sin(2*math.pi*(284+n)/36.25)
    #delta = -23.44*math.cos((n+10)*(360/365)*math.pi/180)*math.pi/180
    delta = math.asin(math.sin((n+284)*(360/365)*math.pi/180)*math.sin(23.44*math.pi/180))
    wH= math.acos(-math.tan(lat)*math.tan(delta))
    wI = math.acos(-math.tan(lat-beta)*math.tan(delta))
    R1= 1+0.033*math.cos(2*math.pi*n/365)
    T1 = math.cos(lat)*math.cos(delta)*math.sin(wH)
    T2 = math.sin(lat)*math.sin(delta)
    H0 = (24*3600*I0/math.pi)*R1*(T1+wH*T2)*0.000001
    
   
    Rb = (math.cos(lat-beta)*math.cos(delta)*math.sin(wI) + wI*math.sin(lat-beta)*math.sin(delta))/(math.cos(lat)*math.cos(delta)*math.sin(wH)+wH*math.sin(lat)*math.sin(delta))
    KT = H/H0
    Hd = H*(1-1.13*KT)
    R = (1-Hd/H)*Rb+(Hd/H)*((1+math.cos(beta))/2) + p*((1-math.cos(beta))/2)
    HT = R*H
    #print(i*0.1, HT)
    if (HT>maxHT):
        maxBeta = i*0.1
        maxHT=HT
    #print (i, HT)
print(maxBeta, maxHT, delta*180/math.pi)