<h1>Chess game</h1>

This is a simple chess game. Users can play against themselves, or invite a friend over for a local game. To learn the rules of the game, click the link below. 

<h2> Documentation <h2>
 
[vaatimusmäärittely](dokumentaatio/vaatismusmaarittely.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

 
<h2> Instructions: </h2>

Run the program with:
```
poetry run invoke start
```

Run the tests with:
```
poetry run invoke test
```
Create the coverage report with:
```
poetry run invoke coverage-report
```
Run pylint tests with:
```
poetry run invoke lint
```

<h2> How to play: </h2>

White starts the game. To make a move, click a piece, and drag it to the desired locating by holding down the mouse button, and releasing it at the destination. More information about the rules can be read from here: [Chess rules](https://en.wikipedia.org/wiki/Rules_of_chess)


