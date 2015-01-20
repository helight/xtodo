#!Python
# -*- coding: utf-8 -*-
import sys
import sqlite3

create_sql = "CREATE TABLE xtodo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status int NOT NULL, time TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP)"

con = sqlite3.connect('todo.db')
con.execute("drop table if exists xtodo")
con.execute(create_sql)
con.commit()
con.close()
print "init db ok"
