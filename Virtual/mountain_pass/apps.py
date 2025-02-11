from django.apps import AppConfig
from flask import Flask
from flasgger import Swagger


class MountainPassConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mountain_pass'

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Получить список пользователей
    ---
    responses:
      200:
        description: Список пользователей
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              name:
                type: string
              email:
                type: string
    """
    return [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}
    ]

@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Создать нового пользователя
    ---
    parameters:
      - name: user
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      201:
        description: Пользователь создан
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
    """
    return {"id": 3, "name": "New User", "email": "newuser@example.com"}, 201

if __name__ == '__main__':
    app.run(debug=True)
