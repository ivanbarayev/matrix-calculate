#!make

login:
	risingcloud login

init:
	risingcloud init -s matrix-calculate

deploy:
	risingcloud build -r -d