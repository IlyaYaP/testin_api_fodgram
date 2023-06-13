class UsersData():
    USER_REGISTRATION_DATA = {
                                "email": "vpupki@nyandex.ru",
                                "username": "vasya.pupkin",
                                "first_name": "Вася",
                                "last_name": "Пупкин",
                                "password": "Qwerty12asd3"
                                }

    INVALID_USER_REGISTRATION_DATA = {
                                "email": "vpupkiyandex.ru",
                                "username": "vasya. pupkin",
                                "first_name": "Вася!)(*(№;))",
                                "last_name": "Пупкин",
                                "password": "Qwerty12asd3"
                                }

    LOGIN_USER_TOKEN_DATA = {

                            "password": "Qwerty12asd3",
                            "email": "vpupki@nyandex.ru"

                            }
    INVALID_LOGIN_USER_TOKEN_DATA = {

                            "password": "Qwerty2asd3",
                            "email": "vpupki@nyandex.ru"

                            }
    
    CHANGING_PASSWORD_DATA = {

                        "new_password": "Awerty2asd3",
                        "current_password": "Qwerty12asd3"

                        }
    
    RETURN_CHANGING_PASSWORD_DATA = {

                        "new_password": "Qwerty12asd3",
                        "current_password": "Awerty2asd3"

                        }
   
    INVALIDE_CHANGING_PASSWORD_DATA = {

                        "new_password": "Awerty2asd3"

                        }
    RECIPE_CREATE_DATA = {
                        "ingredients": [{"id": 22,
                                        "amount": 2}],

                        "tags": [1],
                        "image": "data:image/jpeg;base64",
                        "name": "test recipe",
                        "text": "description test recipe",
                        "cooking_time": 1

                        }
                    


# {'count': 1, 
#  'next': None, 
#  'previous': None, 
#  'results': 
#         [{'id': 1, 
#         'tags': [{'id': 1, 
#                     'name': 'Завтрак', 
#                     'color': '#00FA9A', 
#                     'slug': '1'}], 
#                     'author': {'id': 1, 
#                                 'email': 'admin@admin.ru', 
#                                 'username': 'admin', 
#                                 'first_name': 'admin', 
#                                 'last_name': 'admin', 
#                                 'is_subscribed': False}, 
#                     'ingredients': [], 
#                     'is_favorited': False, 
#                     'is_in_shopping_cart': False, 
#                     'name': 'test_recipe', 
#                     'image': 'http://localhost/media/recipes/images/rick-and-morty-cartoon-characters-adventure-wallpaper-2880x1800_8.jpg', 
#                     'text': 'description test recipe', 
#                     'cooking_time': 20}]}