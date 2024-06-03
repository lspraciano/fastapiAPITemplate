import os

from dynaconf import Dynaconf, Validator

APP_ENV_VAR_PREFIX: str = "FASTAPITEMPLATE"
current_dir: str = os.path.dirname(__file__)
root: str = os.path.abspath(
    os.path.join(
        current_dir,
        os.pardir,
    )
)

settings: Dynaconf = Dynaconf(
    root_path=root,
    envvar_prefix=APP_ENV_VAR_PREFIX,
    settings_files=[
        "./configuration/settings.toml",
        "./configuration/.secrets.toml"
    ],
    environments=[
        "production",
        "development",
        "testing"
    ],
    env_switcher=f"{APP_ENV_VAR_PREFIX}_APP_RUNNING_MODE",
    validators=[
        Validator(
            names="APP_RUNNING_MODE",
            must_exist=True,
        )
    ],
    load_dotenv=False,
    sysenv_fallback=True
)
