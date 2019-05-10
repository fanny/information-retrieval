class Index:
    def __init__(self, term, docid, frequency):
        self.term = term
        self.record = (docid, frequency)

    def get_frequency_feature(self):
        """Extract frequency feature of passed search
        :returns int a value representing the index frequency.
        """
        _, frequency = self.record

        return frequency

    def __repr__(self):
        return 'Index(term=%s, record=%s)' % (self.term, self.record)


