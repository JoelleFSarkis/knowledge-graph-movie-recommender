from rdflib import Graph, Namespace
from collections import defaultdict

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
attribute_matches = defaultdict(int)

target_attrs = []
for s, p, o in g.triples((target, None, None)):
    if p == EX.has_actor:
        target_attrs.append((p, o, 2))
    elif p == EX.has_genre:
        target_attrs.append((p, o, 1))
    elif p == EX.directed_by:
        target_attrs.append((p, o, 2))

for (p, o, weight) in target_attrs:
    for s2, _, _ in g.triples((None, p, o)):
        if s2 != target:
            attribute_matches[s2] += weight

sorted_matches = sorted(attribute_matches.items(), key=lambda x: x[1], reverse=True)
print(f"\nSmart recommendations if you liked '{choice}':")
for movie_uri, score in sorted_matches:
    title = g.value(movie_uri, EX.title)
    if title:
        print(f"- {title} (score: {score})")
