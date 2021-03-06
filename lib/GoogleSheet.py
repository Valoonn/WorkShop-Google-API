import sys
from lib import getCreds
from googleapiclient.discovery import build
import gspread

## Creer un dossier sur Google Drive et copier son ID ici
WORKSHOP_FOLDER_ID = "1wxsqHjFMJBB4UueMGFsiUzKpFk3cz2n_"


################## createSheet(fileName, folderId = '') ####################
# argv :
#   fileName : le nom du SpreadSheet que vous voulez creer
#   folderId : l'ID du dossier dans lequels vous voulez creer le SpreadSheet
#       (si vide : SpreadSheet creer au root du Drive)
# return :
#   Le nom du fichier créer
############################################################################


def createSheet(fileName, folderId = '') :

    drive_service = build('sheets', 'v4', credentials=getCreds.getCred())

    ## Creer ici le sheet


    drive = build('drive', 'v3', credentials=getCreds.getCred())


    ## Deplacer le sheet dans le dossier


    return (fileName)


def initSheet(sheet) :
    sheet.insert_row(["NOM DU RESTAURANT", "ADDRESSE", "OUVERT ?", "NOTE"], 1)



################## fillWithData(info, sheet) ####################
# argv :
#   info : la requette json avec les info que vous voulez rentrer dans le Sheet
#   sheet : l'acces au sheet (return de openSheet())
# return :
#   void
##################################################################


def fillWithData(info, sheet) :
    try :
        name = info["name"]
    except KeyError:
        ouvert = "N/A"
    try :
        address = info["formatted_address"]
    except KeyError:
        ouvert = "N/A"
    try :
        ouvert = str(info["opening_hours"]["open_now"])
    except KeyError:
        ouvert = "N/A"
    try :
        note = str(info["rating"]) + "/5"
    except KeyError:
        note = "N/A"


################## openSheet(fileName) ##########################
# argv :
#   fileName : le nom du SpreadSheet que vous voulez ouvrir
# return :
#   L'acces au SpreadSheet
#################################################################

def openSheet(fileName) :
    client = gspread.authorize(getCreds.getCred())


    initSheet(sheet)

