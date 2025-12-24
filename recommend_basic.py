from rdflib import Graph, Namespace

EX = Namespace("http://example.org/")
g = Graph()
g.parse("movie_graph_full.ttl", format="turtle")

movie_titles = {
    "Inception": "Movie1",
    "Interstellar": "Movie2",
    "The Revenant": "Movie3",
    "Titanic": "Movie4",
    "Django Unchained": "Movie5",
    "The Dark Knight": "Movie6",
    "Shutter Island": "Movie7",
    "The Wolf of Wall Street": "Movie8",
    "Gravity": "Movie9",
    "Tenet": "Movie10",
    "Memento": "Movie11"
}

choice = input("Which movie did you like?\n" + "\n".join(movie_titles.keys()) + "\n\nYour choice: ")
movie_id = movie_titles.get(choice.strip())
if not movie_id:
    print("Movie not found.")
    exit()

target = EX[movie_id]
related_movies = set()

for s, p, o in g.triples((target, None, None)):
    if p in [EX.has_actor, EX.has_genre]:
        for s2, p2, o2 in g.triples((None, p, o)):
            if s2 != target:
                title = g.value(s2, EX.title)
                if title:
                    related_movies.add(str(title))

print(f"\nRecommended movies if you liked '{choice}':")
for m in related_movies:
    print("-", m)
