from sys import argv
from libretro import default_session, RETRO_MEMORY_SAVE_RAM

with default_session(argv[1]) as session:
    size = session.core.get_memory_size(RETRO_MEMORY_SAVE_RAM)

    assert size is not None
    assert size > 0

    data = session.core.get_memory_data(RETRO_MEMORY_SAVE_RAM)

    assert data
    assert data is not None
    assert data.value
