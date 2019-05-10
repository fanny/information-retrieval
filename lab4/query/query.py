class Query:
    def __init__(self, search):
        self.search = search

    def get_frequency_feature(self):
        """Extract frequency feature of passed search
        :returns dict a dict whose key is the term and value is your frequency.
        """
        query_features = {}
        terms = self.search.split(' ')
        for term in set(terms):
            query_features[term] = self.search.count(term)

        return query_features
