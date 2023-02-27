
import mysql.connector

class OpMySql ():
    def __init__(self):
        self.__mydb = mysql.connector.connect( host="127.0.0.1", user="root",  password="", database="ehkaam")


    def add_row_single(self ,name_tb ,name_cell ,value):
        cursor = self.__mydb.cursor()

        try:

            name_ce = self.return_name_call(name_cell)


            lenw = len(name_cell) - 1
            qu = "%s," * lenw
            qu = qu + "%s"



            sql = f'INSERT INTO {name_tb}({name_ce}) values ({qu})'

            cursor.execute(sql, value)

            self.__mydb.commit()
            return cursor.lastrowid
        except  :

           return 0
        finally:
            cursor.close()


    def close_mysql(self):
        self.__mydb.close()
    def add_row_multi(self ,name_tb ,name_cell ,value):
        'Mysql.add_row_multi("tb_test",["v1"],[("a","a")])'
        'Mysql.add_row_multi("tb_test",["v1"],[("a")])'
        cursor = self.__mydb.cursor()

        try:

            name_ce = self.return_name_call(name_cell)


            lenw = len(name_cell) - 1
            qu = "%s," * lenw
            qu = qu + "%s"



            sql = f'INSERT INTO {name_tb}({name_ce}) values ({qu})'
            # print(sql)
            # print(value)
            cursor.executemany(sql, value)

            self.__mydb.commit()
            return cursor.rowcount
        except  :

           return 0
        finally:
            cursor.close()
           # self.__mydb.close()



    def up_row(self ,name_tb ,name_cell ,value ,terms ,condition_value):
        'Mysql.up_row("tb_test",["v1"],["102"],["Id"],["102"])'
        cursor = self.__mydb.cursor()

        try:

            v_set = ""
            arr = []
            for x in range(len(name_cell)):

                if v_set == "":
                    x2 = name_cell[x] + " = %s"
                    arr.append(value[x])
                    v_set = x2
                else:
                    x2 = name_cell[x] + " = %s"
                    arr.append(value[x])
                    v_set = v_set + " , " + x2

            v_where = ""

            for x in range(len(terms)):

                if v_where == "":

                    x2 = " WHERE " + terms[x] + " = %s"
                    arr.append(condition_value[x])
                    v_where = x2


                else:

                    x2 = terms[x] + " = " + " %s "
                    arr.append(condition_value[x])
                    v_where = v_where + " AND " + x2

            sql = f"UPDATE {name_tb} SET {v_set} {v_where}"

            # print(sql)

            cursor.execute(sql, arr)

            self.__mydb.commit()
            return cursor.rowcount
        except:

            return 0
        finally:
            cursor.close()
            # self.__mydb.close()

    def delete_row(self, name_tb, terms, condition_value):
        cursor = self.__mydb.cursor()

        try:

            arr = []

            v_where = ""

            for x in range(len(terms)):

                if v_where == "":

                    x2 = " WHERE " + terms[x] + " = %s"
                    arr.append(condition_value[x])
                    v_where = x2


                else:

                    x2 = terms[x] + " = " + " %s "
                    arr.append(condition_value[x])
                    v_where = v_where + " AND " + x2

            sql = f"DELETE FROM {name_tb} {v_where}"

            cursor.execute(sql, arr)

            self.__mydb.commit()
            return cursor.rowcount
        except:

            return 0
        finally:
            cursor.close()
        # self.__mydb.close()

    def return_name_call(self, name_call):
        tx = ""
        for x in name_call:
            if tx == "":
                tx = x
            else:
                tx = tx + "," + x

        return tx

    def get_row(self, name_tb, terms=[], condition_value=[], filter=" * "):
        cursor = self.__mydb.cursor(dictionary=True)

        try:

            arr = []

            v_where = ""

            for x in range(len(terms)):

                if v_where == "":

                    x2 = " WHERE " + terms[x] + " = %s"
                    arr.append(condition_value[x])
                    v_where = x2


                else:

                    x2 = terms[x] + " = " + " %s "
                    arr.append(condition_value[x])
                    v_where = v_where + " AND " + x2

            sql = f"SELECT {filter} FROM {name_tb} {v_where}"
            # print(sql)
            cursor.execute(sql, arr)

            self.__mydb.commit()
            return cursor.fetchall()
        except:

            return cursor.fetchall()
        finally:
            cursor.close()
            # self.__mydb.close()
