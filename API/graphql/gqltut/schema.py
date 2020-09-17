import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime()


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


schema = graphene.Schema(query=Query)
# or schema = graphene.Schema(query=Query, auto_camelcase=False)
# to keep camel case

results = schema.execute(
        '''
        {
            users(first: 2) {
                username
                lastLogin
            }
        }
        '''
)

items = dict(results.data.items())
print(json.dumps(items, indent=4))
