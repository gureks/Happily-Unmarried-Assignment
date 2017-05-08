import os
from random import randint
from flask import Flask, render_template
from data import club_data

app  = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(20)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/result')
def result():
	groups = [[],[],[],[],[],[],[],[]]
	for club in club_data:
		# print(club, club_data[club]['Champion'])
		if club_data[club]['Champion'] == 1:
			flag = False
			while flag is False:
				number = randint(0,7)
				if groups[number] == []:
					groups[number].append(club_data[club])
					flag = True
	for club in club_data:
		# print(club, club_data[club]['Champion'])
		if club_data[club]['Champion'] == 0:
			while True:
				flag = True
				number = randint(0,7)
				if len(groups[number]) < 4:
					for temp in groups[number]:
						if temp['Country'] == club_data[club]['Country']:
							flag = False
				else:
					flag = False
				if flag:
					groups[number].append(club_data[club])
					break;
	return render_template('result.html', groups=groups)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
