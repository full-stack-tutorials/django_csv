import pytest


@pytest.fixture(scope='function')
@pytest.mark.asyncio
async def random_csv_filepath() -> str:
    import aiofiles
    import random
    import tempfile

    from aiocsv import AsyncWriter

    filepath = tempfile.NamedTemporaryFile().name
    async with aiofiles.open(filepath, mode='w', encoding='utf-8', newline='') as async_stream:
        writer = AsyncWriter(async_stream, dialect='unix')
        await writer.writerow(['one', 'two'])
        await writer.writerow([random.randint(0, 9), random.randint(0, 9)])
        await writer.writerow([random.randint(0, 9), random.randint(0, 9)])
        await writer.writerow([random.randint(0, 9), random.randint(0, 9)])
        await writer.writerow([random.randint(0, 9), random.randint(0, 9)])

    return filepath