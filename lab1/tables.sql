CREATE TABLE IF NOT EXISTS account (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TYPE TRIP_VEHICLE AS ENUM ('car', 'motorcycle', 'bicycle', 'scooter', 'train', 'bus', 'plane', 'boat', 'walking');

CREATE TYPE TRIP_STATUS AS ENUM ('planned', 'in_progress', 'completed', 'canceled');

CREATE TABLE IF NOT EXISTS trips (
    id SERIAL PRIMARY KEY,
    initiator INTEGER NOT NULL REFERENCES account(id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    vehicle TRIP_VEHICLE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TRIP_STATUS NOT NULL
);

CREATE TYPE COMPANION_STATUS AS ENUM ('pending', 'confirmed', 'declined', 'canceled');

CREATE TABLE IF NOT EXISTS companions (
    id SERIAL PRIMARY KEY,
    trip_id INTEGER NOT NULL REFERENCES trips(id),
    companion_id INTEGER NOT NULL REFERENCES account(id),
    status COMPANION_STATUS DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS trip_messages (
    id SERIAL PRIMARY KEY,
    trip_id INTEGER NOT NULL REFERENCES trips(id),
    sender_id INTEGER NOT NULL REFERENCES account(id),
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS trip_itineraries (
    id SERIAL PRIMARY KEY,
    trip_id INTEGER NOT NULL REFERENCES trips(id),
    stop_number INTEGER NOT NULL,
    location TEXT NOT NULL,
    arrival_date DATE,
    departure_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
