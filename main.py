import Create_Dataframes
import joblib
import pipeline
import transformers
import model_manage
def main():
    
    
    df_low, df_rec = Create_Dataframes.create_dataframes("low_req_pcbenchmark", "rec_req_pcbenchmark")
    transformed_df = model_manage.Create_New_Transformers(df_low)
    model_manage.Create_New_Model(transformed_df, 7, "test_model")

    
    
    #new_instance_low = [['887', 'BioShock Infinite', 'Indebted to the wrong people with his life on the line veteran of the U S Cavalry and now hired gun Booker DeWitt has only one opportunity to wipe his slate clean He must rescue Elizabeth a mysterious girl imprisoned since childhood and locked up in the flying city of Columbia ', ' Windows Vista Service Pack 2 32-bit', ' Intel Core 2 Duo Q6867', ' 2 GB', '', '', ' 20 GB', ""]]
    #instance_transformed = pipeline.transform_input(new_instance_low)
    #print(instance_transformed.shape)
    
if __name__ == '__main__':
    main()
