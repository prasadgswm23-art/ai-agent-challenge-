import random

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.
    """
    distribution = {}
    total_pages = len(corpus)
    links = corpus[page]

    # Case 1: The current page has NO outgoing links
    # Every page in the corpus gets an equal probability: 1 / total_pages
    if len(links) == 0:
        for p in corpus:
            distribution[p] = 1 / total_pages
        return distribution

    # Case 2: The current page HAS outgoing links
    # TODO: Loop through every page 'p' in 'corpus':
    # 1. Start with the random jump probability: (1 - damping_factor) / total_pages
    # 2. If 'p' is inside 'links', add: damping_factor / len(links)
    # 3. Save that total into distribution[p]

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.
    """
    # Create a dictionary to count how many times each page is visited (start at 0)
    counts = {page: 0 for page in corpus}

    # Pick the first page completely at random
    current_page = random.choice(list(corpus.keys()))
    counts[current_page] += 1

    # TODO: Loop (n - 1) times:
    # 1. Get probabilities for the next move using transition_model(corpus, current_page, damping_factor)
    # 2. Pick the next page based on those probabilities using:
    #    next_page = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
    # 3. Add 1 to counts[next_page] and update current_page = next_page

    # TODO: Divide each count in 'counts' by 'n' so they become probabilities, then return it