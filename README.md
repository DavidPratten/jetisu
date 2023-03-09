# Jetisu

<img align="right" width="100" height="100" src="images/jetisu_logo.png">

Jetisu is a toolset for modelling with __intensionally defined relations__.
- a "__relation__" is a table with columns and rows,
- "__intensionally defined__" means the table is not defined a list of rows, or derived from other tables, but defined by computable rules.

## Doing for computation and rules what the relational model did for data
Prior to the advent of the relational model, programmers' mental model of data spanned multiple levels of abstraction and required them to procedurally navigate either hierarchies or networks to access data. The relational model challenged this approach and provided a stable and robust mental model of data for programmers to use (Schemas and Relational Queries).  

One of the relational model's key benefits is that programmers were, to a greater extent, insulated from innovation in database technologies. This isolation reduced, or removed, the cost of adoption of innovations in technologies such as: hardware, caching, virtualisation, cryptography, storage, sharding, redundancy, indexing, query optimisation, distributed systems, etc.

The Jetisu Toolkit is exploring the possibility that the relational model can do for rules and code what it did for data. And provide a stable and robust mental model of rules for programmers to use (Schemas and Relational Queries). The following diagram is a representation of what this might look like:

<img width="100%" src="images/doing for rules what rm did for data.png">

## Querying Rules As Code
The examples are chosen to illustrate the benefits (and/or challenges) of querying intensionally defined relations to model rules as code.
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
## Background to "intensionally defined relations"
Every table has an intension, which is its intended meaning and its extension which is its list of rows. But not all tables 
are defined in the same way!  

| How defined                  | Intension (a test that is true if a row is a member of the table) | Extension (list of rows)                       |
|------------------------------|-------------------------------------------------------------------|------------------------------------------------|
| Extensionally defined        | Natural Language                                                  | Listed out in a table                          |
| Derived from other relations | Query in Relational Algebra, SQL, Datalog, including fixed point operators| Generated on demand or materialised for reuse. 
| __Intensionally defined__    | __Computable Constraints and Rules__                              | __Generated or recognised on demand__          |


### Computed or Algorithmic Relations
The idea of a non-derived relation that is defined by computable constraints and rules goes back to the 1970's and 1980's at the beginning of the relational database era. Early references include:

- __Algorithmic relations__ proposed in 1975 by Patrick Hall, Peter Hitchcock and Stephen Todd (hereafter HHT). [(PDF)](https://dl.acm.org/doi/pdf/10.1145/512976.512998) 
- __Computed relations__ described in 1981 by David Maier and David Warren (hereafter MW). [(PDF)](https://dl.acm.org/doi/pdf/10.1145/582318.582345)

These proposals share a common assumption that computation is inherently directed. Neither paper suggested that an algorithmic, or computed relation could be defined in such a way that all directions of computation might be possible "out-of-the-box" with just a single definition.

### Constraint Programming
From the late 1980s the discipline of Constraint Programming CP and Constraint Logic Programming CLP emerged and begin to explore what it took to define a relation as a computable predicate over the cross product of the domains of attributes. Here is a survey of this work and a key reference for the constraint programming language [MiniZinc](https://www.minizinc.org):

- __Constraint Logic Programming: A Survey.__ (1994) J. Jaffar, Michael J. Maher [(PDF)](https://www.sciencedirect.com/science/article/pii/0743106694900337?via%3Dihub)
- __MiniZinc: Towards a Standard CP Modelling Language.__ (2007) N. Nethercote, Peter James Stuckey, Ralph Becket, S. Brand, Gregory J. Duck, Guido Tack [(SpringerLink PDF)](https://link.springer.com/chapter/10.1007/978-3-540-74970-7_38)

The two ideas of computed and algorithmic relations put together with constraint logic programming are foundations of what the Jetisu toolkit calls: "intensionally defined relations".

## A theory of intensionally defined relations
Intensionally defined relations are based on the intuition that the generalisation of an extensionally defined relation is a computable predicate over the cross-product of the domains of the attributes. 

An __intensionally defined relation__ is 
- a set of typed attributes (or columns) ```A```, along with
- a computable predicate (or constraint) ```P``` over the attributes in ```A```, which
- when further constrained in a relational query, is indistinguishable, (within some error bound 𝜖), from its finite extension of tuples (rows).

This definition closely mirrors the definition of a relation in relational database theory, and here are some implications of this definition:

__Not derived from other relations:__ An intensionally defined relation is a standalone computational artifact and not derived from other relations. And the three kinds of relations can be expressed formally as follows: 

Given that a __relation__ is an instantiation of 

```σP(dom(a1) × dom( a2) × … × dom(aN)) for some predicate P and attributes a1, a2, …, aN ∈ A.```

- An __extensionally-defined relation__ captures the relation as a list of tuples for which the predicate ```p``` is asserted to be true.

- An __intensionally-defined relation__ directly computes ```σp(dom(A1) × dom( A2) × … × dom(An))``` within error bound 𝜖 in the context of a relational query. 

- A __derived relation__ is the result of a relational query (possibly including fixed-point operators) over one,  or more, relations of any of these three kinds.

__Queried by name:__ An intensionally defined relation appears by `name` in a query in the same way that any other relation does. e.g. If `australian_gst` is an intensionally defined relation then in SQL it will be queried like this: `SELECT gst_amount FROM australian_gst WHERE price=100;`.

__Separation of Concerns__: The three discipline areas of data management, constraint and logic programming, and relational query languages can develop independently and work together in predictable ways around the common abstraction of the relation.

__Robust abstraction:__ Intensionally defined relations protect the relational programmer from needing to master Logic Programming, Constraint Programming, Search, Numerical Methods, Linear Programming, Symbolic Computation, and manage multiple semantics, termination, and negation, closed and open worlds, etc.

__Ready for query optimisation__: Existing query optimisers for extensional and derived relations can be broadened to cover querying intensionally defined relations, leading to efficiency gains over time. 

__Intimate connection between the constraints in the relation's intensional definition and the ```WHERE``` clause in a query over the relation:__ A key implication of the above definition is that the relational algebra ```SELECT``` or ```σ``` operator (```WHERE``` clause in SQL) contains constraints that may be __pushed down__ into the definition of the relation prior to retrieving the rows in the relation, rather than being applied as a filter after retrieving the rows from the relation.

__Single source of truth:__ The relational algebra is inherently agnostic to which attributes are known and used to constrain the relation and which attributes are unknown and which are sought as the answer. An intensionally defined relation may be used to query rules "forward" or in "reverse" depending on what is known prior to querying. Following HHT, the extent to which a relation is omnidirectional is called its 'effectiveness'.

__Write once, use anywhere and Privacy friendly:__ Rules and data are kept in separate relations. Rules may be applied, when appropriate, to the right data by a variant of the relational `join` `⨝` creating a derived relation which is then available for further processing.

__Better together:__ The `natural join` `⨝` of two intensionally defined relations with common attributes has a stronger predicate over its attributes than the two relations taken separately.

__Technology agnostic:__ While it is convenient to use [MiniZinc](https://www.minizinc.org) to define a relation's intension, it is not required. Any language, or system, that supports the above definitions may be used.  As to the relational query language, it is convenient to use SQL, but the same queries could easily also be formulated in Datalog or other relational query language.

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
