# ***Project*** &nbsp; → &nbsp; **0x0F. Python - Object-relational mapping** <br />
***Scope*** &nbsp; → &nbsp; ` Python ` ` OOP ` ` SQL ` ` MySQL ` ` ORM ` ` SQLAlchemy ` <br />

* ## ***Tasks***
* **[0. Get all states](./0-select_states.py)** &nbsp; → &nbsp; a script that lists all `states` from the database `hbtn_0e_0_usa` .
* **[1. Filter states](./1-filter_states.py)** &nbsp; → &nbsp; a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa` .
* **[2. Filter states by user input](./2-my_filter_states.py)** &nbsp; → &nbsp; a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
* **[3. SQL Injection...](./3-my_safe_filter_states.py)** &nbsp; → &nbsp; a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument and safe from MySQL injections.
* **[4. Cities by states](./4-cities_by_state.py)** &nbsp; → &nbsp; a script that lists all `cities` from the database `hbtn_0e_4_usa`
* **[5. All cities by state](./5-filter_cities.py)** &nbsp; → &nbsp; a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`
* **[6. First state model](./model_state.py)** &nbsp; → &nbsp; a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`
* **[7. All states via SQLAlchemy](./7-model_state_fetch_all.py)** &nbsp; → &nbsp; a script that lists all `State` objects from the database `hbtn_0e_6_usa`
* **[8. First state](./8-model_state_fetch_first.py)** &nbsp; → &nbsp; a script that prints the first `State` object from the database `hbtn_0e_6_usa`
* **[9. Contains `a`](./9-model_state_filter_a.py)** &nbsp; → &nbsp; a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`
* **[10. Get a state](./10-model_state_my_get.py)** &nbsp; → &nbsp; a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
* **[11. Add a new state](./11-model_state_insert.py)** &nbsp; → &nbsp; a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`
* **[12. Update a state](./12-model_state_update_id_2.py)** &nbsp; → &nbsp; a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`
* **[13. Delete states](./13-model_state_delete_a.py)** &nbsp; → &nbsp; a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`
* **[14. Cities in state (Model)](./14-model_city_fetch_by_state.py)** &nbsp; → &nbsp; a script that prints all `City` objects from the database `hbtn_0e_14_usa`
* **[14. Cities in state (Script)](./model_city.py)** &nbsp; → &nbsp; a Python file that contains the class definition of a `City` and inherits from `Base` (imported from `model_state`)
