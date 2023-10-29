import obsws_python as obsws

default_config = {
    "host": "localhost",
    "port": 4455,
    "password": "",
    "timeout": None,
}


def launch_obs():
    cl = obsws.ReqClient(**default_config)


if __name__ == '__main__':
    launch_obs()