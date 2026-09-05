from itertools import chain

python_topics = ["Variables", "Loops", "Functions"]
numpy_topics = ["Arrays", "Indexing", "Broadcasting"]
pandas_topics = ["DataFrame", "Filtering", "GroupBy"]

combined_topics = chain(python_topics, numpy_topics, pandas_topics)

for topic in combined_topics:
    print(topic)
