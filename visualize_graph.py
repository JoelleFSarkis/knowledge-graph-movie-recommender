from rdflib import Graph, Namespace, RDF
import networkx as nx
from pyvis.network import Network

EX = Namespace("http://example.org/")
g = Graph()
g.parse("movie_graph_full.ttl", format="turtle")

def strip_ns(term):
    return str(term).split("/")[-1].split("#")[-1]

G = nx.Graph()
node_types = {}

# Identify node types
for s, p, o in g:
    if p == RDF.type and o == EX.Movie:
        node_types[strip_ns(s)] = "Movie"
    elif p == EX.has_actor:
        node_types[strip_ns(o)] = "Actor"
    elif p == EX.has_genre:
        node_types[strip_ns(o)] = "Genre"
    elif p == EX.directed_by:
        node_types[strip_ns(o)] = "Director"
    G.add_node(strip_ns(s))
    G.add_node(strip_ns(o))
    G.add_edge(strip_ns(s), strip_ns(o), label=strip_ns(p))

# Define colors
color_map = {
    "Movie": "skyblue",
    "Actor": "lightgreen",
    "Genre": "lightcoral",
    "Director": "orange"
}

# Build PyVis network
net = Network(height="700px", width="100%", bgcolor="#ffffff", font_color="black")
for node in G.nodes:
    ntype = node_types.get(node, "")
    color = color_map.get(ntype, "lightgray")
    net.add_node(node, label=node, color=color)

for u, v, d in G.edges(data=True):
    net.add_edge(u, v, label=d["label"])

net.show("movie_knowledge_graph_colored.html")
