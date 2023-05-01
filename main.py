temp = str(input('введите температуру: '))
if temp < str(35.5):
    print('низкая')
if temp >= str(35.5) and temp <= str(36.8):
    print("здоров")
if temp >= str(36.8) and temp <= str(37.5):
    print("болен")
if temp >= str(38):
    print("звони в психушку")
