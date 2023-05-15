# 1. What will be the output of the following Python code?
 

    ```python
    i = 5

    while True:

        if i%9 == 0:

            break

        print(i)

        i += 1
    ```

    a) 5 6 7 8

    b) 5 6 7 8 9

    c) 5 6 7 8 9 10 11 12 13 14 15 ….

    d) error

## Ans . (A) 5 6 7 8
#### -> i initialize from 5 and if codition satisfied like i is divisble with 9 with no remainder the loop will break

# 2. What will be the output of the following Python code?

    ```python
    d = {0: 'a', 1: 'b', 2: 'c'}

    for x in d.values():

        print(x)
    ```

    a) 0 1 2

    b) a b c

    c) 0 a 1 b 2 c

    d) none of the mentioned

## Ans . (B) a b c  
####  -> Because Dict.values return values from Key value pair

# 3. What does math.sqrt(X, Y) do?

    a) calculate the Xth root of Y

    b) calculate the Yth root of X

    c) error

    d) return a tuple with the square root of X and Y

## Ans . (C) Error 
####  -> Because it only find the square root of number 

# 4. Which of these is NOT a characteristic of namedtuples?

    a)  You can assign a name to each of the namedtuple members and refer to them that way, similarly to how you would access keys in dictionary.

    b) Each member of a namedtuple object can be indexed to directly, just like in a regular tuple.

    c) namedtuples are just as memory efficient as regular tuples.

    d) No import is needed to use namedtuples because they are available in the standard library.


## Ans . (D) No import is needed to use namedtuples because they are available in the standard library.
####  -> Because we need to Import like this

```python
from collections import namedtuple

```


# 5. 6,5,24,25,144,(?)


    a) 155

    b) 160

    c) 170

    d) 175


    Explanation :
    ##### Given

    IIIrd term is=Ist termx4,i.e.,6x4=24<br>
    IVth term is =IInd term x 5,i.e,5x5=25<br>
    Vth term is = IVth termx7,i.e.,25x7=175---> <b>Error</b><br>
    Multipliers are in the increasing order of 4,5,6,7, etc<br>

    ##### Corrected 

    IIIrd term is=Ist termx4,i.e.,6x4=24<br>
    IVth term is =IInd term x 5,i.e,5x5=25<br>
    Vth term is = IIIth termx6,i.e.,24x6=144---> <b>Corrcted</b><br>
    Multipliers are in the increasing order of 4,5,6,7, etc<br>



## Ans . D) 175
####  ->  VI th term is = IV th termx7,i.e.,25x7=175


# 6. A, B, C, D and E play a game of cards. A says to B, "If you give me three cards, you will have as many as E has and if I give you three cards, you will have as many as D has." A and B together have 10 cards more than what D and E together have. If B has two cards more than what C has and the total number of cards be 133, how many cards does B have ?



    a) 22

    b) 35

    c) 23

    d) 25


## Ans . D) 24.2 ~ 25


# 7. If apples cost 5 for 75c how many can you buy for $5.70?


    A) 18

    B) 19

    C) 28
    
    D) 38
    

## Ans . D) 38 

#### 75 cents / 5 apples = 15 cents per apple

#### Now, we can calculate how many apples we can buy for $5.70:

#### $5.70 / 0.15 per apple = 38 apples

# 8. Ram had 20 bottles. He went to market and bought 8 crates of bottles. Each crate had 6 bottles. How many bottles does Ram has now?


    a) 38

    b) 48

    c) 58

    d) 68
    
## Ans . (D) 68

# 9. A group raises $92.50 for charity. The money will be equally divided between 3 charities.

    How much money will each charity receive from the group?


    A) 28.3

    B) 30.25

    C) 29.09

    D) 30.83
    
## Ans . (D) 30.83
 

# 10. In the HBO show Silicon Valley, one of the characters creates a mobile application called Not Hot Dog. It works by having the user take a photograph of food with their mobile device. Then the app says whether the food is a hot dog. To create the app, the software developer uploaded hundreds of thousands of pictures of hot dogs. How would you describe this type of machine learning?


    a)Reinforcement machine learning

    b)unsupervised machine learning

    c)supervised machine learning

    d)semi-supervised machine learning
    
    
## Ans. (C) Supervised Machine Learning

# 11. You're working on a binary classification task, to classify if an image contains a cat ("1") or doesn't contain a cat ("0"). What loss would you choose to minimize in order to train a model?

    a)L = y log y^ + (1−y) log (1− y^)

    b)L = - y log y^ - (1−y) log (1− y^)

    c)L = || y - y^ ||22

    d)L = || y - y^ ||22 + constant
    
## Ans (B) L = - y log y^ - (1−y) log (1− y^)

# 12. The most significant phase in genetic algorithm is ________.


    a) Mutation

    b) Selection

    c) Fitness function

    d) Crossover

## Ans (B) Selection

# 13. What is unsupervised learning?


    a) Number of groups may be known

    b) Features of group explicitly stated

    c) Neither feature nor number of groups is known

    d) None of the above
    
## Ans (B) Neither feature nor number of groups is known

# 14. __________will apply element wise activation function to the output of convolution layer. 

A. Input Layer

B. Convolution Layer

C. Activation Function Layer

D. Pool Layer 

## Ans. (C) Activation Function Layer


```python

```
