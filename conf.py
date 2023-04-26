from environ import environ


env = environ.Env()
environ.Env.read_env()


FILENAME_TASKS = env.str('TASKS')
FILENAME_BUILDS = env.str('BUILDS')
