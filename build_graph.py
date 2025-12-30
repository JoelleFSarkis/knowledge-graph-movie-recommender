from rdflib import Graph, Literal, Namespace, RDF

EX = Namespace("http://example.org/")

def add_movie(g, movie_id, title, genre, director, actors,date):
    g.add((EX[movie_id], RDF.type, EX.Movie))
    g.add((EX[movie_id], EX.title, Literal(title)))
    g.add((EX[movie_id], EX.has_genre, EX[genre]))
    g.add((EX[movie_id], EX.directed_by, EX[director]))
    g.add((EX[movie_id], EX.directed_by, EX[date]))
    for actor in actors:
        g.add((EX[movie_id], EX.has_actor, EX[actor]))

def build_movie_graph():
    g = Graph()
    movies = [
        ("Movie1", "Inception", "ScienceFiction", "ChristopherNolan", ["LeonardoDiCaprio"], "2010"),
        ("Movie2", "Interstellar", "ScienceFiction", "ChristopherNolan", ["MatthewMcConaughey","2014"]),
        ("Movie3", "The Revenant", "Drama", "AlejandroInarritu", ["LeonardoDiCaprio"], "2015"),
        ("Movie4", "Titanic", "Romance", "JamesCameron", ["LeonardoDiCaprio", "KateWinslet"], "1997"),
        ("Movie5", "DjangoUnchained", "Western", "QuentinTarantino", ["LeonardoDiCaprio", "JamieFoxx"],"2012"),
        ("Movie6", "TheDarkKnight", "Action", "ChristopherNolan", ["ChristianBale", "HeathLedger"],"2010"),
        ("Movie7", "Shutter Island", "Thriller", "MartinScorsese", ["LeonardoDiCaprio"],"2010"),
        ("Movie8", "The Wolf of Wall Street", "Biography", "MartinScorsese", ["LeonardoDiCaprio", "JonahHill"],"2013"),
        ("Movie9", "Gravity", "ScienceFiction", "AlfonsoCuaron", ["SandraBullock", "GeorgeClooney"],"2013"),
        ("Movie10", "Tenet", "Action", "ChristopherNolan", ["JohnDavidWashington"],"2020"),
        ("Movie11", "Memento", "Mystery", "ChristopherNolan", ["GuyPearce"], "2000")
    ]
    for movie in movies:
        add_movie(g, *movie)
    g.serialize("movie_graph_full.ttl", format="turtle")

if __name__ == "__main__":
    build_movie_graph()
