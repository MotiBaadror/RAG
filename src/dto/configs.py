from dataclasses import dataclass


@dataclass
class QueryConfig:
    """
    Basic config for all the attribute used during the experiments
    """
    data_path: str = 'data/codelon_data'
    model_name: str = 'llama3.2'
    storage_path: str = None
    use_llama_parse: bool = True

    def __post_init__(self):
        self.storage_path = f'{self.data_path}_{self.model_name}'.replace('data/','storage/')
