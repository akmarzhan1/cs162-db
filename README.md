# DB Application

This project is done as part of the Database Assignment for CS162 course. It targets on building a database system for a large franchised real estate company. We make use of SQLAlchemy and Python with concepts, such as data normalization, indices and transactions.

## Installation

You can access the program by running the following lines in your terminal from the root directory:

```python
python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt

python3 run.py
```

You should see the output from the program with the answers to the 6 prompts like the following:

screenshot

## Architecture

```
path/cs162-db
├── app/
│   ├── data.py
│   ├── models.py
│   └── query.py
├── README.md
├── requirements.txt
└── run.py
```

- models.py imports the required libraries and created the database architecture with the needed tables.
- data.py adds hypothetical data to the database and adds entries to the sold houses.
- query.py runs all of the queries from the prompts and makes sure the answers are given in an understandable format.
- requirements.txt has all the needed dependencies.
- run.py imports the program and runs it.

## Database

The database consists of several tables, such as:

- Agents: keeps the information about estate agents
- Offices: keeps the information about offices
- Sellers: keep the information about house sellers
- Buyers: keeps the information about house buyers
- Houses: keeps the information about the houses for sale
- Sales: keeps the information about all existing sales (i.e., houses that are sold)
- Commissions: keeps the information about how much estate agents who sold houses get as part of the commission

## Data Normalization

### 1NF (1st Normal Form)

This normal form is about eliminating repeating groups. In the database for real estate agency:

- There are no repeating groups of columns.
- Each column contains an atomic value (every attribute is single-valued).
- The relation doesn't contain composite (i.e., a minimal set of attributes that consists of two or more attributes that uniquely identify an entry) or multi-valued attributes.
- Each record is unique.
- The order in which the data is stored doesn't matter.

### 2NF (2nd Normal Form)

This normal form is about removing partial dependency. Given that the first normal form is satisfied, all the non-key columns depend on the table's primary key (i.e., a unique identifier for the whole row).

### 3NF (3rd Normal Form)

This part is about ensuring no transitive dependency for the non-prime attributes. A transitive functional dependency happens when changing a non-key column leads to any of the other non-key columns changing. All of our tables except for `Commissions` one are in 3NF since the `Commissions` table has a column `sale_id` which defines both the `agent_id` and the `commission` (depending on the selling price of the house) for that specific sale.

I first normalized all of the data and then used **denormalization** to avoid costly joins and make the querying easier. I could have simply added the total commission for an agent, but there is ambiguity in when and for what the commission was given. Also, querying the total from the current denormalized table is very easy, and the structure is more convenient. For example, if we only had the total commission and agent id, and we calculate the report each month, suppose there is a bug, and the program calculates the commission twice in a single month. Then, the program wouldn’t know whether it already calculated the commission for a given month or for given sold houses, which is why it could add it the second time if it doesn’t recheck and do the process all over again. That is why it is convenient to know which sales the entries correspond to so that it would be easy to navigate in case of malfunctions without having to perform the original queries from scratch (especially given that these will be calculated each month for every agent).

I also didn’t create a separate table for defining the commission quotas as for a small app like this with only a few commission options, it is much easier to just do the logic in python instead of referencing and joining many tables (i.e., also the query will look much nicer and easier).

## Transactions

Operations in SQLAlchemy are done as parts of transactions (i.e., sequences of operations completed as a single logical unit). Transactions are very convenient because they either commit the changes altogether or rollback to the database's original state. By creating and starting a session, we start the transaction. By using `add_all` we add the data that we need and by committing the session, we commit the changes to the database and end the transaction. At this point, before the commit, if anything goes wrong, the transaction will be aborted and the database will be rolled back.

Database transactions guarantee data validity despite malfunctions and are ACID:

- **atomicity**: update all-or-nothing;
- **consistency**: \*\*\*\*database always in consistent state, everybody sees the data the same;
- **isolation:** execution of transactions concurrently will result in a state that is equivalent to a state achieved these were executed serially in some order;
- **durability:** data never lost, updates and modifications to the database are stored in and written to disk and they persist even if a system failure occurs.

## Indexing

As far as I understand, SQLite has an automatic indexing feature from version 3.7.17, which allows doing lookups on non-indexed columns, assuming that generating a temporary index is cheaper than doing a raw lookup. Thus, all queries are automatically optimized. We can also consider primary keys that we defined as indices since the index is simply an ordered structure used to find an entry in $O(log(n))$ complexity (lookup in a BST). Table scan, on the other hand, has $O(n)$ complexity.

The app is very small at this point, which is why additional considerations weren't necessary. However, I acknowledge that if there are many more entries, there would be a need for faster querying as it would take a lot of time to compile reports. If we wanted to manually add indices to some columns to have predefined access to them, we can use the `index_property` from `sqlalchemy.ext.indexable`.
