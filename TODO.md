# TODO

todo list for `djblogger` project.

## todos

- [ ] migrate to postgresql database
- [ ] add dockerfile to create docker containers
- [ ] add a file (`djblogger/environ.py`) to contain environment variables (secret key, theme, ...)
- [ ] add an script to CRUD the `djblogger/environ.py` file.
- [ ] add theme support
    - [ ] add a folder named `themes` in the templates folder and static folder
    - [ ] add `theme`(string) field in the environ
    - [ ] use environ.theme in the views

# DONE

- [X] create project