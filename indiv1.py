#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from mod_ind import s_commands, get_route, display_routes

if __name__ == '__main__':
    routes = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            get_route(routes)

        elif command == 'list':
            display_routes(routes)

        elif command == 'select':
            number2 = input("Выберите номер маршрута: ")
            number3 = int(number2.replace(':', ''))
            count = 0

            for route in routes:
                number1 = route.get('number')
                number1 = int(number1.replace(':', ''))
                if number1 == number3:
                    count += 1
                    print(
                        '{:>4} {} {}'.format("№" + route.get('number'),
                                             route.get('destination', ''),
                                             route.get('time'))
                        )

            if count == 0:
                print("Такие маршруты не найдены")

        elif command == 'help':
            s_commands()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
