import os
import psycopg

url = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(url) as connection:
        while True:
            consulta = input("\nEscribe una query SQL (o 'salir' para terminar): ").strip()

            if consulta.lower() == "salir":
                print("Saliendo...")
                break

            if not consulta:
                continue

            try:
                with connection.cursor() as cur:
                    cur.execute(consulta)

                    if cur.description is not None:
                        filas = cur.fetchall()
                        for fila in filas:
                            print(fila)
                    else:
                        connection.commit()
                        print("Consulta ejecutada correctamente.")
            except Exception as err_sql:
                connection.rollback()
                print("Error en la query:", err_sql)
except Exception as e:
    print("Error de conexión:", e)
    raise