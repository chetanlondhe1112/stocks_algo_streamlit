from datetime import datetime
from sqlalchemy import text
import pandas as pd

class sqlmethods:

    def __init__(self,connection_link=str,connection_object=object,username=str):
        self.sql=connection_object
        self.engine=connection_link
        self.tables=self.sql.tables
        self.user=username

    def fetch_tables(self,table_name=str,index_col=None):
        """
            Function to fetch all the data from table
        """
        try:
            df=pd.read_sql_table(table_name,self.engine)
            return df
        except Exception as e:
            print(e)

    def fetch_table_u(self,table_name=str):
        """
            Retrives the tables data w.r.t user
        """
        s="SELECT * FROM `"+table_name+"` WHERE username='"+str(self.user)+"'"
        try:
            df=pd.read_sql_query(s,self.engine)
            return df
        except Exception as e:
            print(e)

    def upload_to_table(self,df=pd.DataFrame(),table_name=str,if_exists=str):
        """
            Uploads dataframe to table
        """
        try:
            df.to_sql(table_name,con=self.engine,if_exists=if_exists,index=0)
            return True
        except Exception as e:
            print(e)

    def fetch_query(self,query=str):
        try:
            return pd.read_sql_query(sql=query,con=self.engine)
        except Exception as e:
            print(e)
            return 0
        
    def update_row(self,table_name=str,update_values=dict,where_col=str,where_col_value=str):
        #sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
        update_string=''
        count=0
        for i,k in update_values.items():
            count+=1
            if count<len(update_values):
                update_string = update_string+str("{} = '{}', ".format(i,k))
            elif count==len(update_values):
                update_string= update_string+str("{} = '{}' ".format(i,k))

        update_q="UPDATE `"+table_name+"` SET "+update_string+" WHERE "+where_col+" = '"+where_col_value+"'"
    
        try:
            self.engine.execute(text(update_q))
            return 1
        except Exception as e:
            print(e)
            return 0
            
    def fetch_customers_names(self):
        try:
            return self.fetch_tables(table_name=self.tables["customer_table"])["name"].drop_duplicates()
        except:
            return 0

    def fetch_customer(self,customer_name=str):
        customer_tbl=self.tables["customer_table"]
        query="SELECT * FROM `"+customer_tbl+"` WHERE name='"+customer_name+"'"
        try:
            return pd.read_sql_query(sql=query,con=self.engine)
        except:
            return 0

    def update_customer(self,update_values=dict,customr_name=str):
        where_col='name'
        return self.update_row(table_name=self.tables["customer_table"],update_values=update_values,where_col=where_col,where_col_value=customr_name)


    def fetch_access_tokens(self,table_name=str):
        """
            To fetch all access tokens
        """
        query_names_q='SELECT id,access_token,createdate FROM `'+ table_name+'`'
        query_names_df=pd.read_sql_query(query_names_q,self.engine,index_col=['id']).drop_duplicates().dropna(axis=1,how='all')
        if len(query_names_df):
            query_names_df=query_names_df.sort_values(by='createdate',ascending=False,ignore_index=True)
            return query_names_df
        else:
            return pd.DataFrame()

    def update_access_token(self,access_token=str,api_key=str,api_secret=str):
        """
            To fetch all access tokens
        """
        current_time=datetime.now()
        table_name=self.tables["access_token_table"]
        df=pd.DataFrame(data={'id':1,'api_key':api_key,'api_secret':api_secret,'access_token':access_token,'createdate':current_time},index=[0])
        df.to_sql(table_name,self.engine,if_exists="replace",index=False)
           
    

    def get_order_log_names(self):
        order_table=self.tables['order_log_table']
        query = "SELECT customerusername FROM '"+order_table+"'"
        return self.fetch_query(query=query)

    def get_order_log(self,username=str,label=None):
        order_table=self.tables['order_log_table']
        if label!="admin":
            s="SELECT * FROM `"+order_table+"` WHERE customerusername='"+str(username)+"'"
            return self.fetch_query(query=s)
        else:
            return self.fetch_tables(order_table)
            
    def delete_row(self,table_name=str,condition=str):
        d="DELETE FROM `"+table_name+"` WHERE '"+condition+"'"
        print(d)
        #try:
        self.engine.execute(text(d))
        #except Exception as e:
        #    print(e)

