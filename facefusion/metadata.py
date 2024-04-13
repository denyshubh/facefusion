METADATA =\
{
	'name': 'Web3Fusion',
	'description': 'Next generation face swapper and enhancer',
	'version': '2.5.1',
	'license': 'MIT',
	'author': 'Henry Ruhs',
	'url': 'https://web3fusion.net'
}


def get(key : str) -> str:
	return METADATA[key]
