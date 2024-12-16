CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,                   
    first_name VARCHAR(50) NOT NULL,         
    last_name VARCHAR(50) NOT NULL,          
    email VARCHAR(120) UNIQUE NOT NULL,      
    password VARCHAR(255) NOT NULL,          
    role VARCHAR(10) NOT NULL               
);

CREATE TABLE IF NOT EXISTS travels (
    id SERIAL PRIMARY KEY,
    travel_info VARCHAR(255) NOT NULL,
    partner_url VARCHAR(255) NOT NULL,     
    price_outbound REAL,            
    price_round_trip REAL            
);

CREATE TABLE IF NOT EXISTS emissions (
    id SERIAL PRIMARY KEY,
    travel_id INTEGER NOT NULL,
    outbound_emission REAL NOT NULL,         
    return_emission REAL,           
    percentage REAL NOT NULL,              
    FOREIGN KEY (travel_id) REFERENCES travels(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS segments (
    id SERIAL PRIMARY KEY,
    travel_id INTEGER NOT NULL,
    segment_type VARCHAR(50) NOT NULL,       
    flight_date DATE NOT NULL,
    departure_time TIME NOT NULL,
    departure_location VARCHAR(255) NOT NULL,
    arrival_time TIME NOT NULL,
    arrival_location VARCHAR(255) NOT NULL,
    duration VARCHAR(50) NOT NULL,          
    logo_url VARCHAR(255),                  
    FOREIGN KEY (travel_id) REFERENCES travels(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS conditions (
    id SERIAL PRIMARY KEY,
    travel_id INTEGER NOT NULL,
    condition_text VARCHAR(255) NOT NULL,  
    FOREIGN KEY (travel_id) REFERENCES travels(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS services (
    id SERIAL PRIMARY KEY,
    travel_id INTEGER NOT NULL,
    service_text VARCHAR(255) NOT NULL,      
    FOREIGN KEY (travel_id) REFERENCES travels(id) ON DELETE CASCADE
);