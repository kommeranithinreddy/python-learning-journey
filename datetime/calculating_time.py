from datetime import datetime
#start = 2026-08-16 09:30:00
#end   = 2026-08-16 14:45:30

start = datetime(2026, 8, 16, 9, 30)
end = datetime(2026, 8, 16, 14, 45, 30)

result = end - start

print(result.total_seconds())