# rebecka moreno , 2022 

# library imports
import pandas as pd
import numpy as np

#raw data CSV
data1 = pd.read_csv('/Users/rebeckamoreno/Desktop/rawcsvtest.csv', index_col='year')
   
#emissions by unit CSV
data2 = pd.read_csv('/Users/rebeckamoreno/Desktop/emissionscsvtest.csv', index_col='year')   

print(data2.loc[1995]['gas CO'])

#create new emissions csv 
# dflast = pd.DataFrame(datalast, columns= ["year", "gas CO", "gas NOx", "gas PM", "gas SOx", "diesel CO", "diesel NOx", "diesel PM", "diesel SOx", "electric CO", "electric NOx", "electric PM", "electric SOx", "savings CO", "savings NOx", "savings PM", "savings SOx"])
# dflast.to_csv('/Users/rebeckamoreno/Desktop/emissionscalculatedtest.csv')

# #match years and define the emission factors
# def get_gas_emissions():
#     for i in range(len(df1["year"])):
#         for j in range(len(df2["year"])):
#             if df1["year"[i]] = df2["year"[j]]: #if the year matches
#                 Gas_CO = int(df2["gas CO"][j]) #gets the value for CO
#                 Gas_NOx = df2["gas NOx"][j] #gets the value of NOx
#                 Gas_PM10 = df2["gas PM10"][j] #gets the value of PM10
#                 Gas_SOx = df2["gas SOX"][j] #gets the value of SOx

# def get_deez_emissions():
#     for i in range(len(df1["year"])):
#         for j in range(len(df2["year"])):
#             if df1["year"[i]] = df2["year"[j]]: #if the year matches
#                 (Diesel_CO)) = df2["diesel CO"][j] #gets the value for CO
#                 (Diesel_NOx)) = df2["diesel NOx"][j] #gets the value of NOx
#                 (Diesel_PM10)) = df2["diesel PM10"][j] #gets the value of PM10
#                 (Diesel_SOx)) = df2["diesel SOX"][j] #gets the value of SOx

# def get_electric_emissions():
#     for i in range(len(df1["year"])):
#         for j in range(len(df2["year"])):
#             if df1["year"[i]] = df2["year"[j]]: #if the year matches
#                 (int(Electric_CO)) = df2["electric CO"][j] #gets the value for CO
#                 (int(Electric_NOx)) = df2["electric NOx"][j] #gets the value of NOx
#                 (int(Electric_PM10)) = df2["electric PM10"][j] #gets the value of PM10
#                 (int(Electric_Diesel_SOx)) = df2["electric SOX"][j] #gets the value of SOx

# # multiply mileage / gallons by emission factors 
# #def gas_emissions
#     #for i in range (len(df1["mileage"])):
#         #Gas_CO_emissions = mileage * Gas_CO
#     #for j in range (len(df1["mileage"])):
#         #Gas_NOx_emissions = mileage * Gas_NOx
#     #for k in range (len(df1["mileage"])):
#         #Gas_PM_emissions = mileage * Gas_PM10
#     #for l in range (len(df1["gallons"])):
#         #Gas_SOx_emissions = gallons * Gas_SOx

# def deez_emissions
#    for i in range (len(df1["mileage"])):
#         (int(Diesel_CO_emissions)) = mileage * Diesel_CO
#     for j in range (len(df1["mileage"])):
#         (int(Diesel_NOx_emissions)) = mileage * Diesel_NOx
#     for k in range (len(df1["mileage"])):
#         (int(Diesel_PM_emissions)) = mileage * Diesel_PM10
#     for l in range (len(df1["gallons"])):
#         (int(Diesel_SOx_emissions)) = gallons * Diesel_SOx

# def electric_emissions 
#    for i in range (len(df1["mileage"])):
#         (int(Electric_CO_emissions)) = mileage * Electric_CO
#     for j in range (len(df1["mileage"])):
#         (int(Electric_NOx_emissions)) = mileage * Electric_NOx
#     for k in range (len(df1["mileage"])):
#         (int(Electric_PM_emissions)) = mileage * Electric_PM10
#     for l in range (len(df1["gallons"])):
#         (int(Electric_SOx_emissions)) = gallons * Electric_SOx


# # subtract fuel emissions - electric emissions 
# #def gas_savings(): 
#     #for i in range(len(dflast["gas CO"])):
#         #if Gas_CO > 0:
#             #CO_Saved = Gas_CO_emissions - Gas_Electric_CO_emissions
#     #for j in range(len(dflast["gas NOx"])):
#         #if Gas_Nox > 0:
#             #NOx_Saved = Gas_NOx_emissions - Gas_Electric_NOx_emissions
#     #for k in range(len(dflast["gas PM"])):
#         #if Gas_PM > 0:
#             #PM_Saved = Gas_PM_emissions - Gas_Electric_PM_emissions
#     #for l in range(len(dflast["gas SOx"])):
#         #if Gas_SOx > 0:
#             #SOs_Saved = Gas_SOx_emissions - Gas_Electric_SOx_emissions


# # I can do this manually in CSV if needed 
# def deez_savings(): 
#     for i in range(len(dflast["diesel CO"])):
#         if diesel_CO > 0:
#             (int(CO_Saved)) = (int(Diesel_CO_emissions)) - (int(Diesel_Electric_CO_emissions))
#     for j in range(len(dflast["diesel NOx"])):
#         if diesel_Nox > 0:
#             (int(NOx_Saved)) = (int(Diesel_NOx_emissions)) - (int(Diesel_Electric_NOx_emissions))
#     for k in range(len(dflast["diesel PM"])):
#         if diesel_PM > 0:
#             (int(PM_Saved)) = (int(Diesel_PM_emissions)) - (int(Diesel_Electric_PM_emissions))
#     for l in range(len(dflast["diesel SOx"])):
#         if diesel_SOx > 0:
#             (int(SOs_Saved)) = (int(Diesel_SOx_emissions)) - (int(Diesel_Electric_SOx_emissions))






# # document export
#     # vehicle 
#     # year
#     # fuel type
#     # mileage
#     # gallons 
#     # kWh equivalent 
#     # fuel CO 
#     # fuel NOx 
#     # fuel PM 
#     # fuel SOx 
#     # electric CO 
#     # electric NOx
#     # electric PM 
#     # electric SOx 
#     # subtracted CO 
#     # subtracted NOx 
#     # subtracted PM 
#     # subtracted SO

