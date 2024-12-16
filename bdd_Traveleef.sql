DROP SCHEMA IF EXISTS societe_parfum Traveleef;
CREATE SCHEMA bdd_traveleef;
SET SEARCH_PATH to bdd_traveleef;

-- Table pour les Vols
CREATE TABLE vols (
    id SERIAL PRIMARY KEY,
    ville_depart VARCHAR(50) NOT NULL,
    ville_arrivee VARCHAR(50) NOT NULL,
    heure_depart DATETIME NOT NULL,
    heure_arrivee DATETIME NOT NULL,
    prix REAL NOT NULL,
    empreinte_carbone REAL NOT NULL,
    options_classe VARCHAR(50),
    options_passager VARCHAR(50),
    operateur VARCHAR(50)
);

-- Table pour les Trains
CREATE TABLE trains (
    id SERIAL PRIMARY KEY,
    ville_depart VARCHAR(50) NOT NULL,
    ville_arrivee VARCHAR(50) NOT NULL,
    heure_depart DATETIME NOT NULL,
    heure_arrivee DATETIME NOT NULL,
    prix REAL NOT NULL,
    empreinte_carbone REAL NOT NULL,
    options_classe VARCHAR(50),
    operateur VARCHAR(50)
);

-- Table pour les Bus
CREATE TABLE bus (
    id SERIAL PRIMARY KEY,
    ville_depart VARCHAR(50) NOT NULL,
    ville_arrivee VARCHAR(50) NOT NULL,
    heure_depart DATETIME NOT NULL,
    heure_arrivee DATETIME NOT NULL,
    prix REAL NOT NULL,
    empreinte_carbone REAL NOT NULL,
    operateur VARCHAR(50)
);

-- Table pour le Covoiturage
CREATE TABLE covoiturage (
    id SERIAL PRIMARY KEY,
    ville_depart VARCHAR(50) NOT NULL,
    ville_arrivee VARCHAR(50) NOT NULL,
    heure_depart DATETIME NOT NULL,
    heure_arrivee DATETIME NOT NULL,
    prix REAL NOT NULL,
    empreinte_carbone REAL NOT NULL,
    nom_conducteur VARCHAR(50),
    places_disponibles INTEGER NOT NULL
);

-- Table pour le Transport Maritime (Ferries et Bateaux)
CREATE TABLE transport_maritime (
    id SERIAL PRIMARY KEY,
    ville_depart VARCHAR(50) NOT NULL,
    ville_arrivee VARCHAR(50) NOT NULL,
    heure_depart DATETIME NOT NULL,
    heure_arrivee DATETIME NOT NULL,
    prix REAL NOT NULL,
    empreinte_carbone REAL NOT NULL,
    capacite INTEGER NOT NULL,
    operateur VARCHAR(50)
);

-- Table pour les Correspondances (gérer les connexions entre tous les types de transport)
CREATE TABLE correspondances (
    id SERIAL PRIMARY KEY,
    id_transport_depart INTEGER NOT NULL, 
    id_transport_arrivee INTEGER NOT NULL, 
    type_transport_depart VARCHAR(50) NOT NULL,
    type_transport_arrivee VARCHAR(50) NOT NULL,
    temps_minimum_correspondance INTEGER NOT NULL,
    lieu_correspondance VARCHAR(50) NOT NULL
);

-- Table pour les Itinéraires Multimodaux (stocker les itinéraires générés)
CREATE TABLE itineraires_multimodaux (
    id SERIAL PRIMARY KEY,
    segments_itineraire VARCHAR(50) NOT NULL,
    prix_total REAL NOT NULL,
    duree_totale INTEGER NOT NULL,
    empreinte_carbone_totale REAL NOT NULL,
    score REAL
);
