
from typing import List
from models.entry import Entry


class Source:
    async def get(self, domain) -> List[Entry]:
        raise NotImplementedError()