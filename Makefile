
install:
	brew install portaudio
	pip install soundmeter

run:
	@source .env && python soundmeter.py
