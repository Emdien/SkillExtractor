import csv
import regex as re


# Objetivos: Quiero una consola que me permita extraer determinadas Skill IDs de determinadas clases y specs
# Secundario: Extraer Skill IDs de una skill en particular indicando class, spec y nombre de skill.

if __name__ == '__main__':
    skill_file = open(r'skills.csv', 'w', newline='')

    with open('all_skills.csv') as File:
        #Abre un reader en el fichero de datos
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        #Abre un writer en el fichero resultante
        writer = csv.writer(skill_file)
        for row in reader:
            # Patron global. Extrae todas las skills de todas las clases y specs
            pattern = r'.*_G[1-3].*'
            er_skill = re.compile(pattern)
            result = er_skill.fullmatch(row[0].rstrip())
            if result:
                writer.writerow(row)

                
    skill_file.close()