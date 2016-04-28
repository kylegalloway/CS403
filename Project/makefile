default:
	python3 ./evaluator.py redwall/simple.rwall

clean:
	rm -rf ./__pycache__

cat-error1:
	cat redwall/bad_program1.rwall
cat-error2:
	cat redwall/bad_program2.rwall
cat-error3:
	cat redwall/bad_program3.rwall
cat-conditionals:
	cat redwall/conditionals.rwall
cat-recursion:
	cat redwall/recursion.rwall
cat-iteration:
	cat redwall/iteration.rwall
cat-functions:
	cat redwall/functions.rwall
cat-arrays:
	cat redwall/arrays.rwall
cat-dictionary:
	cat redwall/dictionary.rwall
cat-problem:
	cat redwall/test_problem.rwall

run-error1:
	-python3 ./evaluator.py redwall/bad_program1.rwall
run-error2:
	-python3 ./evaluator.py redwall/bad_program2.rwall
run-error3:
	-python3 ./evaluator.py redwall/bad_program3.rwall

run-conditionals:
	python3 ./evaluator.py redwall/conditionals.rwall

run-functions:
	python3 ./evaluator.py redwall/functions.rwall

# Everything above works with evaluator. Everything below needs help.

run-recursion:
	python3 ./evaluator.py redwall/recursion.rwall

run-iteration:
	python3 ./evaluator.py redwall/iteration.rwall

run-arrays:
	python3 ./prettyPrinter.py redwall/arrays.rwall

run-dictionary:
	python3 ./prettyPrinter.py redwall/dictionary.rwall

run-problem:
	python3 ./prettyPrinter.py redwall/test_problem.rwall

# EXTRAS ======================================================================

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
	@echo "Still Insane in the Membrane but the prettyPrinter Works...."

finished:
	@echo "\n\n######################## ERROR 1 ########################\n\n"
	make cat-error1
	make run-error1
	@echo "\n\n######################## ERROR 2 ########################\n\n"
	make cat-error2
	make run-error2
	@echo "\n\n######################## ERROR 3 ########################\n\n"
	make cat-error3
	make run-error3
	@echo "\n\n######################## Arrays ########################\n\n"
	make cat-arrays
	make run-arrays
	@echo "\n\n###################### conditionals ######################\n\n"
	make cat-conditionals
	make run-conditionals
	@echo "\n\n######################## recursion ########################\n\n"
	make cat-recursion
	make run-recursion
	@echo "\n\n######################## iteration ########################\n\n"
	make cat-iteration
	make run-iteration
	@echo "\n\n######################## functions ########################\n\n"
	make cat-functions
	make run-functions
	@echo "\n\n####################### dictionary #######################\n\n"
	make cat-dictionary
	make run-dictionary
	@echo "\n\n######################## problem ########################\n\n"
	make cat-problem
	make run-problem
	make clean
