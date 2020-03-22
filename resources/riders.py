from db import db
from sqlalchemy import text
from flask_restful import Resource
from models.store import StoreModel


class RidersList(Resource):
    def get(self):
        sql = text('select name from items')
        result = db.engine.execute(sql)
        names = [row[0] for row in result]
        print (names)
        return {'names': names}

