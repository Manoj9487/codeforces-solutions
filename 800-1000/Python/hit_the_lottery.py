n = int(input())

note_100 = n // 100
note_20 = (n % 100) // 20
note_10 = ((n % 100) % 20) // 10
note_5 = (((n % 100) % 20) % 10) // 5
note_1 = (((n % 100) % 20) % 10) % 5

print(note_100 + note_20 + note_10 + note_5 + note_1)