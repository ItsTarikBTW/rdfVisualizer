import sys
import os
import glob
import rdflib
import pygraphviz as pgv

# Ensure graphs/ directory exists
graphs_dir = "graphs"
if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

# Find all Turtle files in the data/ directory
ttl_files = glob.glob(os.path.join("data", "*.ttl"))
if not ttl_files:
    print("No .ttl files found in the data/ directory.")
    sys.exit(1)

for ttl_file in ttl_files:
    print(f"Parsing {ttl_file}...")
    # Create a new RDF graph for each ttl file
    g = rdflib.Graph()
    g.parse(ttl_file, format="turtle")

    # Create a new Graphviz graph
    G = pgv.AGraph(directed=True)

    # Iterate over the triples and add edges
    for s, p, o in g:
        s_str = s.n3(g.namespace_manager).strip('"')
        p_str = p.n3(g.namespace_manager).strip('"')
        o_str = o.n3(g.namespace_manager).strip('"')
        G.add_edge(s_str, o_str, label=p_str)

    # Determine output file name: same name as ttl with .png extension inside graphs/
    base_name = os.path.splitext(os.path.basename(ttl_file))[0]
    output_path = os.path.join(graphs_dir, f"{base_name}_v1_graph.png")

    # Layout and draw the graph
    G.layout(prog='dot')
    G.draw(output_path)
    print(f"Graph image saved as {output_path}")