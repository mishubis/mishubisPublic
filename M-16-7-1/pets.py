from cats import Cat

cats = [
    {
        "name": "Пушинка",
        "gender": "девочка",
        "age": "1 год"
    },
    {
        "name": "Сэм",
        "gender": "мальчик",
        "age": "2 года"
    },
    {

        "name": "Снежок",
        "gender": "мальчик",
        "age": "4 года"
    }
]

print("Коты: ")

for cat in cats:
    cat_object = Cat()
    cat_object.init_from_dict(cat)
    cat_object.display()

# Старый вариант
# for cat in cats:
#    cat_object = Cat(name=cat.get("name"),
#                     gender=cat.get("gender"),
#                     age=cat.get("age"))
#    cat_object.display()

