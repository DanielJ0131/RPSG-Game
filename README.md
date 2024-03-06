# Examination2 
# Ngoc Hong (Mi), Chris Lubert, Daniel Jönsson

# Download Class & Package UML Diagram in terminal for Windows & Mac OS/ Linux
# Do everything in virtual enviroment by installing venv!
# Follow these steps below!

# Step: 1
# Installing venv
# Open Directory in Terminal, write (cd Examination2)
# Create the virtual environment with help of our given Makefile. In the Terminal, write (python3 -m venv .venv) and (make venv)
# Activate the venv, write for Windows (. .venv/Scripts/activate) and for Mac/Linux (. .venv/bin/activate)
# Install the virtual packages in venv. write (make install)
# Check the installed virtual packages (make installed)

# Step: 2
# Install the dot command to help generating the UML pictures from source code structure. 
# 1. choco install graphviz (Window) / brew install graphviz (Mac OS/ Linux)
# 2. dot -V (to check what version, optional!)

# Step: 3
# After virtuel enviroment is opened and graphviz is installed open up rpsg map is necessary in Examination2.
# 1. cd Examination2 (if not already opened)
# 2. cd src
# 3. cd rpsg
# Should look something like this in the terminal ~/Examination2/src/rpsg

# Step: 4
# make pyreverse
# And now UML diagram is installed.