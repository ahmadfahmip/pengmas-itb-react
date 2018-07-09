from flask import request
from flask_restful import Resource
from Model import db, Lembaga, LembagaSchema

lembagas_schema = LembagaSchema(many=True)
lembaga_schema = LembagaSchema()

class LembagaResource(Resource):
    def get(self):
        lembagas = Lembaga.query.all()
        lembagas = lembagas_schema.dump(lembagas).data
        return {'status': 'success', 'data': lembagas}, 200
    
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = lembaga_schema.load(json_data)
        if errors:
            return errors, 422
        lembaga = Lembaga.query.filter_by(name=data['name']).first()
        if lembaga:
            return {'message': 'Lembaga already exists'}, 400
        lembaga = Lembaga(
            name = json_data['name'],
            category = json_data['category']
        )

        db.session.add(lembaga)
        db.session.commit()

        result = lembaga_schema.dump(lembaga).data

        return {'status':'success', 'data':result}, 201
    
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = lembaga_schema.load(json_data)
        if errors:
            return errors, 422
        lembaga = Lembaga.query.filter_by(id=data['id']).first()
        if not lembaga:
            return {'message': 'Lembaga does not exists'}, 400
        lembaga.name = data['name']
        db.session.commit()

        result = lembaga_schema.dump(lembaga).data

        return {'status':'success', 'data':result}, 204
    
    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = lembaga_schema.load(json_data)
        if errors:
            return errors, 422
        lembaga = Lembaga.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = lembaga_schema.dump(lembaga).data

        return {'status':'success', 'data':result}, 204


class LembagaSingleResource(Resource):
    def get(self, id):
        try:
            lembaga = Lembaga.find_by_id(id)
        except:
            return {'error': 'An error occured'}, 500
        if not lembaga:
            return {'message': 'Lembaga does not exists'}, 400
        return lembaga.json()
        # lembaga, errors = Lembaga.find_by_id(id)
        # if errors:
        #     return errors, 422
        # if not lembaga:
        #     return {'message': 'Lembaga does not exists'}, 400
        # return {'status': 'success', 'data': lembaga}, 200
    
    # def post(self):
    #     json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    #     # Validate and deserialize input
    #     data, errors = lembaga_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #     lembaga = Lembaga.query.filter_by(name=data['name']).first()
    #     if lembaga:
    #         return {'message': 'Lembaga already exists'}, 400
    #     lembaga = Lembaga(
    #         name = json_data['name'],
    #         category = json_data['category']
    #     )

    #     db.session.add(lembaga)
    #     db.session.commit()

    #     result = lembaga_schema.dump(lembaga).data

    #     return {'status':'success', 'data':result}, 201
    
    # def put(self):
    #     json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    #     # Validate and deserialize input
    #     data, errors = lembaga_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #     lembaga = Lembaga.query.filter_by(id=data['id']).first()
    #     if lembaga:
    #         return {'message': 'Lembaga does not exists'}, 400
    #     lembaga.name = data['name']
    #     db.session.commit()

    #     result = lembaga_schema.dump(lembaga).data

    #     return {'status':'success', 'data':result}, 204
    
    # def delete(self):
    #     json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    #     # Validate and deserialize input
    #     data, errors = lembaga_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #     lembaga = Lembaga.query.filter_by(id=data['id']).delete()
    #     db.session.commit()

    #     result = lembaga_schema.dump(lembaga).data

    #     return {'status':'success', 'data':result}, 204