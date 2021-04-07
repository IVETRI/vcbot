from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQAcURkZCkP1Yc7mhhUXLd0JkU_06nmwxz0E8WFkBCJxi5_nln0Efz4o9gMVCkltLJybq-3Mn-HESQ_jU-QAKNw6eO5dJNvHZLtqo9wzcRaRWxfRQ8o6uqXG_SdEmMmIbZlQ8UTjcr46WnzIDMiLG6mGf6GOj_J7aS17DobuOI2TQq4DT3I-bB8rQJjOYQ2TjIeiaVqNasvOpRRZK64nHCpcbe0sVe_cEREIrz4gEVMJmhMZiuSpFEV_0FcCnKNHYC2OqV3p7PxnY263de9rfKEqum46mjT2z6ViedxfbEKE1bTI64ElnBf2PkP7d_EcqMpSsv3KdTHYX-UX4wR_zpQXUfz5XgA")
BOT_TOKEN = getenv("1770742430:AAGvQrvV0Xjl-0tP1Zk3l7QO5pDoyApeYtk")

API_ID = int(getenv("1497153"))
API_HASH = getenv("172fa7f3478006318afd0c2bf0757647")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1492186775").split()))
