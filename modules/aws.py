from configparser import ConfigParser
from pathlib import Path
import os


def create_file():
    config_object = ConfigParser()
    config_object.read("config.ini")
    aws = config_object["AWS"]
    access_key_id = aws["access-key-id"]
    secret_access_key = aws["secret-access-key"]
    default_region = aws["default-region"]
    default_output = aws["default-output"]
    OS_USER = os.getenv("USER")
    Path(f'/home/{OS_USER}/.aws/').mkdir(parents=True, exist_ok=True)
    Path(f'/home/{OS_USER}/.aws/credentials').touch(mode=0o666, exist_ok=True)
    Path(f'/home/{OS_USER}/.aws/config').touch(mode=0o666, exist_ok=True)
    p_credentials = Path(f'/home/{OS_USER}/.aws/credentials')
    p_config = Path(f'/home/{OS_USER}/.aws/config')

    p_credentials_text = f"[default]\naws_access_key_id={access_key_id}\naws_secret_access_key={secret_access_key}\n"

    p_config_text = f"[default] \nregion={default_region}\noutput={default_output}\n"

    p_credentials.write_text(p_credentials_text)
    p_config.write_text(p_config_text)
