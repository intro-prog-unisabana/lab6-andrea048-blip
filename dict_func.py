# Write your code here!
def employee_print(employee_info):
    # Imprimir datos base (con N/A si no existen)
    print(f"Name: {employee_info.get('Name', 'N/A')}")
    print(f"Salary: {employee_info.get('Salary', 'N/A')}")
    print(f"Role: {employee_info.get('Role', 'N/A')}")

    # Copiar el diccionario para no modificar el original
    extra_info = employee_info.copy()

    # Eliminar las claves base
    extra_info.pop("Name", None)
    extra_info.pop("Salary", None)
    extra_info.pop("Role", None)

    # Imprimir información extra o mensaje si no hay
    if len(extra_info) == 0:
        print("No other info!")
    else:
        for key, value in extra_info.items():
            print(f"{key}: {value}")