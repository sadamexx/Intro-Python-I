# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLong:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLong):
    def __init__(self, name, lat, long):
        super().__init__(lat, long) # bringing down the params from the parent class above
        self.name = name
        
        def __str__(self):
            return f"Waypoint: {self.name}, {self.lat}, {self.long}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(name, difficulty, size, lat, long):
        super().__init__(name, lat, long)
        self.difficulty = difficulty
        self.size = size
    
    def __str__(self):
        return f"Geocache: {self.name}, {self.difficulty}, {self.size},{self.lat}, {self.long}"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)
