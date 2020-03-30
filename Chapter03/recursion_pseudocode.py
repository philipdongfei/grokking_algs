def look_for_key(main_box):
    """loops are sometimes better for performance.
    'Loops may achieve a performance gain for your program.
    Recursion may achieve a performance gain for your programmer.
    Choose which is more import in your situation!'--Leigh Caldwell"""
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")
                return item

def look_for_key(box):
    """this code is clearer to me"""
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key!")
            return item
