clean: 
	find . | grep -E "__pycache__|.pyc|.pytest_cache|.DS_Store$$" | xargs rm -rf