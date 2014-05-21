from flaskext.auth.permissions import Permission, Role

user_settings = Permission('user', 'super')
user_create = Permission('user', 'create')
user_view = Permission('user', 'view')

roles = {
        'admin': Role('admin', [user_create, user_view, user_settings]),
        'writer': Role('writer', [user_create, user_view]),
        'userview': Role('userview', [user_view]),
}

def load_role(role_name):
        return roles.get(role_name)

auth.load_role = load_role
