# Jetisu
Jetisu is a toolset for modelling with __intensionally defined relations__.
- a "__relation__" is a table with columns and rows,
- "__intensionally defined__" means the the table is defined by computable rules rather than by a list of rows.

## Modelling Rules As Code
The examples are chosen to illustrate the benefits (and/or challenges) of using intensionally defined relations to model rules as code.
- [ACT Conveyance Duty](ACT_Conveyance_Duty.ipynb)
- [Australian GST](Australian_GST.ipynb)
- [Birthday Money](Birthday%20Money.ipynb)
- [Range](Range.ipynb)
## Edit and re-run the example notebooks
You can  ```docker run``` the example Jupyter notebooks for yourself.

```shell
docker run XXXXXXXXXXX
```
## Unpacking "intensionally defined"
Every table has an intension, which is its intended meaning and its extension which is its list of rows. But not all tables 
are defined in the same way!  

| How defined           | Intension (a test that is true if a row is a member of the table) | Extension (list of rows)          |
|-----------------------|-------------------------------------------------------------------|-----------------------------------|
| Extensionally defined | Natural Language                                                  | Listed out in a table             |
| Intensionally defined | Computable Constraints and Rules                                  | Generated or recognised on demand |

Our databases and CRMs are full of extensionally defined tables, here are a few:

| Intension (intended meaning) | Extension (list of rows)           |
|------------------------------|------------------------------------|
| Our Customers                | 1 row in a table for each customer |
| Our Orders                   | 1 row in a table for each order    |

