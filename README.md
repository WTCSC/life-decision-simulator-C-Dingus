[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iDZRBYvt)
### Description
make choices and get outputs to make more choices until it ends

### Requirements
* python 3.12.3

### Usage
run the `main.py`
input '1' or '2' to continue through the line text

### Path Modification
To edit the text paths edit the `messages.ook` file with the following syntax

```
%msg(message number)%
(your message)
1.(option 1) %(message to run for option 1)%
2.(option 2) %(message to run for option 2)%
%msg(message number)%
```
#### Example

```
%msg0%
You reach a fork in the road
1. Go left %1%
2. Go right %2%
%msg0%
```
