
from datetime import datetime, timedelta

# Classe représentant un segment de trajet
class Segment:
    def __init__(self, id, mode, departure, arrival, departure_time, arrival_time, price, carbon_footprint):
        self.id = id
        self.mode = mode  # Exemple : 'vol', 'train', 'bus'
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.carbon_footprint = carbon_footprint
        self.duration = (arrival_time - departure_time).seconds // 60  # Durée en minutes

# Classe représentant une correspondance entre deux segments
class Correspondance:
    def __init__(self, id_depart, id_arrivee, type_depart, type_arrivee, min_transfer_time, location):
        self.id_depart = id_depart
        self.id_arrivee = id_arrivee
        self.type_depart = type_depart
        self.type_arrivee = type_arrivee
        self.min_transfer_time = min_transfer_time
        self.location = location

# Classe représentant un itinéraire multimodal
class Itinerary:
    def __init__(self, segments):
        self.segments = segments
        self.total_price = sum(segment.price for segment in segments)
        self.total_duration = sum(segment.duration for segment in segments)
        self.total_carbon_footprint = sum(segment.carbon_footprint for segment in segments)

    def calculate_score(self, alpha=1.0, beta=1.0, gamma=1.0):
        """
        Calcule un score basé sur les pondérations définies par l'utilisateur.
        """
        return (alpha * self.total_price +
                beta * self.total_duration +
                gamma * self.total_carbon_footprint)

# Vérifie si une correspondance entre deux segments est valide
def is_valid_connection(segment1, segment2, min_transfer_time):
    """
    Vérifie si une correspondance est valide entre deux segments.
    """
    if segment1.arrival == segment2.departure and \
       segment1.arrival_time + timedelta(minutes=min_transfer_time) <= segment2.departure_time:
        return True
    return False

# Recherche des itinéraires multimodaux
def find_multimodal_routes(segments, correspondances, max_connections=2, sort_by="price"):
    """
    Recherche des itinéraires multimodaux en assemblant des segments avec des correspondances valides.
    """
    itineraries = []

    def build_itinerary(current_itinerary, remaining_connections):
        last_segment = current_itinerary[-1]

        for connection in correspondances:
            if connection.id_depart == last_segment.id and \
               connection.type_depart == last_segment.mode:
                # Récupérer le segment suivant
                next_segment = next(filter(lambda x: x.id == connection.id_arrivee and x.mode == connection.type_arrivee, segments), None)
                if next_segment:
                    # Vérifier la correspondance
                    if is_valid_connection(last_segment, next_segment, connection.min_transfer_time):
                        new_itinerary = current_itinerary + [next_segment]
                        if remaining_connections > 1:
                            build_itinerary(new_itinerary, remaining_connections - 1)
                        else:
                            itineraries.append(Itinerary(new_itinerary))

    # Initialisation : commencer avec chaque segment
    for segment in segments:
        build_itinerary([segment], max_connections)

    # Trier les itinéraires
    if sort_by == "price":
        itineraries.sort(key=lambda x: x.total_price)
    elif sort_by == "carbon_footprint":
        itineraries.sort(key=lambda x: x.total_carbon_footprint)
    elif sort_by == "duration":
        itineraries.sort(key=lambda x: x.total_duration)

    return itineraries

# Exemple de données
segments = [
    Segment(1, 'vol', 'Paris', 'Berlin', datetime(2023, 11, 12, 8, 0), datetime(2023, 11, 12, 10, 0), 150, 50),
    Segment(2, 'train', 'Berlin', 'Varsovie', datetime(2023, 11, 12, 12, 0), datetime(2023, 11, 12, 16, 0), 60, 20),
    Segment(3, 'bus', 'Varsovie', 'Kiev', datetime(2023, 11, 12, 18, 0), datetime(2023, 11, 13, 2, 0), 40, 15)
]

correspondances = [
    Correspondance(1, 2, 'vol', 'train', 60, 'Berlin'),
    Correspondance(2, 3, 'train', 'bus', 120, 'Varsovie')
]

# Recherche d'itinéraires
itineraries = find_multimodal_routes(segments, correspondances, max_connections=2, sort_by="price")

# Affichage des résultats
for itinerary in itineraries:
    print(f"Itinéraire : Prix = {itinerary.total_price}, Durée = {itinerary.total_duration}, Carbone = {itinerary.total_carbon_footprint}")
