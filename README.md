# Network Design CLI
Simple Python CLI tool to design Fault Tolerant Networks. Final Project for ECSE 422: Fault Tolerant Computing.

## Authors
- Imad Dodin - 260713381
- Nada Marawan - 260720514

## Acknowledgements
Acknowledgements to Professor Maheswaran and the ECSE 422 Teaching Staff for the following functions whose implementations were only modified slightly:
- `graphs/Edge`
- `parsing/read_data`
- `parsing/generate`

## How to use
### Command Line
The tool is developed and tested on Python 3.7, its functionality on other versions of python is not guaranteed.

Usage Summary is provided below:
```
usage: main.py [-h] [--input [INPUT]] [--output [OUTPUT]]
               {reliability,cost} [GOAL]

Generate a Network Design

positional arguments:
  {reliability,cost}    reliability - Generate a network design meeting the
                        given reliability goal (does not minimize cost). cost
                        - Generate a network design meeting the given cost
                        constraint, maximizing reliability.

optional arguments:
  -h, --help            show this help message and exit
  --input [INPUT], -i [INPUT]
                        Input file containing symmetric reliabilities then
                        costs in row major form (default: input.txt)
  --output [OUTPUT], -o [OUTPUT]
                        Output file containing selected edges (default:
                        output.txt)

```

#### Reliability Target

For finding some feasible network given a Reliability Target (Part A):

`python main.py --input input.txt --output output.txt reliability 0.45`

#### Cost Constraint
For finding the maximum reliability network given a Cost Constraint (Part B):

`python main.py --input input.txt --output output.txt cost 150`

Input Files are expected to follow the format in input.txt and to be found on the same level as main.py (Repository Root), Output Files will be automatically be created on the same level.

### Docker

A Dockerfile is provided for portability. 

#### Building 
`docker build -t network:latest .`

#### Running

All environment variables (preceded by -e below) are **required** when running the Docker image (in contrast to the above where input and output are optional with defaults).

##### Reliability Target
`docker run -v $(pwd):/mnt/ -e input=a.txt -e output=b.txt -e command=reliability -e goal=0.97 network:latest`

##### Cost Constraint
`docker run -v $(pwd):/mnt/ -e input=a.txt -e output=b.txt -e command=cost -e goal=150 network:latest`
