# -*- coding: utf-8 -*-
"""
Created on Thu May 10 09:23:46 2018

@author: Sandman
"""
#songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
songs = ([('z', 0.1, 9.1), ('a', 4.4, 4.0), ('b', 2.7, 1.2), ('cc', 3.5, 7.7), ('ddd', 5.1, 6.9)])

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    playlist_size = 0
    
    
    if songs[0][2] <= max_size:
        playlist.append(songs[0][0])
        playlist_size += songs[0][2]
        copy_songs = songs[1:]
        while playlist_size < max_size:
            temp = ''
            avail = max_size - playlist_size
            temp_size = avail
            for song in range(len(copy_songs)):
                if copy_songs[song][0] not in playlist:
                    if copy_songs[song][2] <= temp_size:
                        temp = copy_songs[song][0]
                        temp_size = copy_songs[song][2]
#                        print('temp-size: ' + str(temp_size))
            if temp_size + playlist_size <= max_size and temp is not '':
                playlist_size += temp_size
#                print('playlist size: ' + str(playlist_size))
                playlist.append(temp)
            else:
                break
#    print(playlist)    
    return playlist
    
    
song_playlist(songs, 14)   