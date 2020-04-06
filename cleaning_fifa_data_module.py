#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



## Creamos un clase
class fifa_data():
    
## Creamos una función para limpiar el dataframe    
    def load_drop_data(self,data_file):
        
        #importamos los datos
        raw_data = pd.read_csv(data_file, delimiter = ',')
        #Creamos una copia del dataframe
        df = raw_data.copy()
        # Eliminamos la columna Unnamed 0 ya que es igual al índice que viene por defecto con pandas.
        # También eliminamos las columnas que no son útiles.
        df = df.drop(columns = ['Unnamed: 0', 'Photo','Flag', 'Club Logo'])
      
        
        ##Creamos una función que nos convierta la columna 'Joined' y 'Contract valid until' al formato relevante y extraemos de 
        # la primera, el mes y el año, mientras que de la segunda, solamente el año.        
        
        df['Joined'] = pd.to_datetime(df.Joined, infer_datetime_format=True)
        df['Contract Valid Until'] = pd.to_datetime(df['Contract Valid Until'], infer_datetime_format=True)
        
        list_months_joined = []
        list_years_joined = []
        
        list_months_contract = []
        list_years_contract = []
        
        for i in range(df.shape[0]):
            list_months_joined.append(df['Joined'][i].month)
            list_years_joined.append(df['Joined'][i].year)
            
            list_months_contract.append(df['Contract Valid Until'][i].month)
            list_years_contract.append(df['Contract Valid Until'][i].year)
        
        #Unimos las listas creadas al dataframe y eliminamos la columna 'Joined'
        
        df['year_joined'] = list_years_joined
        df['month_joined'] = list_months_joined
        df.drop(columns = ['Joined'], inplace = True)
        
        
        df['valid_until_year'] = list_years_contract
        df['valid_until_month'] = list_months_contract
        df.drop(columns = ['Contract Valid Until'], inplace = True)
       
        
        #Eliminamos aquellas columnas que tienen muchos valores nulos.
        df.drop(columns = ['Loaned From'], inplace = True)
        #Reemplazamos valores nulos por 0s. en estas columnas que representan las habilidades para cada posición. En este caso,
        #la presencia de valores nulos se debía a los arqueros.
        df[['LS', 'ST','RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM',
       'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB',
       'RCB', 'RB']].fillna(0, inplace = True)
        
        #Eliminamos el resto de las filas que contengan valores nulos
        df.dropna(inplace = True)
        
        df.reset_index(drop = True, inplace = True)
        
        self.data = df
        
        return df
   
    def clean(self,x):
        
        
        try:
            if '€' in x:
                return x.replace('€','')
            elif '$'in x:
                return x.replace('$','')
        except: 
                return x

        df = self.data
        df['Value'] = df['Value'].apply(lambda x : self.clean(x))
        df['Wage'] = df['Wage'].apply(lambda x : self.clean(x))
        df['Release Clause'] = df['Release Clause'].apply(lambda x : self.clean(x))
        
        return df
    

    def limpiar(self,x):
        
            
            
        try:
            
            if 'M' in x:
                return x.replace('M','00000')
            elif 'K'in x:
                return x.replace('K','000')
            if '.' in x:
                return x.replace('.', '')
        except: 
                return x

        df = self.data
        df['Value'] = df['Value'].apply(lambda x : self.limpiar(x))
        df['Wage'] = df['Wage'].apply(lambda x : self.limpiar(x))
        df['Release Clause'] = df['Release Clause'].apply(lambda x : self.limpiar(x))
        
        return df
    
    
    

    
    
    
    
    
    
    
    
    
    
    
