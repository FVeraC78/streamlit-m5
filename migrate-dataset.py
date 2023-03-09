import firebase_admin #importa modulo de firebase
from firebase_admin import credentials, firestore #permite importar keys
import pandas as pd

path = "./" 

cred = credentials.Certificate(path +"names-project-demo2-fverac78.json") 
firebase_admin.initialize_app(cred) #conecta a firebase

db = firestore.client() #crea una instancia de firestone
doc_ref = db.collection(u'profesores') # Set the name of the Collection

# Import data
df = pd.read_csv(path+'profesores.csv')

tmp = df.to_dict(orient='records')
list(map(lambda x: doc_ref.add(x), tmp)) #Ciclo que recorre cada renglon del csv y
#lo inserta en la collection names
