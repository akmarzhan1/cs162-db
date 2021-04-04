from .models import *
# file for populating the tables

# creating the data for the offices
office_col = ['id', 'area']
office_data = [
    [1001, 'Karasuno'],
    [1002, 'Fukurodani'],
    [1003, 'Aoba Johsai'],
    [1004, 'Nekoma'],
    [1005, 'Inarizaki'],
    [1006, 'Itachiyama'],
    [1007, 'Shiratorizawa'],
    [1008, 'Date Tech']]

# creating the data for the agents
agent_col = ['id', 'first_name', 'last_name', 'email']
agent_data = [
    [2001, 'Shoyo', 'Hinata', 'hinata@haikyuu.com'],
    [2002, 'Tobio', 'Kageyama', 'kageyama@haikyuu.com'],
    [2003, 'Atsumu', 'Miya', 'atsumu@haikyuu.com'],
    [2004, 'Osamu', 'Miya', 'osamu@haikyuu.com'],
    [2005, 'Toru', 'Oikawa', 'oikawa@haikyuu.com'],
    [2006, 'Wakatoshi', 'Ushijima', 'ushijima@haikyuu.com'],
    [2007, 'Kiyoomi', 'Sakusa', 'sakusa@haikyuu.com'],
    [2008, 'Kotaro', 'Bokuto', 'bokuto@haikyuu.com'],
    [2009, 'Lev', 'Haiba', 'lev@haikyuu.com'],
    [2010, 'Morisuke', 'Yaku', 'yaku@haikyuu.com']]

# creating the data for the sellers
seller_col = ['id', 'first_name', 'last_name', 'email']
seller_data = [
    [3001, 'Akiteru', 'Tsukishima', 'akiteru@gmail.com'],
    [3002, 'Asahi', 'Azumane', 'azumane@gmail.com'],
    [3003, 'Daichi', 'Sawamura', 'daichi@gmail.com'],
    [3004, 'Hajime', 'Iwaizumi', 'iwaizumi@gmail.com'],
    [3005, 'Hitoka', 'Yaichi', 'yaichi@gmail.com'],
    [3006, 'Kei', 'Tsukishima', 'tsukishima@gmail.com'],
    [3007, 'Keiji', 'Akaashi', 'akaashi@gmail.com'],
    [3008, 'Keishin', 'Ukai', 'ukai@gmail.com'],
    [3009, 'Kenma', 'Kozume', 'kenma@gmail.com'],
    [3010, 'Korai', 'Hoshiumi', 'korai@gmail.com'],
    [3011, 'Natsu', 'Hinata', 'hinata@gmail.com'],
    [3012, 'Naoharu', 'Ezota', 'ezota@gmail.com'],
    [3013, 'Rintaro', 'Suna', 'suna@gmail.com'],
    [3014, 'Ryunosuke', 'Tanaka', 'tanaka@gmail.com'],
    [3015, 'Saeko', 'Tanaka', 'saeko@gmail.com'],
    [3016, 'Satoru', 'Tendo', 'tendo@gmail.com']]

# creating the data for the buyers
buyer_col = ['id', 'first_name', 'last_name', 'email']
buyer_data = [
    [4001, 'Shinsuke', 'Kita', 'kita@gmail.com'],
    [4002, 'Reon', 'Ohira', 'reon@gmail.com'],
    [4003, 'Taketora', 'Yamamoto', 'taketora@gmail.com'],
    [4004, 'Tadashi', 'Yamaguchi', 'yamaguchi@gmail.com'],
    [4005, 'Tatsuto', 'Sokolov', 'sokolov@gmail.com'],
    [4006, 'Tetsuro', 'Kuroo', 'kuroo@gmail.com'],
    [4007, 'Wakatsu', 'Kiryu', 'kiryu@gmail.com'],
    [4008, 'Yu', 'Nishinoya', 'nishinoya@gmail.com'],
    [4009, 'Shimizu', 'Kiyoko', 'kiyoko@gmail.com'],
    [4010, 'Yui', 'Michimiya', 'michimiya@gmail.com']]

# creating the data for the houses
house_col = ['id', 'name', 'office_id', 'agent_id', 'seller_id',
             'bedrooms', 'bathrooms', 'price', 'zipcode', 'date', 'sold']
