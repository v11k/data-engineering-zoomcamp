import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import PageNumberPaginator


@dlt.resource(name="rides")
def ny_taxi_rides():
    client = RESTClient(
        base_url = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api",
        paginator = PageNumberPaginator(base_page = 1)
    )
    for page in client.paginate("data_engineering_zoomcamp_api"):
        yield page

if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name = "taxi_pipeline",
        destination = "duckdb",
        dataset_name = "ny_taxi_data"
    )

    load_info = pipeline.run(ny_taxi_rides())
    print(load_info)