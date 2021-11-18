import cx_Oracle

connection = None
cursor = None

TABLE_QUERY = """
    SELECT * FROM USER_OBJECTS WHERE OBJECT_TYPE='TABLE'
"""
MAIN_MENU = """
    What are you looking for?
    1. Computer
    2. Television
    3. Price update
    4. Exit
"""
COMPUTER_MENU = """
    - Computer -
    1. Product list
    2. Recommended products
    3. Back
"""
TELEVISION_MENU = """
    - Television -
    1. Search by price
    2. Recommended products
    3. Back 
"""


def create_computer():
    cursor.execute(
        """
    CREATE TABLE computer (
        name varchar2(21) UNIQUE,
        price number,
        type varchar2(1),
        cpu number,
        feature varchar2(20)
    )"""
    )


def create_television():
    cursor.execute(
        """
    CREATE TABLE television(
        name varchar2(21) UNIQUE,
        price number,
        type varchar2(1),
        screen_size number
    )"""
    )


def create_global_schema():
    tables = [table[0] for table in cursor.execute(TABLE_QUERY)]
    if "COMPUTER" not in tables:
        create_computer()
        print("Table computer has been created")
    if "TELEVISION" not in tables:
        create_television()
        print("Table television has been created")


def get_values(table, column):
    query = f"SELECT {column} FROM {table}"
    values = [row[0] for row in cursor.execute(query)]
    return values


def combine_computer_values():
    for company_A in ["desktop", "laptop"]:
        model_values = get_values(company_A, "model")
        price_values = get_values(company_A, "price")
        cpu_values = get_values(company_A, "cpu")
        row_counts = len(cpu_values)
        type_values = (
            ["L"] * row_counts if company_A == "laptop" else ["D"] * row_counts
        )
        feature_values = (
            get_values(company_A, "weight")
            if company_A == "laptop"
            else ["none"] * row_counts
        )
        values = [
            ["A" + row1, row2, row3, row4, row5]
            for row1, row2, row3, row4, row5 in zip(
                model_values, price_values, type_values, cpu_values, feature_values
            )
        ]
        cursor.executemany(
            "INSERT INTO computer (name, price, type, cpu, feature) VALUES (:1, :2, :3, :4, :5)",
            values,
        )
        connection.commit()

    for company_B in ["pc", "server"]:
        model_values = get_values(company_B, "model")
        code_values = get_values(company_B, "code")
        price_values = get_values(company_B, "price")
        cpu_values = get_values(company_B, "cpu")
        row_counts = len(cpu_values)
        type_values = (
            get_values(company_B, "type") if company_B == "pc" else ["S"] * row_counts
        )
        feature_values = ["none"] * row_counts
        values = [
            ["B" + row1 + row2, row3, row4, row5, row6]
            for row1, row2, row3, row4, row5, row6 in zip(
                model_values,
                code_values,
                price_values,
                type_values,
                cpu_values,
                feature_values,
            )
        ]
        cursor.executemany(
            "INSERT INTO computer (name, price, type, cpu, feature) VALUES (:1, :2, :3, :4, :5)",
            values,
        )
        connection.commit()


def combine_television_values():
    for company_A in ["HDTV", "PDPTV", "LCDTV"]:
        model_values = get_values(company_A, "model")
        price_values = get_values(company_A, "price")
        screen_size_values = get_values(company_A, "screen_size")
        row_counts = len(price_values)
        if company_A == "HDTV":
            type_values = ["H"] * row_counts
        elif company_A == "PDPTV":
            type_values = ["P"] * row_counts
        else:
            type_values = ["L"] * row_counts
        values = [
            ["A" + row1, row2, row3, row4]
            for row1, row2, row3, row4 in zip(
                model_values, price_values, type_values, screen_size_values
            )
        ]
        cursor.executemany(
            "INSERT INTO television (name, price, type, screen_size) VALUES (:1, :2, :3, :4)",
            values,
        )
        connection.commit()

    for company_B in ["TV"]:
        model_values = get_values(company_B, "model")
        code_values = get_values(company_B, "code")
        price_values = get_values(company_B, "price")
        screen_size_values = get_values(company_B, "screen_size")
        type_values = get_values(company_B, "type")
        values = [
            ["B" + row1 + row2, row3, row4, row5]
            for row1, row2, row3, row4, row5 in zip(
                model_values, code_values, price_values, type_values, screen_size_values
            )
        ]
        cursor.executemany(
            "INSERT INTO television (name, price, type, screen_size) VALUES (:1, :2, :3, :4)",
            values,
        )
        connection.commit()


