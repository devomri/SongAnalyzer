from Model.Artist import Artist
from Model.MusicGenre import MusicGenre

# For hebrew songs analysis
HEBREW_ARTIST_WORD_THRESHOLD = 4500
HEBREW_YEAR_WORD_THRESHOLD = 500000

HEBREW_ARTIST_LIST = [
    Artist("Idan Raichel", MusicGenre.Israeli),
    Artist("Eviatar Banai", MusicGenre.Israeli),
    Artist("Moshe Peretz", MusicGenre.Oriental),
    Artist("Dudu Aharon", MusicGenre.Oriental),
    Artist("Kobi Peretz", MusicGenre.Oriental),
    Artist("Meir Ariel", MusicGenre.Israeli),
    Artist("Hadag Nahash", MusicGenre.Israeli),
    Artist("Lior Narkis", MusicGenre.Oriental),
    Artist("Mooki", MusicGenre.Israeli),
    Artist("Eyal Golan", MusicGenre.Oriental),
    Artist("Omer Adam", MusicGenre.Oriental),
    Artist("Regev Hod", MusicGenre.Oriental),
    Artist("Sarit Hadad", MusicGenre.Oriental),
    Artist("Shlomo Artzi", MusicGenre.Israeli),
    Artist("Shalom Hanoch", MusicGenre.Israeli),
    Artist("Arik Einstein", MusicGenre.Israeli),
    Artist("Rita", MusicGenre.Israeli),
    Artist("Miri Mesika", MusicGenre.Israeli),
    Artist("Keren Peles", MusicGenre.Israeli),
    Artist("Assaf Amdursky", MusicGenre.Israeli),
    Artist("Avraham Tal", MusicGenre.Israeli),
    Artist("Mashina", MusicGenre.Israeli),
    Artist("Yehoram Gaon", MusicGenre.Israeli),
    Artist("Yishi Levi", MusicGenre.Oriental),
    Artist("Avi Biter", MusicGenre.Oriental),
    Artist("Shlomi Shabat", MusicGenre.Oriental),
    Artist("Zohar Argov", MusicGenre.Oriental),
    Artist("Lior Farhi", MusicGenre.Oriental),
    Artist("Shimi Tavori", MusicGenre.Oriental),
    Artist("Ofer Levi", MusicGenre.Oriental),
    Artist("Moshik Afia", MusicGenre.Oriental),
    Artist("Zehava Ben", MusicGenre.Oriental),
    Artist("Idan Yaniv", MusicGenre.Oriental),
    Artist("Margalit Tzanani", MusicGenre.Oriental),
    Artist("Boaz Sharabi", MusicGenre.Oriental),
    Artist("Yehuda Poliker", MusicGenre.Israeli),
    Artist("Berry Sakharof", MusicGenre.Israeli),
    Artist("Rami Fortis", MusicGenre.Israeli),
    Artist("Mosh Ben Ari", MusicGenre.Israeli),
    Artist("Hayehudim", MusicGenre.Israeli),
    Artist("Aviv Geffen", MusicGenre.Israeli),
    Artist("Chava Alberstein", MusicGenre.Israeli),
    Artist("Matti Caspi", MusicGenre.Israeli),
    Artist("Shlomo Gronich", MusicGenre.Israeli),
    Artist("Yehudit Ravitz", MusicGenre.Israeli),
    Artist("Gali Atari", MusicGenre.Israeli),
    Artist("Nurit Galron", MusicGenre.Israeli),
    Artist("Danny Sanderson", MusicGenre.Israeli),
    Artist("Alon Oleartchik", MusicGenre.Israeli),
    Artist("Dani Litani", MusicGenre.Israeli),
    Artist("Gidi Gov", MusicGenre.Israeli),
    Artist("Ehud Banai", MusicGenre.Israeli),
    Artist("Meir Banai", MusicGenre.Israeli),
    Artist("Knesiyat Hasechel", MusicGenre.Israeli),
    Artist("Arkadi Duchin", MusicGenre.Israeli),
    Artist("Maor Cohen", MusicGenre.Israeli),
    Artist("Yermi Kaplan", MusicGenre.Israeli),
    Artist("Eran Zur", MusicGenre.Israeli),
    Artist("Ninet Tayeb", MusicGenre.Israeli),
    Artist("Arik Sinai", MusicGenre.Israeli),
]

# For english analysis
ENGLISH_ARTIST_WORD_THRESHOLD = 12000
ENGLISH_YEAR_WORD_THRESHOLD = 500000

HIPHOP_ARTIST_LIST = [
    Artist("Kool_Keith", MusicGenre.HipHop),
    Artist("Canibus", MusicGenre.HipHop),
    Artist("RZA", MusicGenre.HipHop),
    Artist("Killah_Priest", MusicGenre.HipHop),
    Artist("Eminem", MusicGenre.HipHop)
]

POP_ARTIST_LIST = [
    Artist("Lady_Gaga", MusicGenre.Pop),
    Artist("Big_Sean", MusicGenre.Pop),
    Artist("Ed_Sheeran", MusicGenre.Pop),
    Artist("Drake", MusicGenre.Pop),
    Artist("Migos", MusicGenre.Pop),
    Artist("Rihanna", MusicGenre.Pop),
    Artist("Adele", MusicGenre.Pop),
    Artist("Twenty_One_Pilots", MusicGenre.Pop),
    Artist("Ariana_Grande", MusicGenre.Pop),
    Artist("Taylor_Swift", MusicGenre.Pop),
    Artist("Maroon_5", MusicGenre.Pop),
    Artist("Justin_Bieber", MusicGenre.Pop),
    Artist("Imagine_Dragons", MusicGenre.Pop),
    Artist("John_Legend", MusicGenre.Pop),
    Artist("Metallica", MusicGenre.Pop),
    Artist("Sia", MusicGenre.Pop),
    Artist("Train", MusicGenre.Pop),
]