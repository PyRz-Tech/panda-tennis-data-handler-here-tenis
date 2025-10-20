```mermaid
graph TD
    A[API] -->|Request| B[Python: requests]
    B -->|JSON Response| C[JSON Data]
    C -->|Convert| D[Pandas DataFrame]
    D -->|Save| E[Output.csv]
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbf,stroke:#333,stroke-width:2px
    style E fill:#ffb,stroke:#333,stroke-width:2px
```
```
tenis_api_project/
    | __config/
    |   |__config.py
    |   |___ __init__.py
    |
    |__src/
    |   |__ __init__.py
    |   |__ api_client.py
    |   |__ data_processor.py
    |   |__ utils.py
    |
    |__tournaments/
    |   |__ output.csv
    |
    |__ docs/
    |   |__ Concepts.md
    |   |__ HowCreate.md
    |   |__ TipsForBetter.md
    |   |__WhyPandas.md
    |   |__WhyRestAPI.md
    |
    |__ requirements.txt
    |__ .env
    |__ run.py
    |__ README.md
```


```
[API] --> [Request (Python)] --> [JSON Data] --> [Pandas DataFrame] --> [Output.csv]
```
