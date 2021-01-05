# Eth-Vanity-Address

Eth-Vanity-Address is a simple Python script tasked with generating ethereum adresses, and testing them against a user-selected configuration for custom, visual, or ease-of-use purposes. 

## Installation

For general installation, clone this repository to your workspace and use the PIP-manager to install the requirements listed under both a `requirements.txt` doc, as well as the `pipfile`s. 

Reccomended installation is to a virtual environment, such as venv, to ensure that dependancies are compatible. This build runs on python 3.8

```bash
pip install requests
```

## Usage

In the root of the project, the main script, `app.py` exists, as well as the `found.txt` document. The application natively scans for leading 0s following the ethereum address identifier, 0x. For additional search options, utilize the `search.txt` file under `*/addrgen/search.txt`.

Following installation, the application will have examples of both inputs (to `search.txt` and `found.txt`) - these preconfigurations are for general reference only; feel free to change the search input as well as the `found` format. The script will append results to the `found.txt` file to avoid overwriting. To save a result, there will be a `save.txt` file provided under the `/addrgen/` subfolder. Please use general safety guidelines for managing any addresses produced and saved.

Once the dependencies are installed or built into your virtual environment, the script can be compiled and run using your native OS terminal. The general CLI will include information about speed, quantity, and results. To terminate the script, either kill the terminal manually or use your native OS hotkey to end the loop.

For reference:
```py
(venv) c:\ParentDirectory\Eth-Vanity-Address>pip install requests
...
...
...
(venv) C:\ParentDirectory\Eth-Vanity-Address>python app.py
```

To ensure that this python script is optimized for efficiency on a singular instance, both the build, and the interface, are provided as-is. The read and write functions are easily reconfigured, but without changing the file path, they will simply create a new file to write to (`found.txt`), or return a file-path error. As such, moving the text files will likely result in unintended conflict.

Considering the general benchmarks that python sets, there is room to be desired, but a single thread on an old Intel i7 7700-HQ was able to match 25,000 addresses/second. 

![CLI](https://i.imgur.com/ul3puOd.png)

## Contributing
The project will be free to use, clone, modify, and distribute, but is and was ultimately inteded to be a fun project that I will likely not continue. Any prolongued development will likely be a clone of this project, or a result of free-time and boredom.

## License
[MIT](https://choosealicense.com/licenses/mit/)
