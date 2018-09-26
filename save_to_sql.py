# _*_ coding:UTF-8 _*_
'''
Created on Mar 7, 20172:06:13 PM
Author: VIC
Email: victor.wei@msn.cn
Link: http://www.weizhikai.com

'''

import pymysql
import config
from pymysql import cursors

class sqloperater:
    def __init__(self, sqlstr):
        super().__init__()
        self.sqlstr = sqlstr
        self.status = ''
        
    # drop existed table
    def drop_table(self, sqlstr):
        connection = pymysql.connect(host=config.HOST,
                                     user=config.USER,
                                     password=config.PASSWORD,
                                     db=config.DATABASE,
                                     charset=config.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        try:
            with connection.cursor() as cursor:
                cursor.execute(self.sqlstr)
                connection.commit()
                self.status = 'Table dropped Sucessfully'
        except Exception as e:
            self.status = 'Failed to drop Table', str(e)

    # create new table
    def create_table(self, sqlstr):
        connection = pymysql.connect(host=config.HOST,
                                     user=config.USER,
                                     password=config.PASSWORD,
                                     db=config.DATABASE,
                                     charset=config.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        try:
            with connection.cursor() as cursor:
                cursor.execute(self.sqlstr)
                connection.commit()
                self.status = 'Table created Sucessfully'
        except Exception as e:
            self.status = 'Failed to Create Table', str(e)
            
    # add data to table       
    def AddData(self, sqlstr):
        connection = pymysql.connect(host=config.HOST,
                                     user=config.USER,
                                     password=config.PASSWORD,
                                     db=config.DATABASE,
                                     charset=config.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor)
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(self.sqlstr)
                connection.commit()
                self.status = 'Added Successfully'
        except Exception as e:
           self.status = 'Failed to Add', str(e)
        
        finally:
            connection.close()
        
    # bulk-action for adding data to table
    def AddManyData(self, sqlstr):
        connection = pymysql.connect(host=config.HOST,
                                     user=config.USER,
                                     password=config.PASSWORD,
                                     db=config.DATABASE,
                                     charset=config.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor)
        
        try:
            with connection.cursor() as cursor:
                cursor.executemany(self.sqlstr)
                connection.commit()
                self.status = 'Added Successfully'
        except Exception as e:
           self.status = 'Failed to Add', str(e)
        
        finally:
            connection.close()
            
    # update data in the table
    def updateData(self, sqlstr):
        connection = pymysql.connect(host=config.HOST,
                                     user=config.USER,
                                     password=config.PASSWORD,
                                     db=config.DATABASE,
                                     charset=config.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        try:
            with connection.cursor() as cursor:
                cursor.execute(sqlstr)
                connection.commit()
                self.status = 'Updated Successfully'
        except Exception as e:
            self.status = 'Failed to Update', str(e)
        finally:
            connection.close()
    
    # delete data from the table
    def deleteData(self, sqlstr):
        connection = pymysql.connect(host=config.HOST,
                                     user=config.USER,
                                     password=config.PASSWORD,
                                     db=config.DATABASE,
                                     charset=config.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        try:
            with connection.cursor() as cursor:
                cursor.execute(sqlstr)
                connection.commit()
                self.status = 'Deleted Successfully'
        except Exception as e:
            self.status = 'Failed to Delete ', str(e)
        finally:
            connection.close()
    
    # read data from table
    def fetchOneData(self, sqlstr):
        connection = pymysql.connect(host=config.HOST,
                                     user=config.USER,
                                     password=config.PASSWORD,
                                     db=config.DATABASE,
                                     charset=config.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        try:
            with connection.cursor() as cursor:
                cursor.execute(sqlstr)
                self.sqldata = cursor.fetchone()
                self.status = 'Fetch Data Successfully'
        except Exception as e:
            self.status = 'Failed to Fetch Data ', str(e)
            self.sqldata = []
        finally:
            connection.close()
            
            
    # read all data from table    
    def fetchAllData(self, sqlstr):
        connection = pymysql.connect(host=config.HOST,
                                     user=config.USER,
                                     password=config.PASSWORD,
                                     db=config.DATABASE,
                                     charset=config.CHARSET,
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        try:
            with connection.cursor() as cursor:
                cursor.execute(sqlstr)
                self.sqldata = cursor.fetchall()
                self.status = 'Fetch Data Successfully'
        except Exception as e:
            self.status = 'Failed to Fetch Data ', str(e)
            self.sqldata = []
        finally:
            connection.close()
            
    # retrun execution status    
    def get_status(self):
        return self.status
    
    # return data
    def get_data(self):
        return self.sqldata
    
    # read and save data to a file 
    def sql_to_set(self, sqlstr):
        sqlreader = sqloperater(sqlstr)
        sqlreader.fetchAllData(sqlstr)
        data = sqlreader.get_data()
        for i in range(len(data)):
            print(data[i])
    
    
'''
sqlstr = "delete from `aepro`.`db_aecategories`;"
saver = sqloperater(sqlstr)
saver.deleteData(sqlstr)
print(saver.get_status())
'''
