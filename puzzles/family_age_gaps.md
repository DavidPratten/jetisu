# How old is Donald?

The following puzzle is from Peter Revesz's 1993 paper "A closed-form evaluation for Datalog queries with integer (gap)-order constraints." _Theoretical Computer Science, 116(1), 117–149._ https://doi.org/10.1016/0304-3975(93)90222-F

The solution below demonstrates an approach to this problem using complete relations.

## Problem

> Alfred and Alice have children Bernard, Carl and Donald in this order.
Bernard and Bernice have a child Edward. Donald and Denise have children Elise and
Fred. Edward and Elise have a child, Gerald. Fred and Felice have a child, Harold. 
Alfred is not yet 70, and Harold is already in school. Gerald was born just last
month. Elise is over four years older than her younger brother Fred, and Bernard is over
25 years older than his son Edward. Assuming that there is over 17 years difference between parents and their children
and that no siblings are twins or born in the same year, how old is Donald?

And here the solution with a literate programming query using a complete relation and SQL.

## Solution

| **Donald_age** |
| -- |
| 47 |
| 48 |
| 49 |

## Relation Expression

```SQL
SELECT Donald_age
from COMPLETE(
    Alfred_age int, Alice_age int, Bernard_age int,
    Bernice_age int, Carl_age int, Donald_age int,
    Denise_age int, Edward_age int, Elise_age int,
    Fred_age int, Felice_age int, Gerald_age int,
    Harold_age int
  )
WHERE
    ---- Approach
    ---- Given that no siblings are twins or born in the same year we will use > rather than >=
    ---- Given the age gap between parents and their children we will add a generational gap test for each family

    -- Alfred and Alice have children Bernard, Carl and Donald in this order.
    Bernard_age > Carl_age
    AND Carl_age > Donald_age
    -- generational gap of >17 years
    AND min(Alfred_age, Alice_age) - 17 > max(Bernard_age, Bernice_age, Carl_age, Donald_age)

    -- Bernard and Bernice have child Edward.
    -- generational gap of >17 years
    AND min(Bernard_age, Bernice_age) - 17 > Edward_age

    -- Donald and Denise have children Elise and Fred.
    -- generational gap of >17 years
    AND min(Donald_age, Denise_age) - 17 > max(Elise_age, Fred_age)

    -- Edward and Elise have child Gerald.
    -- generational gap of >17 years
    AND min(Edward_age, Elise_age) - 17 > Gerald_age

    -- Fred and Felice have child Harold
    -- generational gap of >17 years
    AND min(Fred_age, Felice_age) - 17 > Harold_age

    -- Alfred is not yet 70
    AND Alfred_age < 70

    -- Harold is already in school
    AND Harold_age > 5

    -- Gerald was born just last month
    AND Gerald_age = 0

    -- Elise is over 4 years older than her younger brother Fred
    AND Elise_age - 4 > Fred_age

    -- Bernard is over 25 years older than his son Edward
    AND Bernard_age - 25 > Edward_age;

```
