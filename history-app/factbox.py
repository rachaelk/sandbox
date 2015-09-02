from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from collections import defaultdict
import json
import pandas as pd;
import time;
import datetime;

# NOTE: The name of the New York City Mapping database is newyork. 
# One may change this to fit their own names.
name_of_database = 'factbox'
engine = create_engine('postgresql://localhost/' + name_of_database, convert_unicode=True)
db_session = scoped_session(sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine
))

def obtainNewFact(dlist_facts):
	dlist_facts[0].append(raw_input('\nInfo to save >> '))
	dlist_facts[1].append(raw_input('\nDate begin >> '))
	dlist_facts[2].append(raw_input('\nDate end >> '))
	dlist_facts[3].append(raw_input('\nPages >> '))
	dlist_facts[4].append(raw_input('\nBook title >> '))
	dlist_facts[5].append(raw_input('\nAuthor >> '))
	
	

def main():

	print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
	
	dlist_facts = [[], [], [], [], [], []]

	cont = raw_input("Would you like to begin?[y/n] >> ")
	while(cont[0] == 'y'):
		obtainNewFact(dlist_facts)
		cont = raw_input("\nWould you like to continue?[y/n] >> ")

	if len(dlist_facts[0])> 0:

		facts = pd.DataFrame({'book': dlist_facts[4],'pages': dlist_facts[3], 
			'author': dlist_facts[5], 'fact': dlist_facts[0],  
			'date_begin': dlist_facts[1], 'date_end': dlist_facts[2]})

		print facts


		# Allow for editing.
		edit = raw_input("Would you like to edit an entry?[y/n] >> ")
		while (edit[0] == 'y'):
			k   = raw_input('Which entry? Please type in its id (0, 1, ...) >> ')
			while k.isdigit == False: # error handling
				k   = raw_input('W\nI''m sorry. Please enter an integer. (0, 1, ...) >> ')
			k = int(k)

			col = raw_input('Which column? (author, books, start date, end date, ..) >> ')
			if col == 'start date':
				col = 'date_begin'
			if col == 'end date':
				col = 'date_end'
			if col == 'auth':
				col = 'author';
			if col == 'page':
				col = 'pages';
			if col not in ['fact', 'date_begin', 'date_end', 'author', 'pages', 'book']: # error handling
				col = raw_input('I''m sorry. The column you entered doesn''t exist. ' + 
					'Can you please re-enter the column?\nColumn names: author, book, dates, fact, pages\n>> ');
			new_info = raw_input('\nWhat would you like to enter? >> ')

			
			facts[col][k] = new_info;
			edit = raw_input("Would you like to continue editing?[y/n] >> ")

		print facts;
		facts['date_begin'] = pd.to_datetime(facts['date_begin'])
		facts['date_end']   = pd.to_datetime(facts['date_end'])

		print facts;

		cont = raw_input("\nLook okay to dump?")
		if cont[0]=='y':
			facts.to_sql(name ='facts', con = engine, if_exists = 'append', index = False)

if __name__ == '__main__': 
    main()
