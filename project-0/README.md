# UOCIS322 - Project 0

Trivial project to exercise version control, turn-in, and other mechanisms
for CIS 322.

Please read this **thoroughly** before starting.

## Setting up Git

### Windows Users

If you're using Windows, please refer to this [link](https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/) for instructions on enabling SSH.

### Setting up keys

In order to access your GitHub repositories and commit changes,
you have to set up an SSH key first. This is more secure and convenient than using your GitHub username and password every time. Read more 
[here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

### Adding keys

Once you've created your keys and added them to your GitHub account, use the following command to add the key:
```
ssh-add path/to/.ssh/ssh_filename
```
You may also need to start an `ssh agent` every time you open a new terminal session:
```
eval $(ssh-agent)
```

### Installing git
You might already have git. Check `which git`.

If you don't, here's a tutorial on installing git: [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## General Instructions
These instructions also apply to every other project you will be doing this term. There's always a GitHub repository, like this one. You will be doing the following with EVERY project:

- Start by forking the repository on
[GitHub](https://github.com/UO-CIS322/project-0),
then cloning it locally.

- Read the instructions in `README` files (like this one). They clearly outline everything that needs to be done.

- Commit your changes and push.

- Test everything from scratch: clone elsewhere from scratch, run and make sure everything works as expected. It is recommended that you test it on the server we discussed at least once.

- Once you are done with each project, you will submit a `credentials.ini` file on Canvas. It contains your name and repository URL. An example of such a file is provided in this project: `credentials-skel.ini`.
	- BE CAREFUL with this file. Autograder reads this file, and can't correct your mistakes. If the URL is incorrect, or your name is not filled in, it will not grade your project. That is effectively the same as not turning in your project.
	- First time mistakes are can be overlooked, repeated ones will result in docking.

- You should not **ever** push `credentials.ini`. That file should only be submitted through Canvas.

## Project 0 Instructions

### Files needed to be edited
- `Makefile`

### Instructions

- Author: Jesse Baxter

- Contact address: jbaxter@uoregon.edu

- Description: The given software copies a given credintials file into a hello directory. The message in the credentials file is printed, in this case Hello world.

## Grading Rubric

* If everything works as expected, 100 will be assigned.
* If the correct message is not shown ("Hello World"), 20 points will be docked.
* If `make run` fails, 20 points will be docked.
* If `make install` fails, 20 points will be docked.
* If `credentials.ini` is commited, 10 points will be docked.
* If `README.md` is not updated with your name and info, 10 points will be docked.
* If `credentials.ini` is incorrect or not submitted, 0 will be assigned.
