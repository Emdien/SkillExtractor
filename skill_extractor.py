import csv
import regex as re

# TODO: Embed the .csv file so there is no need for external files (OR make use of cloud storage and extract it from there?)

# Returns an adjusted regex pattern
def genPattern(className, specID):
    classString = ""
    specString = ""

    if className.lower() == "blademaster" or className.lower() == "bm":
        classString = "BladeMaster_"
        if specID == "1" or specID.lower() == "fire":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "lightning":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "spectral":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "kungfumaster" or className.lower() == "kfm":
        classString = "KungfuMaster_"
        if specID == "1" or specID.lower() == "fire":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "wind":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "wolf":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "destroyer" or className.lower() == "des":
        classString = "Destroyer_"
        if specID == "1" or specID.lower() == "earth":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "shadow":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "twin steel": #? xd Idk 
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "forcemaster" or className.lower() == "fm":
        classString = "ForceMaster_"
        if specID == "1" or specID.lower() == "fire":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "ice":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "lightning":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "assasin" or className.lower() == "sin":
        classString = "Assassin_"
        if specID == "1" or specID.lower() == "serpent":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "shadow":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "phantom":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "summoner" or className.lower() == "sum":
        classString = "Summoner_"
        if specID == "1" or specID.lower() == "earth":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "wind":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "fantasy":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "warlock" or className.lower() == "wl":
        classString = "Warlock_"
        if specID == "1" or specID.lower() == "ice":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "shadow":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "tba":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "swordmaster" or className.lower() == "bd":
        classString = "SwordMaster_"
        if specID == "1" or specID.lower() == "wind":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "lightning":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "ghost":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "soulfighter" or className.lower() == "sf":
        classString = "SoulFighter_"
        if specID == "1" or specID.lower() == "earth":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "ice":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "tba":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "shooter" or className.lower() == "gun":
        classString = "Shooter_"
        if specID == "1" or specID.lower() == "fire":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "shadow":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "tba":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "warrior" or className.lower() == "war":
        classString = "Warrior_"
        if specID == "1" or specID.lower() == "lightning":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "ice":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "tba":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "archer" or className.lower() == "arc":
        classString = "Archer_"
        if specID == "1" or specID.lower() == "light":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "wind":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "tba":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString

    elif className.lower() == "thunderer" or className.lower() == "ast":
        classString = "Thunderer_"
        if specID == "1" or specID.lower() == "galaxy":
            specString = "G1_"
        elif specID == "2" or specID.lower() == "storm":
            specString = "G2_"
        elif specID == "3" or specID.lower() == "tba":
            specString = "G3_"
        elif specID == "0" or specID == "":
            specString = "G[1-3]_"
        else:
            print("Spec not valid! Try one of these values: [0,1,2,3]")
            return None
        return classString + specString
    else :
        print("Class not valid! Try one of these values: [bm, kfm, fm, des, sin, sum, bd, wl, sf, gun, war, arc, ast]")
        return None


if __name__ == '__main__':

    print("Choose a class (if empty, it will extract all classes and specs): ")
    selectedClass = input()
    selectedSpec = ""

    if selectedClass == "":
        # Global pattern for extracting skills from all classes
        regexPattern = r'.*_G[1-3].*'
    else:
        print("Choose a spec (if empty, it will extract for all specs): ")
        selectedSpec = input()

    print("Finally, select a filename (If empty, it will be class+spec.csv. If no class selected, it will be skills.csv): ")
    selectedFile = input()

    if selectedFile == "":
        if selectedClass == "":
            selectedFile = "skills.csv"
        else:
            selectedFile = selectedClass + selectedSpec + ".csv"
    else:
        selectedFile = selectedFile + ".csv"

    if selectedClass != "":
        pattern = genPattern(selectedClass, selectedSpec)
        regexPattern = pattern + r'.*'


    skill_file = open(selectedFile, 'w', newline='')

    with open('all_skills.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer = csv.writer(skill_file)

        for row in reader:
            er_skill = re.compile(regexPattern)
            result = er_skill.fullmatch(row[0].rstrip())
            if result:
                writer.writerow(row)

                
    skill_file.close()