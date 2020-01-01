answers:
	tesseract images/answers.png results/answers

empty: 
	tesseract images/empty.png results/empty

test:
	tesseract images/test.png results/test

clean:
	rm results/*.txt

run:
	python image-to-text.py