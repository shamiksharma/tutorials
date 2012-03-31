server_port = 8080
token = "PUT_TOKEN_HERE"

try:
    import local_config   # I put real token="..." here and dont check in (.gitignore)
except ImportError:
    pass
