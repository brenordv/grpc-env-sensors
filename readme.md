# Environment Sensor Data Processor
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=brenordv_grpc-env-sensors&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=brenordv_grpc-env-sensors)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=brenordv_grpc-env-sensors&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=brenordv_grpc-env-sensors)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=brenordv_grpc-env-sensors&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=brenordv_grpc-env-sensors)

[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=brenordv_grpc-env-sensors&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=brenordv_grpc-env-sensors)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=brenordv_grpc-env-sensors&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=brenordv_grpc-env-sensors)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=brenordv_grpc-env-sensors&metric=bugs)](https://sonarcloud.io/summary/new_code?id=brenordv_grpc-env-sensors)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=brenordv_grpc-env-sensors&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=brenordv_grpc-env-sensors)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=brenordv_grpc-env-sensors&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=brenordv_grpc-env-sensors)

I’m used to working in projects where the system receives tons of data (readings) from various environment sensors and 
then decide to act, depending on what it is receiving.

Since I have never worked with gRPC and ZODB, I decided to create this project.
The idea is simple: Use gRPC and ZODB and create a base system that could digest lots of sensor data and scale out,
if necessary. The messages can be received, read and processed directly using a gRPC client or via the Flask API (which,
in turn, use the gRPC client).

Some aspects of this project (like validation and what to do with the readings received) are quite generic,
since it’s not based on any business logic or real world case. I plan on setting up a couple of sensors with an 
Arduino (or a Raspberry Pi) and make it send the readings to the API.

# Why Python, Flask and gRPC?
## Python
My programming language of choice. Easy to learn, fast to code and help is just a DuckDuckGo (or Google) search away.

## Flask
In my opinion, Flask is way more flexible, easy to learn and lightweight than Django. Taking that in consideration, 
along with the scope of this project, it makes more sense to choose Flask over Django.

## gRPC
I've heard some great things about gRPC, but never tried it. As far as I researched it's a great option for a low 
latency, high scalability (language agnostic) solution. It adds a couple layers of complexity to the application (when
we compare to not using any type of RPC at all), but I'm believing it is worth it, specially considering load balancing 
and application evolution.

## ZODB
Until this project I had never even heard of Zope Foundation or ZODB, but it turned out to be an excellent option.
It's simple and fast, great for concurrent access. I know it was not designed for this type of use, but would work.
In a real life scenario I could probably use ZODB as a buffer for a slower, but more scalable solution.


# Entities
In its current state, this project has 3 entities:
1. **Location**: Not all that useful. Not used for anything, really. Included because it makes sense, even in a basic 
setting for this type of thing.
2. **Sensor**: Represents the physical sensor that's (hypothetically) sending environment readings.
3. **Sensor Reading**: The actual reading from the sensor. Contains a lot of data.

The current version of `Sensor Reading` contains both the id of its sensor and the id of its location. Normally, the 
reading would not have both, but I decided to include it so I could make a few more validations on each reading.

Also, all entities have read-only properties and validation on setters, to make sure everything is has it should be.

# How to make it all work
You use the current scripts:
1. `run_server.py`: starts the gRPC server. You should run this first.
2. `run_api.py`: starts the flask API. You should run this after `run_server.py`, so it can connect to the server.
3. `run_client.py`: sends random readings to the server and then fetches (and prints) all readings
4. `run_send_api_request.py`: sends a post request to the API (good to make simple tests)
5. `run_print_sensors_and_locations.py`: prints all sensors and locations available.
6. `run_playground.py`: testing area. don't need to run it for anything.

## Performance
- *Update - Dec 12th, 2021*: I used the IDE (PyCharm) to run the gRPC server AND the API at the same time. To make the 
requests I used another application I made using GoLang and the result was: 578 requests processed each second 
(or 49.9 million requests/day). It's a good first start, but I believe I can do better.

- *Update - Dec 21st, 2021*: After a bunch of refactoring in both this application and the one I use to test it, I've 
got a better result: 1156 requests/second (or 99.8 million requests/day).

### Test output for sending 5000 readings
```text
go-Request!::POST
Your session id is: 051a2b75-6397-4e8e-b4da-2a87145e0ee2
Making POST requests 100% |████████████████████████████████████████████████████████████████████| (5000/5000, 1156 it/s)
Done! Elapsed time: 514.3µs

Process finished with the exit code 0
```

### Test output for sending 5000 request to get latest 1000 readings
```text
go-Request!::GET
Your session id is: 27b122df-137e-4c15-86f9-04cef98eabe0
Making GET requests 100% |████████████████████████████████████████████████████████████████████| (5000/5000, 286 it/s)
Done! Elapsed time: 0s

Process finished with the exit code 0
```

### Test output for sending 5000 request to get latest 100 readings
```text
go-Request!::GET
Your session id is: 27b122df-137e-4c15-86f9-04cef98eabe0
Making GET requests 100% |████████████████████████████████████████████████████████████████████| (5000/5000, 286 it/s)
Done! Elapsed time: 0s

Process finished with the exit code 0
```


# Big picture
- Clients, services, private apis and other clients can access teh gRPC endpoints.
- Meanwhile, a public API can be used (by a frontend or other third party applications), to make use of gRPC`s endpoint.  
![Simplified big picture of this project](schema_envisdp_v1simple.png)


# TODO
0. Lots of refactoring...
1. Create flask interface (in progress)
2. Add post route for adding sensor_reading
3. Standardize fetch base result to include item count and is_empty property
4. Add swagger to flask interface
5. Convert single use scripts to a commandline interface
6. Add unit tests
7. Add stress tests


# Next steps
After finishing TODO items 1 and 2, I'll probably go look for a raspberry pi zero w and a couple of sensors, so I 
can start "Audrey II" project.

# Application used to test the API:
go-Request: https://github.com/brenordv/go-request
