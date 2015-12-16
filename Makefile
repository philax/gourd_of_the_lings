test:
	python -m unittest discover -v

junit: coverage
	py.test --junitxml junit.xml test_character.py

coverage:
	coverage erase
	coverage run -m unittest discover -v
	coverage html

profile:
	rm -rf .profile
	python -m cProfile -o .profile Basic.py
	python -c "import pstats; pstats.Stats('.profile').sort_stats(2).reverse_order().print_stats(10)"


clean:
	rm -rf .profile .coverage htmlcov
