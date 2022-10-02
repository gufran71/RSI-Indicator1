#Rsi indicator takes last 14 period data from data-frame (df) 
import pandas as pd

def Rsi_indicator(df):
    r_df = df
    ind = range(0,len(r_df))
    print(ind)
    indexlist = list(ind)
    df.index = indexlist

    gain1=[]
    loss1=[]
    
    for index, row in r_df.iterrows():
        if index !=0:
            change =  row['Close']-df.iloc[index-1]["Close"]
            if change> 0:
                gain1.append(change)
                loss1.append(0)
            else:
                change=abs(change)
                loss1.append(change)
                gain1.append(0)
        else:
            a=0
            gain1.append(a)
            loss1.append(a)        
    r_df['Gain'] = gain1   
    r_df['Loss'] = loss1   
      
    print(r_df)   
    
        
    # calculate avg.gain
    sum_gain1=0;
    sum_loss1=0;
    if range(0,22) == ind:
      for i in range(8,22): #22 rows in dataframe
         cg = gain1[i]
         sum_gain1 += cg; 
           
         #losss
         cl = loss1[i]
         sum_loss1 +=  + cl;       
    else:
        for i in range(9,23): #23 rows in dataframe
         cg = gain1[i]
         sum_gain1 += cg; 
          
         #losss
         cl = loss1[i]
         sum_loss1 +=  + cl;
         
    
    avg_gain1= sum_gain1/14;
    
    #calculate avg.loss
    avg_loss1 = sum_loss1/14  
      
    rs1 = avg_gain1/avg_loss1
    rsi1= round(100-(100/(1+rs1)))
    print('rsi_1=',rsi1)
    return rsi1
  