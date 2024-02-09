# Relay BE Assignment

## Project Description
In order to align incentives for Relay and for our couriers, we’re implementing a pay per delivery attempt earnings model for couriers. This means that couriers are compensated for every parcel they deliver, subject to minimum hourly earning guarantees and other targeted incentives.
We’d like you to write and deploy a stateless API endpoint that takes a courier’s activity log documenting their Relay activity over the course of a week. The endpoint should return a structured earnings statement. The activity log should be transformed into the earnings statement according to a rate card.
![Rate Card](image.png)

## Table of Contents
1. [Technologies Used](#technologies-used)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
6. [Testing](#testing)
7. [Further Improvements](#known-issues)

## Technologies Used
- Python
- Docker
- Flask
- Pandas
- Pytest
- Shell

## Installation
1. Clone the repository: `git clone https://github.com/AbhayKD/Relay-be-assignment`
2. Run make file: `docker-compose up`

## Testing 
To run tests, use the following command:

```pytest test/```
or
```docker-compose up test```
