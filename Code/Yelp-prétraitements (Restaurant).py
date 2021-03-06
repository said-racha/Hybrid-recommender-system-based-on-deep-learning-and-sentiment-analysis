# -*- coding: utf-8 -*-
"""Restaurant.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ByBFkD2NO2Ns8MbIs33xK8waiaeWmPDI
"""

from google.colab import drive
drive.mount('/content/gdrive')

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import ast

restaurant_json= pd.read_json('/content/drive/MyDrive/L3 PFE 2020 2021/Code/Yelp-data/Datasets.json/restaurants.json',lines=True)
restaurant_json[:3]

nomDuCsvFile='Restaurant1.csv'
restaurant_json.to_csv(nomDuCsvFile, sep='|', index=False) #transformation a un fichier csv

Restaurant1_csv=pd.read_csv(nomDuCsvFile, delimiter='|')
Restaurant1_csv[:3]

"""##Regler Pb ta3 Maps

###Attributes
"""

#mettre les lignes ta3 map dans une liste puis la convertir en df
attributes=[]

for i in range(Restaurant1_csv.shape[0]): #traiter autant de ligne qu'on souhaite du df
  restaurant_att_str=str(Restaurant1_csv.loc[i,'attributes']) #convertir en string
  restaurant_att_dict=ast.literal_eval(restaurant_att_str) #convertir en dict
  attributes.append(restaurant_att_dict)

Restaurant_att1_=pd.DataFrame.from_dict(attributes) #le df qui contient les element berk ta3 map

Restaurant_merged1 = Restaurant1_csv.merge(Restaurant_att1_, left_index=True, right_index=True) #concatener le def des colonnes de map avec le df original 

Restaurant_merged1.head()

"""Pr l'instant on a concatener le dataset orginal avec les maps de attributes 
il faut a present :

1.   drop la colone attributes (7alelna ses données en colones on en a plus besoin)
2.   reiterer le mm processus pr les colonnes qui contiennent encore des maps

"""

Restaurant_sansColAttribues=Restaurant_merged1.drop('attributes', axis=1)

Restaurant_sansColAttribues.head()

"""###Good For"""

#mettre les lignes ta3 map dans une liste puis la convertir en df
GoodFor=[]

for i in range(Restaurant_sansColAttribues.shape[0]): #traiter autant de ligne qu'on souhaite du df
  restaurant_att_str2=str(Restaurant_sansColAttribues.loc[i,'Good For']) #convertir en string
  restaurant_att_dict2=ast.literal_eval(restaurant_att_str2) #convertir en dict
  GoodFor.append(restaurant_att_dict2)

Restaurant_goodFor_=pd.DataFrame.from_dict(GoodFor) #le df qui contient les element berk ta3 map


Restaurant_merged2 = Restaurant_sansColAttribues.merge(Restaurant_goodFor_, left_index=True, right_index=True) #concatener le def des colonnes de map avec le df original 
Restaurant_merged2.head()

Restaurant_sansColGoodFor=Restaurant_merged2.drop('Good For', axis=1)
Restaurant_sansColGoodFor.head()

"""###Ambience"""

#mettre les lignes ta3 map dans une liste puis la convertir en df
Ambience=[]

for i in range(Restaurant_sansColGoodFor.shape[0]): #traiter autant de ligne qu'on souhaite du df
  restaurant_att_str3=str(Restaurant_sansColGoodFor.loc[i,'Ambience']) #convertir en string
  restaurant_att_dict3=ast.literal_eval(restaurant_att_str3) #convertir en dict
  Ambience.append(restaurant_att_dict3)

Restaurant_ambience_=pd.DataFrame.from_dict(Ambience) #le df qui contient les element berk ta3 map


Restaurant_merged3 = Restaurant_sansColGoodFor.merge(Restaurant_ambience_, left_index=True, right_index=True) #concatener le def des colonnes de map avec le df original 
Restaurant_merged3.head()

Restaurant_sansColAmbience=Restaurant_merged3.drop('Ambience', axis=1)
Restaurant_sansColAmbience.head()

"""###Final Maps"""

