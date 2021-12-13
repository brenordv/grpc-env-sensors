# -*- coding: utf-8 -*-
from core.environment import ENV_VARS
from core.settings import SECRETS_FILE

print(SECRETS_FILE)
print(SECRETS_FILE.exists())
print(ENV_VARS)
