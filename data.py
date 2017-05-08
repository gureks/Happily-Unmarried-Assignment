import csv 

"""
Structure of the csv file, club_data array:
	Club Name : String
	Country : String
	Logo : String
	Champion : Boolean/Int
"""

club_data = {}


# read the file and save the data in club_data when application is deployed.
with open('data.csv', newline='', encoding='utf8') as file:
	rows = csv.reader(file, dialect='excel')
	next(rows) # skips the headings
	
	for row in rows:
		club_data[row[0]] = {
			"Club":row[0],
			"Country": row[1], 
			"Logo": row[2],
			"Champion": int(row[3])
		}

	file.close()