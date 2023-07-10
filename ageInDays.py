Days = int(input())
Years = int(Days / 365)
Days = int(Days % 365)
Months = int(Days / 30)
Days = Days % 30
print(Years, "ano(s)")
print(Months, "mes(es)")
print(Days, "dia(s)")