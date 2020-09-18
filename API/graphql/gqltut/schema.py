import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())
    
    # is_staff = graphene.Boolean()
    # or is_staff = graphene.Boolean(name='is_staff) to keep camel case

    def resolve_users(self, info, first):
        return [
            User(username='Ntombi', last_login=datetime.now()),
            User(username='Sizwe', last_login=datetime.now()),
            User(username='Nonhle', last_login=datetime.now())
        ][:first]

class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.String()
    
    user = graphene.Field(User)

    def mutate(self, info, username):
        if info.context.get('is_vip'):
            username = username.upper()
        user = User(username=username)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
# or schema = graphene.Schema(query=Query, auto_camelcase=False)
# to keep camel case

results = schema.execute(
        '''
        mutation createUser($username: String) {
            createUser(username: $username) {
                user {
                    username
                }
            }
        }
        ''',
        variable_values = {'username': 'Alice'},
        context = {'is_vip': True}
)

items = dict(results.data.items())
print(json.dumps(items, indent=4))
