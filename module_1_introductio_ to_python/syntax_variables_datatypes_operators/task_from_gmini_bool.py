# Модуль 1 | Вступ до Python
# Тема: Task from gmini bool
# Розглянуто:
# -----------------------------------------------

#Спробуй таке завдання:
#Уяви, що в тебе є has_ticket = True і has_id = False. Напиши умову if, яка надрукує "Вхід дозволено", тільки якщо є і квиток, і паспорт. Зможеш?
has_ticket = True
has_id = False
has_ticket = (input("Do you have a ticket? (yes/no): ").lower() == "yes")
has_id = (input("Do you have a valid ID? (yes/no): ").lower() == "yes")
if has_ticket and has_id:
    print("Вхід дозволено. Ласкаво просимо!")
elif not has_ticket and has_id:
    print("Вхід заборонено: у вас немає квитка.")
elif has_ticket and not has_id:
    print("Вхід заборонено: пред'явіть паспорт.")
else:
    print("Вхід заборонено: у вас немає нічого!")