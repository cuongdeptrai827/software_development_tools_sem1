#  Общее описание решений 
1. Сделал git clone своего репозитория
2. открыл папку geometric_lib через терминал 
3. Описал решение фаилов rectangle.py и triangle.py на Pycharm
4. Сделал git commit каждому файлу
 
---
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

---
# Описание каждой функции с примерами вызова
## **Circle:** 

````
def area(r) :
return math.pi *r *r
````

  Number r is  the radius of the circle

  Return the value of square of the circle with formula S = pi * r^2 

  _Example:_

  in : `10`
  
  out : `314,16`

 
``` 
def perimeter(r): 
return 2 * math.pi * r 
``` 

  Number r is the radius of the circle

  return the value of perimeter of the circle with formula S = pi * 2r

  _Example :_ 

  in : `10`

  out : `62,83`

## Rectangle: 
  ``` 
  def rectangle(a,b):
  return a*b
   ```

Numbers a and b are two sides of the rectangle.

Return the result as the area of a rectangle with two sides a and b.


_Example :_

in: `3 4` 

out : `12`



```` 
def perimeter(a, b):
return 2(a + b)
````


Numbers a and b are two sides of the rectangle.

Returning the result is the perimeter of the rectangle with 2 sides a and b. 
 
Example :

in : `3 4`

out : `14`


##  Square: 

    def square(a):
       return a*a

Number a is the side of the square.

Return  the area of the square of side a

_Example:_

in : `10` 

out : `100`

````
   def perimeter(a):
   return 4 * a
````
Number a is the side of the square.

Return to the perimeter of the square of side a.

_Example :_

 in : `10`

 out : `40`

## Triangle :
   
```` 
def area(a, h):
return a * h / 2 
````

a is a side of a right triangle.

h is the height lowered from the opposite peak to a.

Return the perimeter of the right triangle.

 _Example:_ 

  in : `10 5`

  out : `25`
 
```
def perimeter(a, b, c):
   return a + b + c
``` 
a,b,c are the lengths of the three sides of the triangle respectively.

Return  the perimeter of the triangle.
 
_Example :_ 

in : `10 15 20` 

out : `45` 


--- 

# История изменения проекта с хешами комитов 

1. _**commit d84b719181d9841f7caacbf0dbec420a4379ee28 **_
````
Author: Nguyen Le Cuong <nguyenlecuongaaa@gmail.com>
Date:   Tue Oct 10 21:01:25 2023 +0300
adding comment to square.py
````
2. _**commit bf1c5abc5f48026cd61d599adcf2060fc58f6302**_ 
````
Author: Nguyen Le Cuong <nguyenlecuongaaa@gmail.com>
Date:   Tue Oct 10 21:00:17 2023 +0300

     `adding comment to rectangle.py`
````
3. **_commit 437a5b116c3aece0dfce7c5f9b7e179141512d63_**
````
Author: Nguyen Le Cuong <nguyenlecuongaaa@gmail.com>
Date:   Tue Oct 10 20:58:52 2023 +0300

     `adding comment to circle.py`
````
4. _**commit 4462fe80c0f161f8bd7570650ba0675197dd5165**_
````
Author: Nguyen Le Cuong <nguyenlecuongaaa@gmail.com>
Date:   Tue Oct 10 20:55:58 2023 +0300

     `Adding comment to triangle.py`
````

