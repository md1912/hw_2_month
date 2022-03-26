from environs import Env

env = Env()
env.read_env()

many = env.int("MY_MONEY")
