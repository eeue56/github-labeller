import os
from github.GithubException import GithubException
from github import Github
import randomcolor

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ORG = os.getenv("ORG")

def create_label(github, repo, label_name, color):
    repo = github.get_repo(f"{ORG}/{repo}")
    labels = repo.get_labels()

    for label in labels:
        if label.name == label_name:
            print(f"Label {label_name} already exists for repo {repo}, skipping.")
            return

    print(f'Making label {label_name} with color #{color} in repo {repo}')
    repo.create_label(label_name, color)


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
            create_label(github, repo, label, color_without_hex)


if __name__ == '__main__':
    main()