import json
from datetime import datetime
from pathlib import Path


def save_raw(jobs):

    Path("storage/transformed").mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    path = f"storage/transformed/jobs_{timestamp}.json"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            jobs,
            f,
            ensure_ascii=False,
            indent=2
        )