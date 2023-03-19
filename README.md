# pyConfigPyramid

A Python class for loading configuration settings from a JSON file.

### Usage

1. Create a JSON file with your configuration settings. For example, "wangConfig.json":

    ```json
    {
        "foo": "bar",
        "answer": 42,
        "enabled": true
    }
    ```

2. Import the `WangConfig` class and create an instance:

    ```python
    from wangConfig import WangConfig

    config = WangConfig()
    ```

3. Access your configuration settings as attributes on the `config` object:

    ```python
    print(config.foo)  # "bar"
    print(config.answer)  # 42
    print(config.enabled)  # True
    ```

### Notes

- The `WangConfig` class uses the `json` and `os` libraries to read the JSON file.
- The JSON file must be named "wangConfig.json" and located in the same directory as "wangConfig.py".
- If the JSON file is not found or cannot be read, an error will be raised.
- If a requested configuration setting is not found in the JSON file, an error will be raised.

Feel free to modify and improve this class as needed for your specific use case. Happy coding!
