import os
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager
from app.models import Role, User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    from flask_migrate import upgrade

    upgrade()

    from app.models import Role

    Role.insert_roles()


if __name__ == '__main__':
    manager.run()
