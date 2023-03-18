import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """Extract data from raw song JSON file and INSERT to 'songs' and 'artists' tables.
    
    Parameters
    ----------
    cur : cursor
        cursor of psycopg2 database connection
    filepath : file
        song data file
    """

    # open song file
    song_df = pd.read_json(filepath, lines = True) 

    # insert song record
    song_data = song_df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = song_df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """Extract data from raw log JSON file and INSERT to 'time', 'users' and 'songplays' tables.
    
    Parameters
    ----------
    cur : cursor
        cursor of psycopg2 database connection
    filepath : file
        log data file
           
    
    Description: This function is responsible for performing the following tasks:
    1. Inserting time info into 'time' table.
    2. Upserting user info into 'users' table.
    3. Inserting user info into 'songplays' table.
    """
    # open log file
    log_df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    log_df = log_df[log_df['page'] == 'NextSong']

    # convert timestamp column to datetime
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    t = pd.to_datetime(log_df['ts'], unit = 'ms')
    time_data = (t, t.dt.hour, t.dt.day, t.dt.isocalendar().week, t.dt.month, t.dt.year, t.dt.weekday)
    time_df = pd.DataFrame.from_dict(dict(zip(column_labels, time_data)))
    
        
    # insert time data records
    
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df =  log_df[['userId' ,'firstName' ,'firstName' ,'gender' ,'level' ]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    log_df['ts']=pd.to_datetime(log_df['ts'],unit='ms')
    for index, row in log_df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = [row.ts,row.userId, row.level,songid, artistid,row.sessionId,row.location, row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)
       

def process_data(cur, conn, filepath, func):
    """Load song_data and log_data files and execute respective function with each file.
    
    Parameters
    ----------
    cur : cursor
        cursor of psycopg2 database connection.
    conn : connection
        connection of psycopg2
    filepath : string
        directory of files
    func : def
        function for processing of each file
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=udacity.postgres.database.azure.com port=5432 dbname=sparkifydb user=meezar password= udacity123! sslmode=require")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()