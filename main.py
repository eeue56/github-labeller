import os
from github.GithubException import GithubException
from github import Github
import randomcolor

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ORG = os.getenv("ORG")

def create_label(github, repo, label_name, color, description):
    repo = github.get_repo(f"{ORG}/{repo}")
    labels = repo.get_labels()

    for label in labels:
        if label.name == label_name:
            print(f"Label {label_name} already exists for repo {repo}, skipping.")
            return

    print(f'Making label {label_name} with color #{color} and description "{description}" in repo {repo}')
    repo.create_label(label_name, color, description)


def update_descriptions(github, repo, label_name, description):
    repo = github.get_repo(f"{ORG}/{repo}")
    labels = repo.get_labels()

    for label in labels:
        if label.name == label_name:
            print(f"Changing description for {label_name} in repo {repo}, from '{label.description}' to '{description}'.")
            label.edit(label.name, label.color, description)
            return
    else:
        print(f'Failed to find label {label_name} in repo {repo}.')

def main():
    import json
    with open('settings.json') as f:
        settings = json.load(f)

    color_generator = randomcolor.RandomColor()
    github = Github(ACCESS_TOKEN)

    for label in settings['labels']:
        [color] = color_generator.generate()
        color_without_hex = color[1:]

        for repo in settings['repos']:
            create_label(github, repo, label, color_without_hex, settings['descriptions'][label])

    for (label_name, description) in settings['descriptions'].items():
        for repo in settings['repos']:
            update_descriptions(github, repo, label_name, description)


if __name__ == '__main__':
    main()