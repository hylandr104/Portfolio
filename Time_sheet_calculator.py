# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:33:52 2020

@author: rockg
"""

'''
Need to calculate:
    Hours worked at each rate
    Amount for each rate
    Total amount to be invoiced
'''

import pandas as pd
from decimal import *

normal_rate = 550
higher_rate = 650
start_higher = 22
end_higher = 6
lb = 0.5            # Lunch Break

def nh(list1,list2,a,b,c='No',d='No'):
    hr = b - a
    if c == d or str(c) == 'nan':
        hr = hr - lb
    list1.append(hr)
    
    p = hr * normal_rate
    list2.append(p)
    
def hh(list1,list2,start = end_higher,end = start_higher):
    hr = (end_higher - start) + (end - start_higher)
    list1.append(hr)
    
    p = hr * higher_rate
    list2.append(p)

def night(list1,list2,a,b,c='No',d='No'):
    hr = b + 24 - a
    if c == d or str(c) == 'nan':
        hr = hr - lb
    list1.append(hr)
    
    p = hr * higher_rate
    list2.append(p)
    
def night_cheaper(list1,list2,start = start_higher, end = end_higher,):
    hr = (start_higher - start) + (end - end_higher)
    list1.append(hr)
    
    p = hr * normal_rate
    list2.append(p)
    
def weekend_days(list1,list2,a,b,c='No',d='No'):
    hr = b - a
    if c == d or str(c) == 'nan':
        hr = hr - lb
    list1.append(hr)
    
    p = hr * higher_rate
    list2.append(p)
    
def appendmultiple(list,x=0):
    for a in list:
        a.append(x)

def main(name):
    
    df = pd.read_csv(name)
    
    n_hours = []
    h_hours = []
    p_normal = []
    p_higher = []    
    
    for i in range(df.shape[0] - 1):                        
        idx1,idx2=i,i+1                         
        row1,row2=df.iloc[idx1],df.iloc[idx2]           #for iterating over 2 rows at once for nights
        if row1['Day'] == 'Fri':
            if row1['Nights'] == 'Yes':
                if row1['Start']>=start_higher:
                    night(h_hours,p_higher,row1['Start'],row2['End'],row1['Paid Lunch?'])
                    appendmultiple([n_hours,p_normal])
                else:
                    night(start_higher,row2['End'],row1['Paid Lunch?'])
                    night_cheaper(n_hours,p_normal,start = row1['Start'])
                    
            else:
                if row1['Start']>=end_higher and row1['End']<=start_higher:
                    nh(n_hours,p_normal,row1['Start'],row1['End'],row1['Paid Lunch?'])
                    appendmultiple([h_hours, p_higher])
                    
                elif row1['Start']<end_higher and row1['End']<=start_higher:
                    nh(n_hours,p_normal,end_higher,row1['End'],row1['Paid Lunch?'])
                    hh(h_hours,p_higher,start = row1['Start'])
                                
                elif row1['Start']>=end_higher and row1['End']>start_higher:
                    nh(n_hours,p_normal,row1['Start'],start_higher,row1['Paid Lunch?'])
                    hh(h_hours,p_higher,end = row1['End'])        
                
                else:                           
                    appendmultiple([n_hours,p_normal,h_hours,p_higher])
                    
        elif row1['Day'] == 'Sat':
            if row1['Nights'] == 'Yes':
                night(h_hours,p_higher,row1['Start'],row2['End'],row1['Paid Lunch?'])
                appendmultiple([n_hours,p_normal])
            else:
                if str(row1['Start']) == 'nan':
                    appendmultiple([n_hours,p_normal,h_hours,p_higher])
                else:
                    weekend_days(h_hours,p_higher,row1['Start'],row1['End'],row1['Paid Lunch?'])
                    appendmultiple([n_hours,p_normal])
                   
        elif row1['Day'] == 'Sun':
            if row1['Nights'] == 'Yes':
                if row2['End']<=end_higher:
                    night(h_hours,p_higher,row1['Start'],row2['End'],row1['Paid Lunch?'])
                    appendmultiple([n_hours,p_normal])
                else:
                    night(h_hours,p_higher,row1['Start'],end_higher,row1['Paid Lunch?'])
                    night_cheaper(n_hours,p_normal,end = row2['End'])
            else:
                if str(row1['Start']) == 'nan':
                    appendmultiple([n_hours,p_normal,h_hours,p_higher])
                else:
                    weekend_days(h_hours,p_higher,row1['Start'],row1['End'],row1['Paid Lunch?'])
                    appendmultiple([n_hours,p_normal])
        else:
            if row1['Nights'] == 'Yes':
                if row1['Start']>=start_higher and row2['End']<=end_higher:
                    night(h_hours,p_higher,row1['Start'],row2['End'],row1['Paid Lunch?'])
                    appendmultiple([n_hours,p_normal])
                    
                elif row1['Start']>=start_higher and row2['End']>end_higher:
                    night(h_hours,p_higher,row1['Start'],end_higher,row1['Paid Lunch?'])
                    night_cheaper(n_hours,p_normal,end = row2['End'])
                    
                elif row1['Start']<start_higher and row2['End']<=end_higher:
                    night(start_higher,row2['End'],row1['Paid Lunch?'])
                    night_cheaper(n_hours,p_normal,start = row1['Start'])
                    
                else:
                    night(h_hours,p_higher,start_higher,end_higher,row1['Paid Lunch?'])
                    night_cheaper(n_hours,p_normal,row1['Start'],row2['End'])
                    
            else:
                if row1['Start']>=end_higher and row1['End']<=start_higher:
                    nh(n_hours,p_normal,row1['Start'],row1['End'],row1['Paid Lunch?'])
                    appendmultiple([h_hours, p_higher])
                    
                elif row1['Start']<end_higher and row1['End']<=start_higher:
                    nh(n_hours,p_normal,end_higher,row1['End'],row1['Paid Lunch?'])
                    hh(h_hours,p_higher,start = row1['Start'])
                                
                elif row1['Start']>=end_higher and row1['End']>start_higher:
                    nh(n_hours,p_normal,row1['Start'],start_higher,row1['Paid Lunch?'])
                    hh(h_hours,p_higher,end = row1['End'])        
                
                else:                           
                    appendmultiple([n_hours,p_normal,h_hours,p_higher])
    
    df1 = pd.DataFrame({'Hours NR':n_hours,
                        'Invoice NR':p_normal,
                        'Hours HR':h_hours,
                        'Invoice HR':p_higher})

    joined = df.join(df1)
    joined.set_index('Day',inplace=True)
    #print(joined)
    
    joined.to_csv(name)
    
    total_hours_n,total_hours_h,total_pay_n,total_pay_h = sum(n_hours),sum(h_hours),sum(p_normal),sum(p_higher)
    total_pay = total_pay_n + total_pay_h

    sf = open(name,'a')
    
    sf.write('\nTotal hours at normal rate = ' + str(round(total_hours_n,2)) +
             '\nTotal hours at higher rate = ' + str(round(total_hours_h,2)) +
             '\nAmount to invoice at normal rate = ' + str(round(total_pay_n,2)) + 
             '\nAmount to invoice at higher rate = ' + str(round(total_pay_h,2)) +
             '\nTotal to invoice = ' + str(round(total_pay,2)))
    
    sf.close()