def table_preparation():
    create_global_schema()
    try:
        combine_computer_values()
        print("Values have combined to Table computer")
    except cx_Oracle.IntegrityError:
        print("Table computer already has its values")
    try:
        combine_television_values()
        print("Values have combined to Table television")
    except cx_Oracle.IntegrityError:
        print("Table television already has its values")


def show_computer_list_by_query(query):
    strFormat = "%-10s%-10s%-10s%-10s%-10s\n"
    computer_strOut = strFormat % ("name", "price", "type", "cpu", "feature")
    computer_strOut += "-" * len(computer_strOut) + "\n"
    for row in cursor.execute(query):
        computer_strOut += strFormat % row
    print(computer_strOut)


def show_television_list_by_query(query):
    strFormat = "%-10s%-10s%-10s%-10s\n"
    television_strOut = strFormat % ("name", "price", "type", "screen_size")
    television_strOut += "-" * len(television_strOut) + "\n"
    for row in cursor.execute(query):
        television_strOut += strFormat % row
    print(television_strOut)


def computer_menu():
    print(COMPUTER_MENU)
    selection = "0"
    while selection not in ["1", "2", "3"]:
        selection = input("Enter: ")
        if selection == "1":
            show_computer_list_by_query("SELECT * FROM computer ORDER BY name")
        elif selection == "2":
            show_computer_list_by_query(
                """
                SELECT * FROM computer 
                WHERE (price < (SELECT AVG(price) FROM computer WHERE name LIKE 'A%')) 
                AND
                (cpu > (SELECT AVG(cpu) FROM computer WHERE name LIKE 'A%')) 
                AND
                (name LIKE 'A%')
                UNION
                SELECT * FROM computer 
                WHERE (price < (SELECT AVG(price) FROM computer WHERE name LIKE 'B%')) 
                AND
                (cpu > (SELECT AVG(cpu) FROM computer WHERE name LIKE 'B%')) 
                AND
                (name LIKE 'B%')
            """
            )
        elif selection == "3":
            call_user_interface()
        else:
            print("Invalid input")


def search_television_by_price():
    price = input("Enter price: ")
    price = int(price)
    show_television_list_by_query(
        f"""
        SELECT * FROM television
        WHERE ABS(price - {price}) = (SELECT MIN(ABS(price - {price})) FROM television)
        ORDER BY name
    """
    )


def television_menu():
    print(TELEVISION_MENU)
    selection = "0"
    while selection not in ["1", "2", "3"]:
        selection = input("Enter: ")
        if selection == "1":
            search_television_by_price()
        elif selection == "2":
            show_television_list_by_query(
                """
                SELECT * FROM television 
                WHERE (price < (SELECT AVG(price) FROM television)) 
                AND
                (screen_size > (SELECT AVG(screen_size) FROM television)) 
                ORDER BY (screen_size / price) DESC
            """
            )
        elif selection == "3":
            call_user_interface()
        else:
            print("Invalid input")


def price_update():
    cursor.execute(
        """
        UPDATE computer SET 
        price = price * 0.9
        WHERE (cpu < (SELECT AVG(cpu) FROM computer))
    """
    )
    cursor.execute(
        """
        UPDATE television SET 
        price = price * 1.1
        WHERE screen_size = (SELECT MAX(screen_size) FROM television)
    """
    )
    cursor.execute(
        """
        DELETE FROM television 
        WHERE (screen_size/price) = (SELECT MAX(screen_size/price) FROM television)
    """
    )
    connection.commit()


def call_user_interface():
    print(MAIN_MENU)
    selection = "0"
    while selection not in ["1", "2", "3", "4"]:
        selection = input("Enter: ")
        if selection == "1":
            computer_menu()
        elif selection == "2":
            television_menu()
        elif selection == "3":
            price_update()
            print("Price updated")
            call_user_interface()
        elif selection == "4":
            pass
        else:
            print("Invalid input")

    cursor.execute("DROP TABLE computer")
    cursor.execute("DROP TABLE television")
    print("Bye!")
    exit()


def login():
    global connection
    global cursor
    user = input("user: ")
    password = input("password: ")
    try:
        connection = cx_Oracle.connect(
            user=user, password=password, dsn="localhost:1521"
        )
    except cx_Oracle.DatabaseError as e:
        print(e)
        exit()
    print("Successfully connected to Oracle Database")
    cursor = connection.cursor()


def main():
    login()
    table_preparation()
    call_user_interface()


if __name__ == "__main__":
    main()
