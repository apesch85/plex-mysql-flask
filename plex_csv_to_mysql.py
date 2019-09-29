import csv
import os
import pymysql.cursors

file_location = '/Users/pesch/Downloads/plex_list.csv'

mysql_username = os.environ['mysql_username']
mysql_password = os.environ['mysql_password']
plex_db = os.environ['plex_db']
mysql_ip = os.environ['mysql_ip']
mysql_port = int(os.environ['mysql_port'])


def read_csv(file_name):
	print 'Reading in data...'
	plex_list = []
	with open(file_name) as plex_reader:
		plex_records = csv.reader(plex_reader, delimiter=',')
		for record in plex_records:
			plex_list.append(record)
	print 'Passing records to MySQL function...'
	print plex_list[0]
	return plex_list


def write_mysql(plex_movies=None, plex_tv_shows=None):
	print 'Initiating MySQL connection to plex db...'
	plexdb = pymysql.connect(
		host=mysql_ip,
		port=mysql_port,
  		user=mysql_username,
  		passwd=mysql_password,
  		db=plex_db,
  		charset='utf8mb4',
  		cursorclass=pymysql.cursors.DictCursor
  		)
	print 'Connection established!'

	if plex_movies:
	    with plexdb.cursor() as cursor:
	        # Create a new record
	        sql = ('INSERT IGNORE INTO movies '
	        	   '(movie_title, movie_year, movie_rating, movie_resolution, '
	        	   'movie_container, movie_director, movie_genre) VALUES '
	        	   '(%s, %s, %s, %s, %s, %s, %s)')

	        cursor.executemany(sql, plex_movies)

	elif plex_tv_shows:
		with plexdb.cursor() as cursor:
			sql = ('INSERT IGNORE INTO tv_shows (tv_title, tv_year, tv_rating, '
				   'tv_studio, tv_genre VALUES (%s, %s, %s, %s, %s)')
		
			cursor.executemany(sql, plex_tv_shows)

	else:
		raise Exception('Please provide some Plex data...')

	plexdb.commit()
	plexdb.close()

	print 'Writing to MySQL is complete!'


def main():
	movies = read_csv(file_location)
	write_mysql(plex_movies=movies)


if __name__ == '__main__':
	main()