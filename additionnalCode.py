import os
import pandas as pd
import glob
import os.path


# we use the same path because we only want to rename folder to join them after
source = "C:\\Users\\Ivan\\Desktop\\csv"
destination = "C:\\Users\\Ivan\\Desktop\\csv"
listeFichiers = os.listdir(source)
for i in range(len(listeFichiers)):
    fichier = listeFichiers[i]
    zeros = 15 - len(fichier)
    nouveauNom = fichier[:7] + "0"*zeros + fichier[7:]
    print(fichier, "   \t--->", nouveauNom)
    os.rename(os.path.join(source, fichier), os.path.join(destination, nouveauNom))



# merge file
joined_files = os.path.join("C:\\Users\\Ivan\\Desktop\\csv", "dataSet*.csv")

# a list of all files
joined_list = glob.glob(joined_files)

# put all files in a dataframe
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)

# create a csv file with all files in from the dataframe
df.to_csv("C:\\Users\\Ivan\\Desktop\\csv\\dataSetAllIn.csv", index=False)