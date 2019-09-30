# plex-mysql-flask
These scripts will create a connection to a backend MySQL database containing Plex data about movies I own and serve that data up in a datatable front-end. 

To begin perform the following -
* Clone the repo
* Change into the directory of the repo and install the requirements via pip -
  * `pip install -r requirements.txt`
* Set the environment variables listed below. These variables describe the connection to MySQL -
  * mysql_username
  * mysql_password
  * mysql_db
  * mysql_ip
  * mysql_port
  * mysql_table
* Start the production WSGI server waitress -
  * `python waitress_server.py 2&1> /dev/null &`

## The MySQL table schema
In order for the datatable to render properly, the following schema must be used -

| Column           | Type          | Null | Key |
|------------------|---------------|------|-----|
| movie_title      | varchar(200)  | No   | PRI |
| movie_year       | varchar(4)    | No   | PRI |
| movie_rating     | varchar(100)  | Yes  |     |
| movie_resolution | varchar(100)  | Yes  |     |
| movie_container  | varchar(25)   | Yes  |     |
| movie_director   | varchar(1000) | Yes  |     |
| movie_genre      | varchar(1000) | yes  |     |
