print(f"begin ->> common_data.py")

from datautils import SourceData

QuoteInfo = tuple[str, str, str, str, str]
AttributeInfo = tuple[str, str]

ParameterInfo = dict[str: str]   # "cod", "name", "left", "right", "measure", "step", "type"

DataBank = dict[str: SourceData]


data_bank: DataBank = {
    "tables": None,
    "quotes": None,
    "attributes": None,
    "parameters": None
}

print(f"end ->> common_data.py")




