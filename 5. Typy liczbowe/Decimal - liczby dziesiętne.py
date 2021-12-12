# Liczby Dziesiętne (DECIMAL) - liczby o stałej precyzji
print( 0.1 + 0.1 + 0.1 - 0.3)  # za mała liczba bitów żeby reprezentować dokładne wartości
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))  # Domyślnie jest drukowane 28 cyfr
decimal.getcontext().prec = 4  # Ustalenie stałej precyzji ( cztery miejsca po przecinku ).
print(decimal.Decimal(1) / decimal.Decimal(7))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
decimal.getcontext().prec = 28
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print(decimal.Decimal('1.00') / decimal.Decimal('3.0'))
with decimal.localcontext() as ctx:  # ustawienie preczji dla konkretnego zadania
    ctx.prec = 2
    print(decimal.Decimal('1.0') / decimal.Decimal('3.00000'))
print(decimal.Decimal('1.000') / decimal.Decimal('3.00000000000'))  # wartość precyzji pozostaję jak przed zadaniem