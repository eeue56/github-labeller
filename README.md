# github-labeller
Make new github labels across multiple repos

## Dependencies

```
pip install -r requirements.txt
```

## Running

```
ACCESS_TOKEN="SOME PERSONAL TOKEN FROM GITHUB" ORG="elm-community" python main.py
```


## example settings

Create a `settings.json` that provides the repos to create the issues in, any labels you want, and any descriptions they might have.

This will probably be updated to use a better format in future

```
{
    "repos": ["stalk", "json-to-elm"],
    "labels": [
        "complexity: 1",
        "complexity: 2",
        "complexity: 4",
        "complexity: 8"
    ],
    "descriptions": {
        "complexity: 1": "A simple task, should take minimal time",
        "complexity: 2": "A task that might require a bit of exploration",
        "complexity: 4": "A task that will require a lot of exploration",
        "complexity: 8": "A task so large it will take a very long time. Consider splitting into smaller tasks"
    }
}
```