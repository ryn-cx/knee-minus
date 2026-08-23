# KneeMinus

[Disney+](https://www.disneyplus.com) API wrapper built using [Good Ass
Pydantic Integrator](https://github.com/ryn-cx/good-ass-pydantic-integrator) and
[Get Around](https://github.com/ryn-cx/get-around).

## Installation

```bash
uv add git+https://github.com/ryn-cx/kneeminus
```

## Usage

Every endpoint is called for the parsed model, and `download()` and `load()` are
the halves of that call.

```python
from kneeminus import KneeMinus

client = KneeMinus()

entity = client.entity("entity-422f6dcc-226f-44e7-98d4-22de69b31cf3")
season_one = client.entity(
    "entity-422f6dcc-226f-44e7-98d4-22de69b31cf3",
    season_id="38ff3861-23ba-44b4-a2de-d756de57ba41",
)

downloaded = client.entity.download("entity-422f6dcc-226f-44e7-98d4-22de69b31cf3")
entity = client.entity.load(downloaded)
```
