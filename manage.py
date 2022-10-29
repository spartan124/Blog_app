import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from app import blueprint
from app.main import create_app, db
import click
from flask.cli import FlaskGroup
from dotenv import load_dotenv

load_dotenv() #Loads the .env file

app = create_app(os.getenv("FLASK_ENV", 'development'))
app.app_context().push()
app.register_blueprint(blueprint)
migrate = Migrate(app, db)
cli = FlaskGroup(app)
cli.add_command(MigrateCommand, 'db')


@cli.command('run')
def run():
    app.run(host="0.0.0.0", port=5000)

@cli.command('test')
@click.argument('test_case', default='test*.py')
def test(test_case='test*.py'):
    """run the unit tests"""
    tests = unittest.TestLoader().discover('app/test', pattern=test_case)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


app.cli.add_command(test)

if __name__=="__main__":
    cli()