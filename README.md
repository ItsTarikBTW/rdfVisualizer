# RDF Visualizer

This repository provides a tool to convert RDF Turtle files (.ttl) into visual graphs using Graphviz. The application parses RDF data, creates graphs with styled nodes and edges, and generates PNG images for each Turtle file.

## Example: The Beatles

The provided `Beatles.ttl` file demonstrates the RDF representation of a music group. It includes information about the band, its members, albums, and songs. For example:

- Defines the band "The Beatles" and its members.
- Specifies an album "Please Please Me" with details such as release date.
- Details a song "Love Me Do" with attributes like length and writers.

(Example graph generated for `Beatles.ttl` from the `data/` directory.)
![The Beatles Graph](graphs/Beatles.png)
v1
![The Beatles Graph](graphs/Beatles_rdf_graph.png)

## How to Run

1. **Prepare your environment:**  
    Ensure you have Docker installed or Python 3.12 with required libraries.

2. **Run with Docker:**  
     Build and run the container with:
     ```
     docker build -t rdf-visualizer .
     docker run --rm rdf-visualizer
     ```
    This will parse the Turtle files in the `data/` directory and generate graph images in the `graphs/` folder.

3. **Run Locally:**  
     - Install dependencies:
        ```
        pip install -r requirements.txt
        ```
     - Execute the application:
        ```
        python main.py
        ```
     Graph images will be saved in the `graphs/` directory.

## Files

- **main.py & main_v1.py:** Python scripts to parse RDF files and generate visual graphs.
- **Dockerfile:** For containerized execution.
- **requirements.txt:** Contains required Python libraries.
- **data/**: Directory containing Turtle (.ttl) files.
- **graphs/**: Output folder for generated graph images.
