import sqlite3


class CrudInterface():
    @staticmethod
    def write_log(user_id, time_game, result_game='defeat', exception=None):
        conn = sqlite3.connect('database/database_log.db')
        cur = conn.cursor()
        request = f"""INSERT INTO db_log(user_id, time_game, result_game, exception)
                      VALUES ('{user_id}', '{time_game}', '{result_game}', '{exception}')"""
        cur.execute(request)
        conn.commit()
        conn.close()

    @staticmethod
    def read_log(list_colums: list[str], list_filters: list[str] = []) -> list:
        conn = sqlite3.connect('database/database_log.db')
        cur = conn.cursor()
        request = f"SELECT {', '.join(list_colums)} "\
                  f"FROM db_log "\
                  f"{('WHERE ' + ' AND '.join(list_filters)) if list_filters else ''}"
        response = cur.execute(request).fetchall()
        conn.close()
        return response


if __name__ == '__main__':
    CrudInterface()