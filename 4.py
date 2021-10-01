years = int(input())
print(years * 365 * 8 * 12)
minutes_spend = int(input()) * 5
years_spend = minutes_spend // (365 * 8 * 60)
minutes_spend = minutes_spend % (365 * 8 * 60)
days_spend = minutes_spend // (8 * 60)
minutes_spend = minutes_spend % (8 * 60)
hours_spend = minutes_spend // 60
minutes_spend %= 60
print('Вы потратите на просмотр экспонатов  ' + str(years_spend) + ' лет '
      + str(days_spend) + ' дней ' + str(hours_spend) + ' часов ' + str(minutes_spend) + ' минут')