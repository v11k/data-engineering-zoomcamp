import dlt
import requests

@dlt.resource(name="rides", write_disposition="replace")
def ny_taxi_rides():
    url = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"
    page = 1
    while True:
        params = {'page': page}
        response = requests.get(url, params=params)
        response.raise_for_status() # Stop if the API breaks
        data = response.json()

        # If the API returns an empty list, we have reached the end
        if not data:
            break

        yield data
        page += 1

if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="taxi_hw_v3",
        destination="duckdb",
        dataset_name="ny_taxi_data"
    )

    print("Starting the pipeline...")
    load_info = pipeline.run(ny_taxi_rides())
    print("--- SUCCESS ---")
    print(load_info)