from datetime import datetime, timezone

now1 = datetime.now()
print(now1)
print(now1.tzinfo)
now2 = datetime.now(timezone.utc)
print(now2)
print(now2.tzinfo)