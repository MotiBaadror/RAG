from components.set_index import get_files


def test_get_files():
    data_path = 'data/codelon_data'
    results = get_files(data_path=data_path)
    print(results)
    assert len(results) ==1