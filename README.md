# Aemulator
A try to solve challenges in a distributed manner. 
The idea is explained in this German blog entry: https://www.dobuch.de/meine-reise-mit-docker-teil-1/

## Goal in a few Words
Main goal for me is to get more familiar with docker and its ecosystem. 
To achieve this I want to build a system that eases to find solutions to hard problems.
The process of finding the solution is therefore split into a lot of smaller problems and distributed to multiple clients on separate containers.

## System Structure:
* Challenger: The centralized service where participants can join and request the challenge to solve.
* Participants: Multiple containers trying to solve the challenge and report it to the validator.
* Validator: Whenever a participant container "thinks" it found a solution, the validator (surprise) validates it and tells the challenger a solution was found. 

## TODOs
- [ ] Implement Challenger API.
- [ ] Implement Challenger API docker image.
- [ ] Implement Challenger.
- [ ] Implement Challenger Web viewer. 
- [ ] Implement Participants API.
- [ ] Implement Participants API docker image.
- [ ] Implement Validator API.
- [ ] Implement Validator API docker image.
- [ ] Implement examplary solution solver (PoC).
- [ ] Implement build automation.