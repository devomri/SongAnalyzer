import ProcessingLayer.SongsAnalyzer as analyzer


def main():
    print("Songs Analyzer Project")
    songs_analyzer = analyzer.SongsAnalyzer()

    """
    rappers_list = ["kool_keith", "canibus", "cunninlynguists", "rza", "wu-tang", "killah_priest", "Drake"]
    for artist in rappers_list:
        diversity = songs_analyzer.lexical_diversity_by_artist(artist)
        print("Rapper: {0} has lexical diversity of {1}".
              format(artist, diversity))
    """

    years_intervals = [(1970, 1979), (1980, 1989), (1990, 1999), (2000, 2009)]
    for year_interval in years_intervals:
        diversity = songs_analyzer.lexical_diversity_by_year_interval(year_interval[0], year_interval[1])
        print("Interval {0}-{1} has diversity of: {2}".format(year_interval[0], year_interval[1], diversity))


if __name__ == '__main__':
    main()
