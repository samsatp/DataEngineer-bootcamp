import os
import pandas as pd
from sqlalchemy import create_engine
import argparse


def ingestion(args):
    data_url = args.data_url
    user = args.user
    password = args.password
    host = args.host
    port = args.port
    db_name = args.db_name
    table_name = args.table_name

    # dowload data
    os.system(f'wget {data_url} -O output.csv')

    # data iter
    df_iter = pd.read_csv("output.csv", iterator=True, chunksize=30)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

    for i, df in enumerate(df_iter):
        df.to_sql(name = table_name, con=engine, if_exists='append')
        print(f'inserting batch: {i}')
    
    print('Done')





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True)
    parser.add_argument('--password', required=True)
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', required=True)
    parser.add_argument('--db_name', required=True)
    parser.add_argument('--table_name', required=True)
    parser.add_argument('--data_url', required=True)

    args = parser.parse_args()

    ingestion(args)