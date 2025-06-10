ef GoogleSearch(query):
    results = list(search(query, num_results=5))
    # results = list(search(query, num_results=100, lang="en", ssl_verify=False))

    Answer = f"the search results for '{query}' are:\n[start]\n"

    for i in results:
        Answer += f"URL: {i}\n\n"

    Answer += "[end]"
    return Answer
