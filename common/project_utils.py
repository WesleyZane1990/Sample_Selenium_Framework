from __future__ import annotations

import os
from dotenv import load_dotenv

def get_run_ci() -> bool:
    run_ci = os.getenv("RUN_CI", "")
    return run_ci.strip().lower() in {"1", "true", "yes", "on"}


if not get_run_ci() and not load_dotenv():
    raise FileNotFoundError("Error: .env file was not found in the project root")


def get_user_name() -> str:
    user_name = os.getenv("PROJECT_USERNAME")
    if not user_name:
        raise RuntimeError("Set PROJECT_USERNAME")

    return user_name


def get_password() -> str:
    password = os.getenv("PROJECT_PASSWORD")
    if not password:
        raise RuntimeError("Set PROJECT_PASSWORD")

    return password


def get_url() -> str:
    base_url=os.getenv("PROJECT_URL")

    return base_url if base_url.endswith("/") else f"{base_url}/"

# def get_options() -> list[str]:
#     options = os.getenv("BROWSER_OPTIONS_CHROME")
#     if not options:
#         raise RuntimeError("Set BROWSER_OPTIONS_CHROME")
#
#     return [option.strip() for option in options.split(";") if option.strip()]


def get_browser() -> str:
    browser_name = os.getenv("BROWSER_NAME")
    if browser_name !='chrome':
        raise ValueError(f"Unsupported browser {browser_name}.Only 'Chrome' is project browser")

    return browser_name
