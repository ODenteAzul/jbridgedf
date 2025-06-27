from jbridgedf.parser import APIDataParser

# Example using FRED's API (Federal Reserve)
# Requires a registered API Key, that you can register for free in https://fred.stlouisfed.org

API_KEY = "paste here yhour API Key"
SERIE_ID = "GDP"
URL = f"https://api.stlouisfed.org/fred/series/observations?series_id={SERIE_ID}&api_key={API_KEY}&file_type=json"

parser = APIDataParser()
df = parser.get_from_api(
    url=URL,
    variable_list=["date", "value"],
    is_list=True,
    convert_timestamp=False,
    sanitize=False,
    frequency="auto",
    col_freq="date",
    date_as_index=True,
    date_format="%Y-%m-%d",
    data_key="observations"
)

print(df.head())
