base_andpoint = 'http://localhost:81'


class UsersEndPoints():
    LIST_USERS = f'{base_andpoint}/api/users/'
    USER_REGISTRATION = f'{base_andpoint}/api/users/'
    USER_PROFILE = f'{base_andpoint}/api/users/1/'
    INVALIDE_USER_PROFILE = f'{base_andpoint}/api/users/99/'
    USER_TOKEN = f'{base_andpoint}/api/auth/token/login/'
    CURRENT_USER = f'{base_andpoint}/api/users/me/'
    CHANGING_PASSWORD = f'{base_andpoint}/api/users/set_password/'
    DELETE_TOKEN = f'{base_andpoint}/api/auth/token/logout/'


class TagsEndPoints():
    LIST_TAGS = 'http://localhost/api/tags/'
    TAGS_NOT_FOUND = 'http://localhost/api/tags/99/'


class RecipesEndPoints():
    RECIPES_LIST = 'http://localhost/api/recipes/'
    GET_RECIPE = 'http://localhost/api/recipes/32/'


class IngredientsEndPoints():
    INGREDIENTS_LIST = 'http://localhost/api/ingredients/'


class ShoppingCartEndPoints():
    DOWNLOAD_SHOPPING_CART = 'http://localhost/api/recipes/download_shopping_cart/'


class SubscriptionEndPoints():
    MY_SUBSCRIPTION = 'http://localhost/api/users/subscriptions/'