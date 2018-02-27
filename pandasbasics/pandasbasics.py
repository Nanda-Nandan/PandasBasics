import pandas as pd

#find the first and last elements of series

long_series = pd.Series(np.random.randn(1000))
long_series.head()
long_series.tail(3)

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index,
                   columns=['A', 'B', 'C'])
df

wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
              major_axis=pd.date_range('1/1/2000', periods=5),
              minor_axis=['A', 'B', 'C', 'D'])
wp


#loop over all column headers and manipulate
df.columns = [x.lower() for x in df.columns]
df

#get the actual value inside dataframe
df.values

#get the actual value inside panel
wp.values

#if u intialize a column with less data and less index the field corresponing to that index will be Nan
df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                   'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                   'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
df


'''
DataFrames
'''
#DataFrame from dictionary of series or dictionaries,here index is the row
#Dataframe from series
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df

#rows and columns can be accessed using index and columns attribute,since here three column is not there it will return a series of Nan values
pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])

#attributes to access index and columns are below
df.index
df.columns


#Dataframe from dictionary
d = {'one' : [1., 2., 3., 4.],
     'two' : [4., 3., 2., 1.]}
d
#if you wont give index python will automatically index it as 0,1,2,3 instaed of a,b,c,d
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])

#Dataframe from structured array or records
data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])#int 4,float 6 ,string 10 width
data[:] = [(1,2.,'Hello'), (2,3.,"World")]
pd.DataFrame(data)#columns are A,B,C
pd.DataFrame(data, index=['first', 'second'])
pd.DataFrame(data, columns=['C', 'A', 'B'])#makes the position of column as C,A,B

#DataFrame from list of dictionaries
#keys are columns and values are data values,c value is nan fro first row,index is by default 0,1
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)
#modify the columns to less numbers
pd.DataFrame(data2, columns=['a', 'b'])
#multi-indexed frame by passing a tuples dictionary [TO SEE MORE]

#DataFrame from records
pd.DataFrame.from_records(data, index='C')#here index is c column having c,value1,value2 as differents rows

#DataFrame from items
pd.DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6])])#takes tuple as key,value pair and construct dataframe as dictionary
pd.DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6])],orient='index', columns=['one', 'two', 'three'])#orient set the keys as index,however column names explicitly has to be passed

#Column selection,addition,deletion
#deletion
del df['two']
three = df.pop('three')
#addition
df['foo'] = 'bar'#add bar to each row of newly added column foo
df['one_trunc'] = df['one'][:2]#create anew colum taking some range of values of old column
df.insert(1, 'bar', df['one'])#insert at 1st position with column name bar and values same as df['one']

#column in method chain
iris=pd.DataFrame.from_items([('SepalWidth', [1, 2, 3]), ('SepalLength', [4, 5, 6])])
(iris.query('SepalLength > 5')#like where to search
 .assign(SepalRatio = lambda x: x.SepalWidth / x.SepalLength,PetalRatio = lambda x: x.PetalWidth / x.PetalLength)#=> operator
 .plot(kind='scatter', x='SepalRatio', y='PetalRatio'))

#Indexing & Selection
df.loc['b']#row of bth index
df.iloc[2]#2nd row

#we can do all bolean operation on dataframe,it will compute elementwise
df1 = pd.DataFrame({'a' : [1, 0, 1], 'b' : [0, 1, 1] }, dtype=bool)
df2 = pd.DataFrame({'a' : [0, 1, 1], 'b' : [1, 1, 0] }, dtype=bool)
df1 & df2

#DataFrame interoperability with NumPy functions
np.exp(df)
np.asarray(df)#make every row as array excluding index

#matrix mul on dataframe
df.T.dot(df)
s1 = pd.Series(np.arange(5,10))
s1.dot(s1)
#we can access columns using . operator
df.foo1

# Matching / broadcasting behavior  add(), sub(), mul(), div() 
df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
row = df.iloc[1]#2nd row
column = df['two']
df.sub(row, axis='columns')#substract rowwise df and 2nd row,axis column indicates columns fixed,but sustract row wise
df.sub(row, axis=1)#same axis 1 means in horizontal direction
df.sub(column, axis='index')#index says index or rows fixed substract column wise,so substract df-df['two']
df.sub(column, axis=0)#vertical axis


#Multiindex
dfmi = df.copy()
dfmi.index = pd.MultiIndex.from_tuples([(1,'a'),(1,'b'),(1,'c'),(2,'a')],#first index is 1,2 with heading name first,second index is a,b,c,a name second
                                       names=['first','second'])
dfmi.sub(column, axis=0, level='second')#first index divided into two groups in second index(a,b,c) corresponding to first index 1
#and (a) corresponding to first index 2,level=second and axis zero means first group(vertical index) of second level.[to see more]


#fill the nan values to 0 before adding to df2
df.add(df2, fill_value=0)

#Comparisions
df.gt(df2)#check elementwise greater than
df2.ne(df)#!=
df+df == df*2#nans doesnt compare with equal so will return false u can check using np.nan == np.nan,will return false
(df > 0).all()#check all elements of each column satisfy the condition given
(df > 0).any()#check at least any element of each column satisfy the condition,the output will be column wise ex:-one true two true three false
pd.DataFrame(columns=list('ABC')).empty#df.empty to check if dataframe is empty


#series and index divide and remainder
s = pd.Series(np.arange(10))
div, rem = divmod(s, 3)
#similar can be appy to index also



