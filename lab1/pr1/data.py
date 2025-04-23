temp_db = [
    {
        "id": 1,
        "username": "johndoe",
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "password": "hashedpassword",
        "description": "A sample user",
        "created_at": "2025-03-05T12:00:00",
        "trips": [
            {
                "id": 1,
                "initiator": {"id": 1, "username": "johndoe"},
                "start_date": "2025-04-01",
                "end_date": "2025-04-10",
                "vehicle": "car",
                "description": "Trip to the mountains",
                "created_at": "2025-03-05T12:00:00",
                "status": "planned",
                "companions": [
                    {
                        "id": 1,
                        "trip_id": 1,
                        "companion_id": {"id": 2, "username": "janedoe"},
                        "status": "confirmed",
                        "created_at": "2025-03-05T12:00:00",
                    }
                ],
                "messages": [
                    {
                        "id": 1,
                        "trip_id": 1,
                        "sender_id": 1,
                        "message": "Looking forward to this trip!",
                        "created_at": "2025-03-05T12:05:00",
                    }
                ],
                "itineraries": [
                    {
                        "id": 1,
                        "trip_id": 1,
                        "stop_number": 1,
                        "location": "Mountain Base",
                        "arrival_date": "2025-04-01",
                        "departure_date": "2025-04-02",
                        "created_at": "2025-03-05T12:00:00",
                    }
                ],
            }
        ],
    },
    {
        "id": 2,
        "username": "janedoe",
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "janedoe@example.com",
        "password": "hashedpassword",
        "description": "Another sample user",
        "created_at": "2025-03-05T12:00:00",
        "trips": [],
    },
]
