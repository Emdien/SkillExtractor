import csv
import regex as re

if __name__ == '__main__':
    skill_file = open(r'skills.csv', 'w', newline='')

    with open('all_skills.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer = csv.writer(skill_file)
        for row in reader:
            pattern = r'.*_G[1-3].*'
            er_skill = re.compile(pattern)
            result = er_skill.fullmatch(row[0].rstrip())
            if result:
                writer.writerow(row)

                
    skill_file.close()