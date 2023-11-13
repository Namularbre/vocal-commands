env: dict = {}
with open('.env') as dotenv:
    for line in dotenv.readlines():
        key, value = line.split('=')
        value = value.replace("\"", "").strip()
        env[key.strip()] = value
