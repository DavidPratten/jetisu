# Jetisu
Jetisu is a toolset for modelling with __intensionally defined relations__.
- a "__relation__" is a table with columns and rows,
- "__intensionally defined__" means the the table is defined by computable rules rather than by a list of rows.

Jetisu is understood to be the first implementation of intensionally defined relations. If you are aware of an earlier implementation, please raise an issue.

## Modelling Rules As Code
The examples are chosen to illustrate the benefits (and/or challenges) of using intensionally defined relations to model rules as code.
- [ACT Conveyance Duty](ACT_Conveyance_Duty.ipynb)
- [Australian GST](Australian_GST.ipynb)
- [Birthday Money](Birthday%20Money.ipynb)
- [Australian COVID vaccinations up-to-date and eligibility](COVID_vaccinations.ipynb)
- [Australian COVID vaccinations mandatory for work roles](COVID_vaccinations_and_work.ipynb)
- [Range](Range.ipynb)
## Edit and re-run the example notebooks
You can  ```docker run``` the example Jupyter notebooks for yourself.

```shell
docker run -p 8888:8888 ghcr.io/davidpratten/jetisu:latest
```
Here is help on [How to run the example notebooks](docs/run_notebooks.md) 
## Background to "intensionally defined relations"
Every table has an intension, which is its intended meaning and its extension which is its list of rows. But not all tables 
are defined in the same way!  

| How defined           | Intension (a test that is true if a row is a member of the table) | Extension (list of rows)          |
|-----------------------|-------------------------------------------------------------------|-----------------------------------|
| Extensionally defined | Natural Language                                                  | __Listed out in a table__         |
| Intensionally defined | __Computable Constraints and Rules__                              | Generated or recognised on demand |

The idea of a relation that is defined by computable constraints and rules goes back to the 1970's and 1980's at the beginning of the relational database era. Early references include:

- __Algorithmic relations__ were proposed in 1975 by Patrick Hall, Peter Hitchcock and Stephen Todd. 
- __Computed relations__ were described in 1981 by David Maier and David Warren. 

These proposals share a common assumption that computation is inherently directed. Neither paper suggested that an algorithmic, or computed relation could be defined in such a way that all directions of computation might be possible "out-of-the-box" with just a single definition.

The maturation of satisfaction solvers and of the constraint language [MiniZinc](https://www.minizinc.org) have provided the building blocks for realising ideas that were put forward nearly 50 years ago. The Jetisu project calls these relations, which are algorithmic or computed, "intensionally defined relations".

## Built With Open Source Software
* [sqlglot](https://github.com/tobymao/sqlglot)
* [MiniZinc](https://www.minizinc.org/)
* [OptiMathSAT](https://optimathsat.disi.unitn.it/)
* [Gecode](https://www.gecode.org/)
* [Jupyter](https://jupyter.org/)
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/)

## Acknowledgements
The Jetisu project has been helped along by inspiration from
* [Prolog](https://athena.ecs.csus.edu/~mei/logicp/Programming_in_Prolog.pdf)
* [Tutorial D](https://www.dcs.warwick.ac.uk/~hugh/TTM/)
* [Picat](http://www.picat-lang.org/) 
* [s(CASP)](https://ceur-ws.org/Vol-2970/gdepaper1.pdf)
* [Blawx](https://www.blawx.com/)
* [Catala](https://catala-lang.org/)
