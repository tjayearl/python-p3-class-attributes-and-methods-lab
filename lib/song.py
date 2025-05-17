class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        Song.add_song_to_count()

        # Add genre and artist to lists (all entries, including duplicates)
        Song.genres.append(genre)
        Song.artists.append(artist)

        # Update unique genres and artists lists
        Song.add_to_genres()
        Song.add_to_artists()

        # Update genre and artist counts (histograms)
        Song.add_to_genre_count()
        Song.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        # Remove duplicates, keep only unique genres
        cls.genres = list(set(cls.genres))

    @classmethod
    def add_to_artists(cls):
        # Remove duplicates, keep only unique artists
        cls.artists = list(set(cls.artists))

    @classmethod
    def add_to_genre_count(cls):
        # Reset the dictionary and count frequencies again
        cls.genre_count = {}
        for genre in cls.genres:
            # Actually count how many times this genre appears in the full list
            count = cls.genres.count(genre)
            cls.genre_count[genre] = count

        # However, this above approach only counts unique genres once each, so better:
        # Instead, count directly from the full list of genres (including duplicates)
        cls.genre_count = {}
        for genre in cls.genres:
            cls.genre_count[genre] = cls.genres.count(genre)

    @classmethod
    def add_to_artist_count(cls):
        # Reset the dictionary and count frequencies again
        cls.artist_count = {}
        for artist in cls.artists:
            cls.artist_count[artist] = cls.artists.count(artist)