TotalActuel=Restaurant_sansColAmbience.columns
TotalVoulu=['business_id','latitude','longitude','Breakfast & Brunch', 'American (Traditional)', 'Burgers', 'Fast Food', 
        'American (New)', 'Chinese', 'Pizza', 'Italian', 'Sandwiches', 'Sushi Bars', 'Japanese', 
        'Indian', 'Mexican', 'Vietnamese', 'Thai', 'Asian Fusion','Take-out', 'Wi-Fi', 
        'dessert','latenight','lunch','dinner','breakfast','brunch', 'Caters', 
        'Noise Level','Takes Reservations', 'Delivery', 'romantic','intimate','touristy',
        'hipster','divey','classy','trendy','upscale','casual',
        'Parking', 'Has TV','Outdoor Seating', 'Attire', 'Alcohol', 'Waiter Service', 
        'Accepts Credit Cards', 'Good for Kids', 'Good For Groups', 
        'Price Range', 'Wheelchair Accessible']

nomDuCsvFile='Restaurant2_AvecMaps.csv'
Restaurant_sansColAmbience.to_csv(nomDuCsvFile, sep='|', index=False) #transformation a un fichier csv

"""##Traitement2 List

###Breakfast & Brunch
"""

b=False

for i in range(Restaurant_sansColAmbience.shape[0]):

  if ('Breakfast & Brunch'in Restaurant_sansColAmbience.loc[i,'categories']) :
    b=True

  if(b) :
    Restaurant_sansColAmbience.loc[i,'Breakfast & Brunch'] = 1
  else :
    Restaurant_sansColAmbience.loc[i,'Breakfast & Brunch'] = 0
  b=False

"""###American (Traditional)"""

b=False

for i in range(Restaurant_sansColAmbience.shape[0]):

  if ('American (Traditional)'in Restaurant_sansColAmbience.loc[i,'categories']) :
    b=True

  if(b) :
    Restaurant_sansColAmbience.loc[i,'American (Traditional)'] = 1
  else :
    Restaurant_sansColAmbience.loc[i,'American (Traditional)'] = 0
  b=False

"""###Burgers"""

b=False

for i in range(Restaurant_sansColAmbience.shape[0]):

  if ('Burgers'in Restaurant_sansColAmbience.loc[i,'categories']) :
    b=True

  if(b) :
    Restaurant_sansColAmbience.loc[i,'Burgers'] = 1
  else :
    Restaurant_sansColAmbience.loc[i,'Burgers'] = 0
  b=False

"""###Fast Food"""

b=False

for i in range(Restaurant_sansColAmbience.shape[0]):

  if ('Fast Food'in Restaurant_sansColAmbience.loc[i,'categories']) :
    b=True

  if(b) :
    Restaurant_sansColAmbience.loc[i,'Fast Food'] = 1
  else :
    Restaurant_sansColAmbience.loc[i,'Fast Food'] = 0
  b=False

"""###Le reste ta3 categories"""

categoriesRestantes=['American (New)','Chinese', 'Pizza', 'Italian', 'Sandwiches', 'Sushi Bars', 'Japanese', 
        'Indian', 'Mexican', 'Vietnamese', 'Thai', 'Asian Fusion']

for categorie in categoriesRestantes :
  b=False
  for i in range(Restaurant_sansColAmbience.shape[0]):

    if (categorie in Restaurant_sansColAmbience.loc[i,'categories']) :
      b=True

    if(b) :
      Restaurant_sansColAmbience.loc[i,categorie] = 1
    else :
      Restaurant_sansColAmbience.loc[i,categorie] = 0
    b=False
    
   
Restaurant_sansColAmbience.head()

Restaurant_sansColcategories=Restaurant_sansColAmbience.drop('categories', axis=1)
Restaurant_sansColcategories.head()

"""##Final"""

columns_items = ['business_id','latitude','longitude','Breakfast & Brunch', 'American (Traditional)', 'Burgers', 'Fast Food', 
        'American (New)', 'Chinese', 'Pizza', 'Italian', 'Sandwiches', 'Sushi Bars', 'Japanese', 
        'Indian', 'Mexican', 'Vietnamese', 'Thai', 'Asian Fusion','Take-out', 'Wi-Fi', 
        'dessert','latenight','lunch','dinner','breakfast','brunch', 'Caters', 
        'Noise Level','Takes Reservations', 'Delivery', 'romantic','intimate','touristy',
        'hipster','divey','classy','trendy','upscale','casual',
        'Has TV','Outdoor Seating', 'Attire', 'Alcohol', 'Waiter Service', 
        'Accepts Credit Cards', 'Good for Kids', 'Good For Groups', 
        'Price Range', 'Wheelchair Accessible']
Restaurant= Restaurant_sansColcategories[columns_items]

Restaurant.rename(columns = {'business_id':'item_id'}, inplace = True)

Restaurant

nomDuCsvFile='Restaurant_sansEncodage.csv'
Restaurant.to_csv(nomDuCsvFile, sep='|', index=False) #transformation a un fichier csv