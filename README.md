# package-sorter

### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

### Explanation of the Code

- The volume is calculated using width * height * length.
- A package is considered bulky if: Its volume is >= 1,000,000 cm³, or any of its dimensions (width, height, or length) is >= 150 cm.
- A package is considered heavy if its mass is >= 20 kg.
- If the package is both bulky and heavy, it is REJECTED.
- If the package is either bulky or heavy (but not both), it is SPECIAL.
- Otherwise, it is STANDARD.


### How to Use

- Clone the repository: Copy the repository URL from GitHub (click Code -> HTTPS -> Copy link (https://github.com/ManasiJadhav3012/package-sorter.git)).
- Run the script on the terminal by opening terminal at the location of the file:
```bash
python sort_packages.py