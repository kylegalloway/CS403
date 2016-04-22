default:
	python3 ./evaluator.py redwall/simple.rwall

cat-error1:
	cat redwall/bad_program1.rwall

run-error1:
	-python3 ./evaluator.py redwall/bad_program1.rwall

cat-error2:
	cat redwall/bad_program2.rwall

run-error2:
	-python3 ./evaluator.py redwall/bad_program2.rwall

cat-error3:
	cat redwall/bad_program3.rwall

run-error3:
	-python3 ./evaluator.py redwall/bad_program3.rwall

# Everything above works with evaluator. Everything below needs help.

cat-conditionals:
	cat redwall/conditionals.rwall

run-conditionals:
	python3 ./prettyPrinter.py redwall/conditionals.rwall

cat-recursion:
	cat redwall/recursion.rwall

run-recursion:
	python3 ./prettyPrinter.py redwall/recursion.rwall

cat-iteration:
	cat redwall/iteration.rwall

run-iteration:
	python3 ./prettyPrinter.py redwall/iteration.rwall

cat-functions:
	cat redwall/functions.rwall

run-functions:
	python3 ./prettyPrinter.py redwall/functions.rwall

cat-arrays:
	cat redwall/arrays.rwall

run-arrays:
	python3 ./prettyPrinter.py redwall/arrays.rwall

cat-dictionary:
	cat redwall/functions.rwall

run-dictionary:
	python3 ./prettyPrinter.py redwall/functions.rwall

cat-problem:
	cat redwall/test_problem.rwall

run-problem:
	python3 ./prettyPrinter.py redwall/test_problem.rwall

clean:
	rm -rf ./__pycache__

pretty:
	python3 ./prettyPrinter.py redwall/simple.rwall

tree:
	python3 ./runParser.py redwall/simple.rwall

sanity-check:
	python3 ./prettyPrinter.py redwall/simple.rwall
	-python3 ./prettyPrinter.py redwall/bad_program1.rwall
	-python3 ./prettyPrinter.py redwall/bad_program2.rwall
	-python3 ./prettyPrinter.py redwall/bad_program3.rwall
	python3 ./prettyPrinter.py redwall/conditionals.rwall
	python3 ./prettyPrinter.py redwall/recursion.rwall
	python3 ./prettyPrinter.py redwall/iteration.rwall
	python3 ./prettyPrinter.py redwall/functions.rwall
	python3 ./prettyPrinter.py redwall/arrays.rwall
	python3 ./prettyPrinter.py redwall/functions.rwall
	python3 ./prettyPrinter.py redwall/test_problem.rwall
	@echo "Still Insane but the prettyPrinter Works...."