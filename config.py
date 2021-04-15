from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQBiXQqWpvUfM_cv7EvnEaiWKCZs9F6ev5br2VZT-pQMoXMEPIHK-X6eTGwCZPSqVYoVJUx0DvMFse0xcx9v1m1W9XL-pQQkfFh6ho-NBVHGnuMa7w5MSWYa4PulJwk3lwrdiSGK1D-g_qTEnigt2RSq4sY7qtP6mFMKMb2kw-Iu8phu7Z1kzK9-4MAaH-MP2X4UjHH_XR059ShsjzXrYEXCYGh8ti3lSrLFpcUM7nL_5MGsNBH9aR5fAtuLBXJa5A8dkH43Q716p6Hq0BCbKB0w58AELvFol9PGoHstK-HSLt7rav5AlDFupPZuO0pVIyfhp60zHLc0juRBY4C--fo6Ufz5XgA")
BOT_TOKEN = getenv("1770742430:AAGvQrvV0Xjl-0tP1Zk3l7QO5pDoyApeYtk")

API_ID = int(getenv("1497153"))
API_HASH = getenv("172fa7f3478006318afd0c2bf0757647")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1492186775").split()))
