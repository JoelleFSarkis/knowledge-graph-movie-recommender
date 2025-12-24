from rdflib import Graph, Literal, Namespace, RDF

EX = Namespace("http://example.org/")

def add_movie(g, movie_id, title, genre, director, actors):
    g.add((EX[movie_id], RDF.type, EX.Movie))
    g.add((EX[movie_id], EX.title, Literal(title)))
    g.add((EX[movie_id], EX.has_genre, EX[genre]))
    g.add((EX[movie_id], EX.directed_by, EX[director]))
    for actor in actors:
        g.add((EX[movie_id], EX.has_actor, EX[actor]))

def build_movie_graph():
    g = Graph()
    movies = [
        ("Movie1", "Inception", "ScienceFiction", "ChristopherNolan", ["LeonardoDiCaprio"]),
        ("Movie2", "Interstellar", "ScienceFiction", "ChristopherNolan", ["MatthewMcConaughey"]),
        ("Movie3", "The Revenant", "Drama", "AlejandroInarritu", ["LeonardoDiCaprio"]),
        ("Movie4", "Titanic", "Romance", "JamesCameron", ["LeonardoDiCaprio", "KateWinslet"]),
        ("Movie5", "DjangoUnchained", "Western", "QuentinTarantino", ["LeonardoDiCaprio", "JamieFoxx"]),
        ("Movie6", "TheDarkKnight", "Action", "ChristopherNolan", ["ChristianBale", "HeathLedger"]),
        ("Movie7", "Shutter Island", "Thriller", "MartinScorsese", ["LeonardoDiCaprio"]),
        ("Movie8", "The Wolf of Wall Street", "Biography", "MartinScorsese", ["LeonardoDiCaprio", "JonahHill"]),
        ("Movie9", "Gravity", "ScienceFiction", "AlfonsoCuaron", ["SandraBullock", "GeorgeClooney"]),
        ("Movie10", "Tenet", "Action", "ChristopherNolan", ["JohnDavidWashington"]),
        ("Movie11", "Memento", "Mystery", "ChristopherNolan", ["GuyPearce"])
    ]
    for movie in movies:
        add_movie(g, *movie)
    g.serialize("movie_graph_full.ttl", format="turtle")

if __name__ == "__main__":
    build_movie_graph()
