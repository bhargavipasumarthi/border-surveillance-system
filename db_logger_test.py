from db_logger import log_event

log_event(
    99,
    "Test Intrusion",
    "HIGH"
)

print("Database logging works")