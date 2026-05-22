import sys


def print_state(lst, tpl):
    print(f"\nТекущий список:  {lst} -> размер: {sys.getsizeof(lst)} байт")
    print(f"Текущий кортеж: {tpl} -> размер: {sys.getsizeof(tpl)} байт")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

initial_size = sys.getsizeof(my_list)
print_state(my_list, my_tuple)

answer = input("\nхочешь изменить список? (да/нет): ").strip().lower()

if answer == "да":
    user_input = input("сколько чисел добавить в список? ").strip()

    try:
        count_to_add = int(user_input)

        if count_to_add <= 0:
            print("введи число больше 0.")
        else:
            start_num = 10
            for i in range(start_num, start_num + count_to_add):
                my_list.append(i)
            new_size = sys.getsizeof(my_list)
            difference = new_size - initial_size

            print("\nРЕЗУЛЬТАТ ИЗМЕНЕНИЯ")
            if len(my_list) > 20:
                print(
                    f"новый список: {my_list[:10]} ... [...еще {len(my_list)-15} элементов...] ... {my_list[-5:]}"
                )
            else:
                print(f"новый список: {my_list}")

            print(f"Итого элементов в списке: {len(my_list)}")
            print(f"Новый размер списка: {new_size} байт")
            print(f"Разница с первоначальным списком: +{difference} байт")

    except ValueError:
        print("ошибка: нужно было ввести целое число!")
else:
    print("\nпрограмма завершена. Размер остался прежним.")
