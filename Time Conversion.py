seconds = int(input())
minutes = int(seconds / 60)
seconds = seconds % 60
hours = int(minutes / 60)
minutes = minutes % 60
print(f"{hours}:{minutes}:{seconds}")