
class Session:
    """
        the booking sesssion, create initally or after finishing one booking
    """

    def __init__(self):
        self.past_suggestions = []
        self.n_people = 0
        self.min_date = None
        self.max_daye = None
        self.trip_length = 0



class Core:
    """
        core logic that implements the mainapi
    """
    def __init__(self):
        self.favorite_bookings = []


