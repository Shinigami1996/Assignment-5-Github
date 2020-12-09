```python
#   Set imports
import pandas as pd
from sqlalchemy import create_engine
import pymysql
```


```python
#   Create engine and connect
engine = create_engine('mysql+pymysql://Streak:12345@1@localhost/new_schema1000')
conn = engine.connect()
```


```python
#   Read SQL into a DataFrame
frame = pd.read_sql("SELECT * FROM vgsales_2016;", conn)

pd.set_option('display.max_columns', 500)
```


```python
frame.head
```




    <bound method NDFrame.head of                                 Name Platform  Year_of_Release         Genre  \
    0                         Wii Sports      Wii             2006        Sports   
    1                  Super Mario Bros.      NES             1985      Platform   
    2                     Mario Kart Wii      Wii             2008        Racing   
    3                  Wii Sports Resort      Wii             2009        Sports   
    4           Pokemon Red/Pokemon Blue       GB             1996  Role-Playing   
    ...                              ...      ...              ...           ...   
    16445  Samurai Warriors: Sanada Maru      PS3             2016        Action   
    16446               LMA Manager 2007     X360             2006        Sports   
    16447        Haitaka no Psychedelica      PSV             2016     Adventure   
    16448               Spirits & Spells      GBA             2003      Platform   
    16449            Winning Post 8 2016      PSV             2016    Simulation   
    
              Publisher  NA_Sales  EU_Sales  JP_Sales  Other_Sales  Global_Sales  \
    0          Nintendo     41.36     28.96      3.77         8.45         82.53   
    1          Nintendo     29.08      3.58      6.81         0.77         40.24   
    2          Nintendo     15.68     12.76      3.79         3.29         35.52   
    3          Nintendo     15.61     10.93      3.28         2.95         32.77   
    4          Nintendo     11.27      8.89     10.22         1.00         31.37   
    ...             ...       ...       ...       ...          ...           ...   
    16445    Tecmo Koei      0.00      0.00      0.01         0.00          0.01   
    16446   Codemasters      0.00      0.01      0.00         0.00          0.01   
    16447  Idea Factory      0.00      0.00      0.01         0.00          0.01   
    16448       Wanadoo      0.01      0.00      0.00         0.00          0.01   
    16449    Tecmo Koei      0.00      0.00      0.01         0.00          0.01   
    
          Critic_Score Critic_Count User_Score User_Count Developer Rating  
    0               76           51          8        322  Nintendo      E  
    1                                                                       
    2               82           73        8.3        709  Nintendo      E  
    3               80           73          8        192  Nintendo      E  
    4                                                                       
    ...            ...          ...        ...        ...       ...    ...  
    16445                                                                   
    16446                                                                   
    16447                                                                   
    16448                                                                   
    16449                                                                   
    
    [16450 rows x 16 columns]>




```python
#creating a new column named 'Post_Pre_2005' with values'Pre-2005' or 'Post-2005'
frame.loc[(frame["Year_of_Release"]<2005),'Post_Pre_2005'] = 'Pre-2005'
frame.loc[(frame["Year_of_Release"]>=2005),'Post_Pre_2005'] = 'Post-2005'
#frame.loc[(frame["Year_of_Release"]=2005),'Post_Pre_2005'] = 'In-2005'
```


```python
print(frame)
```

                                    Name Platform  Year_of_Release         Genre  \
    0                         Wii Sports      Wii             2006        Sports   
    1                  Super Mario Bros.      NES             1985      Platform   
    2                     Mario Kart Wii      Wii             2008        Racing   
    3                  Wii Sports Resort      Wii             2009        Sports   
    4           Pokemon Red/Pokemon Blue       GB             1996  Role-Playing   
    ...                              ...      ...              ...           ...   
    16445  Samurai Warriors: Sanada Maru      PS3             2016        Action   
    16446               LMA Manager 2007     X360             2006        Sports   
    16447        Haitaka no Psychedelica      PSV             2016     Adventure   
    16448               Spirits & Spells      GBA             2003      Platform   
    16449            Winning Post 8 2016      PSV             2016    Simulation   
    
              Publisher  NA_Sales  EU_Sales  JP_Sales  Other_Sales  Global_Sales  \
    0          Nintendo     41.36     28.96      3.77         8.45         82.53   
    1          Nintendo     29.08      3.58      6.81         0.77         40.24   
    2          Nintendo     15.68     12.76      3.79         3.29         35.52   
    3          Nintendo     15.61     10.93      3.28         2.95         32.77   
    4          Nintendo     11.27      8.89     10.22         1.00         31.37   
    ...             ...       ...       ...       ...          ...           ...   
    16445    Tecmo Koei      0.00      0.00      0.01         0.00          0.01   
    16446   Codemasters      0.00      0.01      0.00         0.00          0.01   
    16447  Idea Factory      0.00      0.00      0.01         0.00          0.01   
    16448       Wanadoo      0.01      0.00      0.00         0.00          0.01   
    16449    Tecmo Koei      0.00      0.00      0.01         0.00          0.01   
    
          Critic_Score Critic_Count User_Score User_Count Developer Rating  \
    0               76           51          8        322  Nintendo      E   
    1                                                                        
    2               82           73        8.3        709  Nintendo      E   
    3               80           73          8        192  Nintendo      E   
    4                                                                        
    ...            ...          ...        ...        ...       ...    ...   
    16445                                                                    
    16446                                                                    
    16447                                                                    
    16448                                                                    
    16449                                                                    
    
          Post_Pre_2005  
    0         Post-2005  
    1          Pre-2005  
    2         Post-2005  
    3         Post-2005  
    4          Pre-2005  
    ...             ...  
    16445     Post-2005  
    16446     Post-2005  
    16447     Post-2005  
    16448      Pre-2005  
    16449     Post-2005  
    
    [16450 rows x 17 columns]
    


```python
#Finding whether average of global sales is higher before or after 2005
Average_data = frame.groupby(['Post_Pre_2005'])["Global_Sales"].mean()
```


```python
print(round(Average_data,2))
```

    Post_Pre_2005
    Post-2005    0.48
    Pre-2005     0.65
    Name: Global_Sales, dtype: float64
    


```python

```
