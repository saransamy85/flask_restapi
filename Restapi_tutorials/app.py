from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)


class video(Resource):
    def get(self):
        ram={"name":"saravanan","RollNo":"39"}
        return ram


api.add_resource(video,"/")

if __name__=='__main__':
    app.run(debug=True)

