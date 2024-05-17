import csv
import os
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
ctx = Context()

mod.list("conda_command", desc="conda commands.")

mod.list("conda_argument", desc="Command-line conda options and arguments.")

dirpath = Path(__file__).parent
arguments_csv_path = str(dirpath / "conda_arguments.csv")
commands_csv_path = str(dirpath / "conda_commands.csv")


@mod.capture(
    rule="({user.vocabulary} | {user.punctuation} | {user.prose_snippets} | <phrase> | <user.prose_number>)+"
)
def environment_name(m) -> str:
    """the name for an environment formatted with dashes"""
    return "-".join(m.split(" "))