from gino import Gino
from gino.schema import GinoSchemaVisitor

from data import config

# db = Gino()
from loader import db


async def create_db():
	db.gino: GinoSchemaVisitor

	await db.set_bind(config.POSTGRES_URI)
	await db.gino.create_all()

