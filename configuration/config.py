import pandas as pd
import sqlalchemy
import tomlkit

with open("tls_config.toml", mode="rt",encoding="utf-8") as toml:
    config=tomlkit.load(toml)

print(config)
