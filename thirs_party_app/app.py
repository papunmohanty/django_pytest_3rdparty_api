from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index(location_id: int):
    if isinstance(location_id, int):
        return {
            "location_data": {
                "location_id": location_id,
                "location_name": f"Sample Location {location_id}",
                "address": f"Address {location_id}, for Shipment",
                "latitude": location_id*2.13,
                "longitude": location_id*7.89999
            }
        }
    else:
        return {"message": "No listing found"}
