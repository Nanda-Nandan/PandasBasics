import pandas as pd
#idioms
df = pd.DataFrame(
     {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
df
#if-then...
df.loc[df.AAA >= 5,'BBB'] = -1#if df.AAA >= 5 then assign BBB as -1,for each element
#if-then with assignment to 2 columns
df.loc[df.AAA >= 5,['BBB','CCC']] = 555
df_mask = pd.DataFrame({'AAA' : [True] * 4, 'BBB' : [False] * 4,'CCC' : [True,False] * 2})#boolean masking,crates  column aaa with 4 true values,bbb 4 false values,ccc 2 true,2 false
df.where(df_mask,-1000)#keeps elements of df with -1000 when df_mask true and keeps other elements of df as df_mask false
#if-then-else using numpy’s where()
df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}); df
df['logic'] = np.where(df['AAA'] > 5,'high','low'); df#if elements of aaa > 5 then high else low,4 output for 4 values

