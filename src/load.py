import pandas as pd



def load_data_to_supabase(df, table_name, engine):

    try:
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Data loaded successfully into {table_name} table.")
    except Exception as e:
        print(f"Failed to load data: {e}")