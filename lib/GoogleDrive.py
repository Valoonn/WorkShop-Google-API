import sys, json
from googleapiclient.discovery import build
from apiclient import errors
from lib import getCreds
from apiclient.http import MediaFileUpload


################## uploadFile(filePath) ####################
# argv :
#   filePath : le path du fichier que vous voulez upload
# return :
#   L'ID du fichier créer
############################################################

def uploadFile(filePath) :
    drive_service = build('drive', 'v3', credentials=getCreds.getCred())





################## createFolder(folderName) ####################
# argv :
#   folderName : le nom du dossier que vous voulez creer
# return :
#   L'ID du dossier créer
################################################################


def createFolder(folderName) :

    drive_service = build('drive', 'v3', credentials=getCreds.getCred())






################## deleteFolder(folderName) ####################
# argv :
#   folderName : le nom du dossier que vous voulez supprimer
# return :
#   void
################################################################

def deleteFolder(folderName) :

    ## Le nom du fichier est l'id que l'on trouve dans l'URL sur google drive

    ## https://drive.google.com/drive/folders/1KQo48aNWOQoEPltGpZ1EDR5Dl696MpxB
    ## ID = 1KQo48aNWOQoEPltGpZ1EDR5Dl696MpxB

    drive_service = build('drive', 'v3', credentials=getCreds.getCred())
