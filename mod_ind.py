def s_commands():
    print("Список команд:\n")
    print("add - добавить маршрут;")
    print("list - вывести список маршрутов;")
    print("select - нати маршруты по времени")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def get_route(routes):
    destination = input("Пункт назначения: ")
    number = input("Номер поезда: ")
    time = input("Время отправления: ")

    route = {
        'destination': destination,
        'number': number,
        'time': time
    }
    routes.append(route)
    if len(routes) > 1:
        routes.sort(key=lambda item: item.get('destination', ''))


def display_routes(road):
    if road:
        line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 30,
                '-' * 4,
                '-' * 20
        )
        print(line)
        print(
                '| {:^30} | {:^4} | {:^20} |'.format(
                    "Пункт назначения",
                    "№",
                    "Время"
                                            )
        )
        print(line)

        for route in road:
            print(
                '| {:<30} | {:>4} | {:<20} |'.format(
                    route.get('destination', ''),
                    route.get('number', ''),
                    route.get('time', '')
                )
            )
        print(line)

    else:
        print("Поезда не найдены")