house_data = [
    [5001, 'Kageyama Apartment', 1001, 2001, 3001, 8, 3,
        2900000, 28021, datetime.date(2021, 3, 1), False],
    [5002, 'MSBY Black Jackals Condo', 1001, 2001, 3002, 5, 2,
        150000, 48099, datetime.date(2021, 3, 3), False],
    [5003, 'Tetsuro House', 1002, 2002, 3012, 3, 1,
        90000, 23938, datetime.date(2021, 2, 4), False],
    [5004, 'Johzenji High Dorm ', 1002, 2002, 3010, 4, 1,
        600000, 28021, datetime.date(2021, 2, 6), False],
    [5005, 'Schweiden Adlers Villa', 1002, 2003, 3005, 2, 1,
        300000, 34848, datetime.date(2021, 2, 8), False],
    [5006, 'Sakusa Home', 1003, 2003, 3006, 4, 2,
        48000, 43383, datetime.date(2021, 2, 12), False],
    [5007, 'Daichi San Penthouse', 1003, 2004, 3007, 8, 4,
        360000, 23938, datetime.date(2021, 2, 19), False],
    [5008, 'Hinata House', 1004, 2007, 3008, 4, 2, 700000,
        43737, datetime.date(2021, 3, 3), False],
    [5009, 'Kenma Skyscraper', 1004, 2005, 3009, 12, 4,
        5000000, 28021, datetime.date(2021, 2, 20), False],
    [5010, 'Lev Tower', 1004, 2010, 3003, 5, 3,
        9700000, 48382, datetime.date(2021, 2, 22), False],
    [5011, 'Jujutsu Kaisen Studio', 1005, 2006, 3009, 2, 1,
        100000, 32422, datetime.date(2021, 2, 23), False],
    [5012, 'Miya Twins Tower', 1005, 2006, 3011, 3, 1,
        29000, 48373, datetime.date(2021, 2, 28), False],
    [5013, 'Atsumu Castle', 1005, 2010, 3013, 1, 0, 59000,
        24502, datetime.date(2021, 3, 2), False],
    [5014, 'Osamu Ice Palace', 1006, 2007, 3012, 6, 3,
        320000, 48099, datetime.date(2021, 3, 4), False],
    [5015, 'Asahi Garage', 1006, 2007, 3003, 5, 5,
        30200000, 48729, datetime.date(2021, 3, 7), False],
    [5016, 'Bokuto Sand Castle', 1006, 2008, 3014, 10, 3, 4300000,
        10911, datetime.date(2021, 3, 10), False],
    [5017, 'Akaashi Studio', 1007, 2007, 3016, 3, 1,
        290000, 32422, datetime.date(2021, 3, 15), False],
    [5018, 'Wakatoshi San Condo', 1007, 2009, 3015, 5, 2, 150000,
        23435, datetime.date(2021, 3, 17), False],
    [5019, 'Onigiri Miya Building', 1008, 2009, 3016, 1, 2,
        340000, 48099, datetime.date(2021, 3, 20), False],
    [5020, 'Haikyuu Land', 1008, 2007, 3011, 4, 1, 185000,
        24502, datetime.date(2021, 3, 21), False]]

# dropping all existing tables in the base and creating the updated tables again
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# starting the current session for adding the data
Session = sessionmaker(bind=engine)
session = Session()

# initializing the data
col = [office_col, house_col, agent_col, seller_col, buyer_col]
data = [office_data, house_data,
        agent_data, seller_data, buyer_data]
tables = [Offices, Houses, Agents, Sellers, Buyers]


def add_entries(tables, col, data):
    '''Function for adding the entries from the data into the database.'''
    for value in data:
        item_dict = dict(zip(col, value))
        # **item_dict is a good shortcut for taking the names
        # arguments and inserting them as parameters of the table
        entry = tables(**item_dict)
        session.add(entry)


for i in range(len(tables)):
    add_entries(tables[i], col[i], data[i])

# committing the changes and closing the session
session.commit()


# selling some of the houses and updating the values in a transaction
def sale(house_id, buyer_id, sale_price, sale_date):
    '''
    This transaction does the following:
        - Calculates the commission from selling the house
        - Updates the status of the house if sold 
        - Adds the sale to the Sales table 
    '''

    # querying agent's id corresponding to the house being sold
    agent_id = session.query(Houses.agent_id).filter(
        Houses.id == house_id).first()[0]

    # commissions for the house sale prices
    comparisons = [(sale_price < 100000, 0.01),
                   (sale_price < 200000, 0.075),
                   (sale_price < 500000, 0.06),
                   (sale_price < 1000000, 0.05),
                   (sale_price >= 1000000, 0.04)]

    for comparison in comparisons:
        if comparison[0]:
            comm = comparison[1]

    # storing the commisions from the sale and the sale id in a separate table
    commission = sale_price*comm

    # adding a corresponding entry into the sales
    session.add(Sales(
        house_id=house_id,
        buyer_id=buyer_id,
        sale_price=sale_price,
        sale_date=sale_date))

    # adding a corresponding entry into the commision table
    sale = session.query(Sales.id).filter(
        Sales.house_id == house_id).first()[0]

    session.add(Commission(
        agent_id=agent_id,
        sale_id=sale,
        commission=commission))

    # changing the status of the house to sold
    sold = session.query(Houses).filter(Houses.id == house_id)
    sold.update({Houses.sold: True})

    # committing the changes
    session.commit()


# inserting new data
sold_houses = [
    [5001, 4003, 2800000, datetime.date(2021, 3, 20)],
    [5018, 4005, 150000,  datetime.date(2021, 3, 21)],
    [5002, 4002, 130000, datetime.date(2021, 3, 22)],
    [5009, 4007, 4800000, datetime.date(2021, 3, 23)],
    [5005, 4001, 300000, datetime.date(2021, 3, 24)],
    [5016, 4004, 4100000, datetime.date(2021, 3, 25)],
    [5014, 4004, 360000, datetime.date(2021, 3, 26)],
    [5008, 4002, 700000, datetime.date(2021, 3, 27)],
    [5006, 4001, 45000, datetime.date(2021, 3, 28)],
    [5017, 4003, 9500000, datetime.date(2021, 3, 29)],
    [5011, 4002, 100000, datetime.date(2021, 3, 30)],
    [5003, 4009, 88000, datetime.date(2021, 4, 1)],
    [5019, 4006, 330000, datetime.date(2021, 4, 2)],
    [5007, 4008, 29000, datetime.date(2021, 4, 3)],
    [5004, 4010, 550000, datetime.date(2021, 4, 4)]
]

# putting the corresponding houses on sale and updating the needed tables
for value in sold_houses:
    sale(*value)

session.close()
