from .models import *

# initializing a new session
Session = sessionmaker(bind=engine)
session = Session()

# the month of interest - March so far
month, year = 3, 2021
month_name = datetime.datetime.strptime(str(month), "%m").strftime("%B")

print("REPORT FOR {} {}".format(month_name, year))
print("")
print('1. Top 5 offices with the most sales for {}.'.format(month_name))
print("")

query = session.query(
    # querying the area (instead of office id since it is more understandable) and the count of sales
    Offices.area,
    func.count(Houses.office_id)
).join(
    # joining the Sales and Office tables
    Sales, Offices
).filter(
    # only considering the sold houses, and if the date corresponds to March 2021
    Houses.sold == True,
    func.extract('month', Sales.sale_date) == month,
    func.extract('year', Sales.sale_date) == year
).group_by(
    # grouping by office id since we want to find the most sales by office
    Houses.office_id
).order_by(func.count(Houses.office_id).desc()).limit(5).statement

# returning the information in an understandable format
# could have also simply returned a table pd.read_sql(query, session.bind)
print(pd.read_sql(query, session.bind))
print("")
data = pd.read_sql(query, session.bind)
for index in range(5):
    print("{}. {} with the sale count of {}.".format(
        index+1, data['area'][index], data['count_1'][index]))
print("")
print("")

print('2. Find the top 5 estate agents who have sold the most in {}.', month_name)
print("")

query = session.query(
    # querying the needed info to congratulate the agents
    Agents.first_name,
    Agents.last_name,
    Agents.email,
    func.count(Houses.agent_id)
).join(Sales, Agents).filter(
    # making sure that the house is sold and the timing is March 2021 (time the house was sold)
    Houses.sold == True,
    func.extract('month', Sales.sale_date) == month,
    func.extract('year', Sales.sale_date) == year
).group_by(
    # grouping by agent
    Houses.agent_id
).order_by(func.count(Houses.agent_id).desc()).limit(5).statement

# returning the information in an understandable format
# could have also simply returned a table pd.read_sql(query, session.bind)
print(pd.read_sql(query, session.bind))
print("")
data = pd.read_sql(query, session.bind)
for index in range(5):
    print("{}. {} {} ({}) had a sale count of {}.".format(
        index+1, data['first_name'][index], data['last_name'][index], data['email'][index], data['count_1'][index]))
print("")
print("")

print('3. Calculate the commission that each estate agent must receive and store the results in a separate table.')
print("")

query = session.query(
    # querying the agents with their corresponding commissions
    # the commissions from each sale have been already added
    Commission.agent_id,
    Agents.first_name,
    Agents.last_name,
    Agents.email,
    func.sum(Commission.commission)
).join(Agents, Sales).filter(
    # making sure the entries from the correct time are shown
    func.extract('month', Sales.sale_date) == month,
    func.extract('year', Sales.sale_date) == year
).group_by(Commission.agent_id).order_by(func.sum(Commission.commission).desc()).statement

# returning the information in an understandable format
# could have also simply returned a table pd.read_sql(query, session.bind)
print(pd.read_sql(query, session.bind))
print("")
data = pd.read_sql(query, session.bind)
for index, _ in enumerate(data.iterrows()):
    print("{} {} ({}) should get a total of ${} in commissions.".format(
        data['first_name'][index], data['last_name'][index], data['email'][index], data['sum_1'][index]))
print("All other agents not mentioned would get 0 in commissions.")
print("")
print("")

print('4. For all houses that were sold in {}, calculate the average number of days that the house was on the market.'.format(month_name))
print("")

query = session.query(
    # querying the needed data (listing date, sale date)
    Houses.name,
    Houses.date,
    Sales.sale_date
).join(Sales).filter(
    # making sure the house is sold and the time is right
    Houses.sold == True,
    func.extract('month', Sales.sale_date) == month,
    func.extract('year', Sales.sale_date) == year
).statement

# returning the information in an understandable format
print(pd.read_sql(query, session.bind))
data = pd.read_sql(query, session.bind)
difference = []
for index, _ in enumerate(data.iterrows()):
    difference.append((data['sale_date'][index]-data['date'][index]).days)
print("")
print("On average, the houses were on the market for {} days (rounded).".format(
    round(np.mean(difference))))
print("")
print("")

print('5. For all houses that were sold in {}, calculate the average selling price.'.format(month_name))
print("")

query = session.query(
    # querying the required information
    Houses.name,
    Sales.sale_price
).join(Sales).filter(
    # making sure the house is sold in the right time
    Houses.sold == True,
    func.extract('month', Sales.sale_date) == month,
    func.extract('year', Sales.sale_date) == year
).statement

average = session.query(
    # querying the average selling price
    func.avg(Sales.sale_price)
).filter(
    func.extract('month', Sales.sale_date) == month,
    func.extract('year', Sales.sale_date) == year
).one()

# returning the information in an understandable format
print(pd.read_sql(query, session.bind))
print("")
print('On average, houses were sold at ${} (rounded) during {}.'.format(round(
    average[0]), month_name))
print("")
print("")


print('6. Find the zip codes with the top 5 average sales prices.')
print("")

query = session.query(
    # querying the zip codes and average house prices
    Houses.zipcode,
    func.avg(Houses.price),
).join(Sales).filter(
    # making sure the house is sold in the right time
    Houses.sold == True,
    func.extract('month', Sales.sale_date) == month,
    func.extract('year', Sales.sale_date) == year
).group_by(Houses.zipcode).order_by(func.avg(Houses.price).desc()).limit(5).statement

# returning the information in an understandable format
print(pd.read_sql(query, session.bind))
print("")
data = pd.read_sql(query, session.bind)
for index in range(5):
    print("{}. Houses with zipcode {} had an average sale price of ${}.".format(
        index+1, data['zipcode'][index], round(data['avg_1'][index])))
print("")
print("")

session.close()
