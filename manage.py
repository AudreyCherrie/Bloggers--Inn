from app import create_app,db
from flask_script import Manager,Server
from app.models import Writer,Subscribe,Post,Comments
from flask_migrate import Migrate,MigrateCommand

app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)
migrate =Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,Writer=Writer,Subscribe =Subscribe,Post=Post,Comments=Comments)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
