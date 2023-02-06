# First implementation of intensionally defined relations
We know that intensionally defined (i.e. computed or algorithmic) relations were conceived of in the mid'70s and early 80s, but for some reason the idea never took off. 

As unlikely as it seems, there does not appear to be any implementations of intensionally defined relations prior to the Jetisu toolkit. 

Please assist by testing this claim.

## What would qualify as an earlier implementation?
An earlier implementation of
- computed,
- algorithmic, or
- intensionally defined 

relations would have the following attributes.

Given two intensionally-defined relations, `I` and `J` and an extensionally-defined relation `D`:

1. `I` and `J` are relations as understood in the Relational Algebra just as `D` is. 
1. `I` and `J` may be queried by name using SQL, Relational Algebra, Datalog, or other [language that compiles to SQL](https://github.com/ajnsit/languages-that-compile-to-sql) just as `D` may. 
1. And within relational queries over `I`, the implementation will allow the query to: 
   1. constrain any, or all, attributes of `I` with the `σ (sigma)` relational algebraic operator, and
   1. query `I` as a stand-alone relation, and
   1. query `I ⨝ (join) D`, and
   1. query `I ⨝ (join) J`
1. `I` and `J` are defined using code, or rules, rather than as a list of tuples
1. `I` and `J` could be coded using any approach that creates a relation that behaves like `D` does under the four above conditions. e.g. The definitions might be coded in MiniZinc, Prolog, First Order Logic, satisfaction solver instructions, Answer Set Programming, Constraint Programming, Symbolic Computation, Numerical Methods

## Partial Conformance
Partial conformance to this test may be demonstrated by defining the following relation and executing the following queries.

1. Define a relation called ```australian_gst``` which captures the Australian 10% VAT tax which is called a “Goods and Services Tax” (GST):

```australian_gst(price, ex_gst_amount, gst_amount)```

The following example tuple belongs to this relation:

| **price** | **ex_gst_amount** | **gst_amount** |
|---------|-------------------|----------------|
| 110   | 100               | 10             |

2. Run the following three queries using SQL or equivalent relational query language.

```
SELECT * FROM australian_gst WHERE price = 220;

SELECT * FROM australian_gst WHERE ex_gst_amount = 200;

SELECT * FROM australian_gst WHERE gst_amount = 20;
```
and get the following result each time.

| **price** | **ex_gst_amount** | **gst_amount** |
|-----------|-------------------|----------------|
| **220**   | 200               | 20             |

The Jetisu Toolkit's implementation of this relation is [here](../Australian_GST.ipynb). 

## Have you seen this before?
Please raise an issue if you can point to a prior implementation of
- computed,
- algorithmic, or
- intensionally defined 

relations.

