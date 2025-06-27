from jbridgedf.parser import APIDataParser

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
parser = APIDataParser()
df = parser.get_from_api(
    url=url,
    variable_list=["data", "valor"],
    is_list=True,
    frequency="monthly",
    date_as_index=True
)
print(df.head())
