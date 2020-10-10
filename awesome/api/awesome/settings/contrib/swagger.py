from ..environment import env


SWAGGER_SETTINGS = {
    "DEFAULT_API_URL": env.str("AWESOME_BASE_API_URL", default="https://example.com"),
}
