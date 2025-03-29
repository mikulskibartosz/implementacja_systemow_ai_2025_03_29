.PHONY: load, split, normalize, train, evaluate

load:
	PYTHONPATH=. python src/data/load.py --config-path config/config.yaml

split:
	PYTHONPATH=. python src/data/split.py --config-path config/config.yaml

normalize:
	PYTHONPATH=. python src/features/normalize.py --config-path config/config.yaml

train:
	PYTHONPATH=. python src/models/train.py --config-path config/config.yaml

evaluate:
	PYTHONPATH=. python src/models/evaluate.py --config-path config/config.yaml
