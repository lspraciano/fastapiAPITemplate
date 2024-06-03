
from configuration.configs import settings

import toml


def get_project_metadata() -> dict:
    pyproject_full_path: str = settings.ROOT_PATH_FOR_DYNACONF + "/pyproject.toml"
    with open(
            file=pyproject_full_path,
            mode="r",
            encoding="utf-8"

    ) as f:
        all_data: dict = toml.load(f)
        return all_data["tool"]["poetry"]
