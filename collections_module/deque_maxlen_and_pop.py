from collections import deque

recent_searches = deque(maxlen=5)

recent_searches.append("Python")
recent_searches.append("NumPy")
recent_searches.append("Pandas")
recent_searches.append("Machine Learning")
recent_searches.append("Statistics")
recent_searches.append("Deep Learning")
recent_searches.append("SQL")

print(recent_searches)
print(recent_searches[0])
first_item = recent_searches.popleft()
print(first_item)
print(recent_searches)
