age = int(input())

years = age // 365
age_rest = age % 365
months = age_rest // 30
days = age_rest % 12

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
