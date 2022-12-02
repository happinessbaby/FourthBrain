import helpers

##CLUE: Footage from an ATM security camera is blurry but shows that the perpetrator is a tall male, at least 6'.
##CLUE: Found a wallet believed to belong to the killer: no ID, just loose change, and membership cards for AAA, Delta SkyMiles, the local library, and the Museum of Bash History. The cards are totally untraceable and have no name, for some reason.
##CLUE: Questioned the barista at the local coffee shop. He said a woman left right before they heard the shots. The name on her latte was Annabel, she had blond spiky hair and a New Zealand accent.

def solveCrime():
    AAA_members = helpers.csvReader("/home/yueqi/FourthBrain/data/memberships/AAA.csv")
    Delta_members = helpers.csvReader("/home/yueqi/FourthBrain/data/memberships/Delta_SkyMiles.csv")
    library_members = helpers.csvReader("/home/yueqi/FourthBrain/data/memberships/Terminal_City_Library.csv")
    museum_members = helpers.csvReader("/home/yueqi/FourthBrain/data/memberships/Museum_of_Bash_History.csv")
    
solveCrime()