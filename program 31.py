import pandas as pd
num = [1234,6544,7097,3556,9063]
name = ['maruti','toyota','audi','ferrari','benz']
cost = ['100K','200K','1000K','100M','5B']
fuel = ['electric','diesel','gas','petrol','gas']
mil = ['400','421','120','540','150']
cardata = pd.DataFrame({'plate number':num,'carname':name,'carcost':cost,'carfuel':fuel,'milage':mil})
print(cardata)