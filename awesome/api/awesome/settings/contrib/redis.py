from ..environment import env


REDIS_URL = env.str("AWESOME_REDIS_URL", default="redis://127.0.0.1:6379/2")
