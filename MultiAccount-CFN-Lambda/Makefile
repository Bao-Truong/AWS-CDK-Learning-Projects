venv:
	source .venv/bin/activate
install-requirements:
	python -m pip install -r requirements.txt
synth s:
	cdk synth > cdk.out/manifest.yml
	cat cdk.out/manifest.yml
	code cdk.out/manifest.yml

deploy apply:
	cdk deploy
ls:
	cdk ls
destroy:
	cdk destroy

diff plan:
	cdk diff 
