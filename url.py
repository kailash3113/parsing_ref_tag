import pandas as pd 
from google.colab import files
import io
uploaded = files.upload()

df = pd.read_csv(io.BytesIO(uploaded['reference data - Sheet1.csv']))

cus = df['Customer']
prj = df['Project']
art_id = df['Article_id']

for i,j,k in zip(cus,prj,art_id):
  string = 'https://kriya2.kriyadocs.com/api/getxml/?apiKey=cde4c89b-e452-4ba5-b493-01c691033b72&doi=',k,'&customer=',i,'&project=',j,'&xmltype=raw'
  sample = ''.join(string)
  print(sample)

