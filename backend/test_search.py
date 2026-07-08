from utils.search import SemanticSearch

search_engine = SemanticSearch()

query = "What safety equipment should employees wear?"

results = search_engine.search(query)

print(results)