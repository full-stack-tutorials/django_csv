import pytest

from csvupload_tests.pytest_utils import random_csv_filepath

BASE_URL = 'http://localhost:8000/v1/'


@pytest.mark.asyncio
async def test__csvupload__post(random_csv_filepath):
    import httpx
    import os

    url = f'{BASE_URL}csv-upload/'
    csv_filename = os.path.basename(random_csv_filepath)
    files = {'csv_file': (csv_filename, open(random_csv_filepath, 'rb'), 'text/csv')}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data={'csv_filename': csv_filename}, files=files)
        if response.status_code != 201:
            pytest.fail(f'Expected 201 status code back from web framework service. Recieved {response.status_code} instead.')