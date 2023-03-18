# Data Modeling with Postgres

ETL pipeline for music data using Python and PostgreSQL.

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are file paths to two files in this dataset.


```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```
And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.
```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

```


## Log Dataset
The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.
```
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```
## Create Tables
Write CREATE statements in sql_queries.py to create each table.
```
python create_tables.py
```
## ETL pipeline

```
python etl.py.py
```

### we can see the result by PGAdmin as beloww:

Songs Table:
![songs](ScreenShots/songs.png "songs")

users Table:
![users](ScreenShots/songs.png "users")

artists Table:
![artists](ScreenShots/rtists.png "artists")

time Table:
![time](ScreenShots/time.png "time")

songplays Table:
![songplay](ScreenShots/songplay.png "songplay")


## Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

### ERD 
![ERD](ScreenShots/ERD.png "ERD")

## Now I test the project localy in my machine
### run test.ipynb on Jupyter:
the result as below screen shoots:

### First test
![first](ScreenShots/first.png "first")

### Second test:
![second](ScreenShots/second.png "second")

### Third test:
![third](ScreenShots/third.png "third")

### Fourth test:
![fourth](ScreenShots/fourth.png "fourth")

### Fifth test:
![fifth](ScreenShots/fifth.png "fifth")
