# Jetisu

<img align="right" width="100" height="100" src="images/jetisu_logo.png">

Jetisu is a toolset for modelling with __sigma complete relations__.
- a "__relation__" is a table with columns and rows,
- "__sigma complete__" means the table started its life complete and has been shaped by a relational algebraic σ operator (`WHERE` clause).

To use an artisanal metaphor complete relations are like a raw block of stone. The `WHERE` clause is like the sculptor's hammer that shapes a stature. And the sigma complete relation is like the finished statue that represents any computable relation.

## Doing for computation and business rules what the relational model did for data
Prior to the advent of the relational model, programmers' mental model of data spanned multiple levels of abstraction and required them to procedurally navigate either hierarchies or networks to access data. The relational model challenged this approach and provided a stable and robust mental model of data for programmers to use (Schemas and Relational Queries).  

The Jetisu Toolkit is exploring the possibility that the relational model can do for computation and business logic what it did for data. And provide programmers with a way to specify computations and business logic without the need for procedural code. The following diagram is a representation of what this might look like:

<img width="100%" src="images/doing for rules what rm did for data.png">

## Puzzle Examples
- [Family Age Gaps](puzzles/family_age_gaps.md)

## Rules As Code Examples
The examples are chosen to illustrate the benefits (and/or challenges) of using sigma complete relations to model rules as code.
- [ACT Conveyance Duty](ACT_Conveyance_Duty.ipynb)
- [Australian GST](Australian_GST.ipynb)
- [Birthday Money](Birthday%20Money.ipynb)
- [Australian COVID vaccinations up-to-date and eligibility](COVID_vaccinations.ipynb)
- [Australian COVID vaccinations mandatory for work roles](COVID_vaccinations_and_work.ipynb)
- [Eligibility for rates subsidy](eligible_for_rates_subsidy.ipynb)
- [Range](Range.ipynb)

## Interactive Q&A with Rules as Code
This example shows interactive Q&A using the same rule-set as the above "Australian COVID vaccinations mandatory for work roles" example:
- [Am I required to have COVID vaccinations?](Goal_seeking_covid_vaccination_and_work.ipynb)

## Edit and re-run the example notebooks
You can  ```docker run``` the example Jupyter notebooks for yourself.

```shell
docker run -p 8888:8888 ghcr.io/davidpratten/jetisu:latest
```
Here is help on [How to run the example notebooks](docs/run_notebooks.md) 
## Background to "sigma complete relations"
Let's compare regular data relations with sigma complete relations. 

|                                                          | __Data Relations__                                                                                              | __Sigma Complete Relations__                                  |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| __Purpose__                                              | Capture data about entities of interest                                                                         | Do computation and implement business rules                   |
| __Consists of a rows (tuples) and columns (attributes)__ | Yes                                                                                                             | Yes                                                           |
| __When created the table is__                            | Empty                                                                                                           | Complete<br> (full, containing every possible row)            
| __Specific table is created by__                         | Rows are inserted, updated and removed using Data Manipulation Statements (DML) `INSERT`, `UPDATE`, and `DELETE` | The relation is shaped using constraints in a `WHERE` clause. |
| __Is it a constant value in the database?__              | No                                                                                                              | Yes                                                           |
| __Holds data about entities of interest__                | Yes | No |
| __Discipline which has focused on these__                | Relational Database community                                                                                   | Constraint Programming community                              |


### Computed or Algorithmic Relations
The idea of a relation that is defined by constraints and rules goes back to the 1970's and 1980's at the beginning of the relational database era. Early references include:

- __Algorithmic relations__ proposed in 1975 by Patrick Hall, Peter Hitchcock and Stephen Todd (hereafter HHT). [(PDF)](https://dl.acm.org/doi/pdf/10.1145/512976.512998) 
- __Computed relations__ described in 1981 by David Maier and David Warren (hereafter MW). [(PDF)](https://dl.acm.org/doi/pdf/10.1145/582318.582345)

### Constraint Programming
From the late 1980s the discipline of Constraint Programming CP and Constraint Logic Programming CLP emerged and begin to explore what it took to define a relation as a computable predicate over the cross product of the domains of attributes. Here is a survey of this work and a key reference for the constraint programming language [MiniZinc](https://www.minizinc.org):

- __Constraint Logic Programming: A Survey.__ (1994) J. Jaffar, Michael J. Maher [(PDF)](https://www.sciencedirect.com/science/article/pii/0743106694900337?via%3Dihub)
- __MiniZinc: Towards a Standard CP Modelling Language.__ (2007) N. Nethercote, Peter James Stuckey, Ralph Becket, S. Brand, Gregory J. Duck, Guido Tack [(SpringerLink PDF)](https://link.springer.com/chapter/10.1007/978-3-540-74970-7_38)

The two ideas of computed and algorithmic relations put together with constraint logic programming are foundations of what the Jetisu toolkit calls: "sigma complete relations".

## A formal definition of sigma complete relations

An __sigma complete relation__ is 
- a set of typed attributes (or columns) ```A```, along with
- a computable predicate (or constraint) ```P``` over the attributes in ```A```, 
- and has the value given by the following relational algebraic expression:

```σP(dom(a1) × dom(a2) × … × dom(aN)) for predicate P and typed attributes a1, a2, …, aN ∈ A.```


## Built With Open Source Software
* [sqlglot](https://github.com/tobymao/sqlglot)
* [MiniZinc](https://www.minizinc.org/)
* [OptiMathSAT](https://optimathsat.disi.unitn.it/)
* [Gecode](https://www.gecode.org/)
* [Jupyter](https://jupyter.org/)
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/)

## Acknowledgements
The Jetisu toolkit has been helped along by inspiration from
* [Prolog](https://athena.ecs.csus.edu/~mei/logicp/Programming_in_Prolog.pdf)
* [Tutorial D](https://www.dcs.warwick.ac.uk/~hugh/TTM/)
* [Picat](http://www.picat-lang.org/) 
* [s(CASP)](https://ceur-ws.org/Vol-2970/gdepaper1.pdf)
* [Blawx](https://www.blawx.com/)
* [Catala](https://catala-lang.org/)
