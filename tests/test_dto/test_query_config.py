from dto.configs import QueryConfig


def test_query_config():
    config = QueryConfig(
        data_path='data/codelon_data'
    )
    assert config.model_name == 'llama3.2'
    assert config.storage_path == 'storage/codelon_data_llama3.2'