text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eget tempus est. Phasellus sit amet 
tristique neque. Sed luctus mi ut nisi suscipit placerat. Nunc nec diam dapibus, fermentum risus ut, ultrices orci. 
Integer non magna molestie nibh dapibus tincidunt. Quisque quis est quam. Sed dictum mi sit amet magna pretium blandit. 
Nulla tortor turpis, maximus vitae lobortis quis, varius sed metus. Nullam at congue metus. Pellentesque scelerisque, dui 
et luctus semper, odio diam scelerisque justo, nec tempor ex metus et enim. Praesent rhoncus nisl eget risus elementum ornare. 
Praesent tellus mauris, viverra vitae malesuada at, ornare id nisi. Vestibulum.""".replace(" ","").lower()
#text = text.replace(" ", "").lower()

most = None
second = None
qty_most_common = second_common = 0

for item in text:
    qty = text.count(item)
    #print(item, qty)           # Для того что бы отследить записанные елементы сразу с кол-м счётчика
    if qty > qty_most_common:
        qty_most_common = qty
        most = item
        print(qty, item)        # Показывает все значения выводимые до макимального по ходу итерации
print(f'Самый частый знак тексте: "{most}"')