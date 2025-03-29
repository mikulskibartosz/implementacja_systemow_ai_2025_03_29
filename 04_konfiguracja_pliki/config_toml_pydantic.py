import tomllib
from pydantic import BaseModel
from typing import List, Dict, Union
from datetime import datetime

class Owner(BaseModel):
    name: str
    dob: datetime

class Database(BaseModel):
    enabled: bool
    ports: List[int]
    data: List[List[Union[str, float]]]
    temp_targets: Dict[str, float]

class Server(BaseModel):
    ip: str
    role: str

class Servers(BaseModel):
    alpha: Server
    beta: Server

class Config(BaseModel):
    title: str
    owner: Owner
    database: Database
    servers: Servers

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

config = Config(**config)

print(config)
