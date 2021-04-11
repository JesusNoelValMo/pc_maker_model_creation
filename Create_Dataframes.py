import pymysql
def get_data():
    conn = pymysql.connect(
        host='pcmakerinstance.c15oncijbytw.us-east-2.rds.amazonaws.com',
        port=int(3306),
        user="admin",
        passwd="password",
        db="dbname",
        )
    cursor=conn.cursor()
    conn.connect()
    try:
      cursor.execute("SELECT * FROM dbname.low_req_pcbenchmark")
      rows_low_pcgamebenchmark = cursor.fetchall()
    
      cursor.execute("SELECT * FROM dbname.rec_req_pcbenchmark")
      rows_rec_pcgamebenchmark = cursor.fetchall()
    
      return rows_low_pcgamebenchmark, rows_rec_pcgamebenchmark
    finally:
    
        conn.close()
        
        