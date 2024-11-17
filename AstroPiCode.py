from sense_hat import SenseHat
from gpiozero import MotionSensor
from time import *
import datetime
import pandas as pd



################################ fonctions ################################

def creerCsvVide(cheminCsv):
  with open(cheminCsv, 'w') as f:
    f.write("accelX,accelY,accelZ,gyroX,gyroY,gyroZ,magnX,magnY,magnZ,Heure,Minute,Seconde,mouvement")

def insertDonnees(listeDonnees, cheminCsv, nombreParametre):
  f = open(cheminCsv, "a")
  for i in range(len(listeDonnees)):
    if i%13 == 0:
        f.write("\n"+str(listeDonnees[i]))
    else:
        f.write(","+str(listeDonnees[i]))
  f.close()

blanc = (255, 255, 255)
sense = SenseHat()
sense.clear(blanc)
mouvement = False

def mouvement():
  sense.low_light = True
  rouge = (255, 0, 0)
  sense.clear(rouge)
  print('Mouvement détécté')
  sense.low_light = False
  mouvement = True
  return mouvement
  
def pasMouvement():
  blanc = (255, 255, 255)
  sense = SenseHat()
  sense.clear(blanc)
  print('Aucun mouvement détécté')
  mouvement = False
  return mouvement

def collecteDonnees():
  listeDonnees = []
  sense = SenseHat()
  for i in range(48):
    rawA = sense.get_accelerometer_raw()
    listeDonnees.append("{x},{y},{z}".format(**rawA))
    rawG = sense.get_gyroscope_raw()
    listeDonnees.append("{x},{y},{z}".format(**rawG))
    rawC = sense.get_compass_raw()
    listeDonnees.append("{x},{y},{z}".format(**rawC))
    
    temps = datetime.datetime.now()
    
    listeDonnees.append(temps.hour)
    listeDonnees.append(temps.minute)
    listeDonnees.append(temps.second)

    if mouvement():
        listeDonnees.append(mouvement())
    else:
        listeDonnees.append(pasMouvement())


    sleep(1)
    
  return listeDonnees
################################ fonctions ################################



################################ main execution ################################

chemin = '/home/pi/Desktop/astroPi/dataSet.csv'
liste = collecteDonnees()
print(liste)

creerCsvVide(chemin)
insertDonnees(liste,chemin,13)


################################ corrélation ################################

df = pd.read_csv(chemin)

print(df.corr(method = 'spearman'))

################################ corrélation ################################


pir = MotionSensor(4)



while True:
  if pir.motion_detected:
    mouvement()
  else:
    pasMouvement()

################################ main execution ################################



