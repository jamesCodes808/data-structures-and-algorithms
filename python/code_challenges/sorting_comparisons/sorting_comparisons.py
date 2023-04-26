

def sort_compare_year(movie_lst):
    sorted_movies = sorted(movie_lst, key=lambda x: (x['year'], x['title']), reverse=True)
    return sorted_movies

def remove_leading_articles(title):
    articles = ["A", "An", "The"]

    for article in articles:
        if title.startswith(article):
            return title[len(article):].lstrip()

    return title

def sort_compare_alphabetical(movie_lst):

    for movie in movie_lst:
        movie['modified_title'] = remove_leading_articles(movie['title'])

    sorted_movies_by_alphabetical = sorted(movie_lst, key=lambda x: x['modified_title'])

    sorted_titles_by_alphabetical = [movie['title'] for movie in sorted_movies_by_alphabetical]

    return sorted_movies_by_alphabetical


if __name__ == '__main__':
    movies = [
        {
            'title': "Beetlejuice",
            'year': 1988,
            'genres': ["Comedy", "Fantasy"],
        },
        {
            'title': "The Cotton Club",
            'year': 1984,
            'genres': ["Crime", "Drama", "Music"],
        },
        {
            'title': "The Shawshank Redemption",
            'year': 1994,
            'genres': ["Crime", "Drama"],
        },
        {
            'title': "Crocodile Dundee",
            'year': 1986,

            'genres': ["Adventure", "Comedy"],
        },
        {
            'title': "Valkyrie",
            'year': 2008,
            'genres': ["Drama", "History", "Thriller"],
        },
        {
            'title': "Ratatouille",
            'year': 2007,
            'genres': ["Animation", "Comedy", "Family"],
        },
        {
            'title': "City of God",
            'year': 2002,

            'genres': ["Crime", "Drama"],
        },
        {
            'title': "Memento",
            'year': 2000,

            'genres': ["Mystery", "Thriller"],
        },
        {
            'title': "The Intouchables",
            'year': 2011,

            'genres': ["Biography", "Comedy", "Drama"],
        },
        {
            'title': "Stardust",
            'year': 2007,
            'genres': ["Adventure", "Family", "Fantasy"],
        },
    ]

    print(sort_compare_year(movies))
    print(sort_compare_alphabetical(movies))


