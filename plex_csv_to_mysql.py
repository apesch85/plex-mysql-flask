import csv
import os
from mysql import connector

file_location = '/mnt/c/Users/user/Downloads/plex_list.csv'

mysql_username = os.environ['mysql_username']
mysql_password = os.environ['mysql_password']
plex_db = os.environ['plex_db']
mysql_ip = os.environ['mysql_ip']
mysql_port = int(os.environ['mysql_port'])
plex_table = os.environ['plex_table']


def read_csv(file_name):
	with open(file_name) as plex_reader:
		plex_records = csv.reader(plex_reader, delimiter=',')
		for row in plex_records:
			print row

	return plex_records


def write_mysql(plex_movies=None, plex_tv_shows=None):
	plexdb = mysql.connector.connect(
		host=mysql_ip,
  		user=mysql_username,
  		passwd=mysql_password,
  		database=plex_db
  		)

	plexcursor = plexdb.cursor()

	if plex_movies:
		sql = ('INSERT INTO movies (movie_title, movie_year, '
			   'movie_rating, movie_resolution, movie_container, '
			   'movie_director, movie_genre VALUES (%s %s %s %s %s %s %s)')
		plexcursor.executemany(sql, plex_movies)

	if plex_tv_shows:
		sql = ('INSERT INTO tv_shows (tv_title, tv_year, tv_rating, '
			   'tv_studio, tv_genre VALUES (%s %s %s %s %s)')
		plexcursor.executemany(sql, plex_tv_shows)

def main():
	movies = read_csv(file_location)
	write_mysql(plex_movies=movies)

if __name__ == '__main__':
	main()