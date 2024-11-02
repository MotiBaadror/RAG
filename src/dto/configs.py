from dataclasses import dataclass


@dataclass
class QueryConfig:
    data_path: str
    model_name: str = 'tinyllama'
    storage_path: str = None

    def __post_init__(self):
        self.storage_path = f'storage/{self.data_path}'
