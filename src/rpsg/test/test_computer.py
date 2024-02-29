"""Test File for Unit Testing computer.py."""


def test_get_choice(self):
    """Test get_choice method."""
    self.computer.set_choice(self.choice)
    assert self.computer.get_choice() in ["rock", "paper", "scissors", "gun"]


def test_set_choice(self):
    """Test the set_choice method."""
    self.computer.set_choice(self.choice)
    assert self.choice in ["rock", "paper", "scissors", "gun"]


def test_easy_choice(self):
    """Test the easy_choice method."""
    self.computer.easy_choice()
    assert self.computer.get_choice() == "rock"


def test_medium_choice(self):
    """Test the medium_choice method."""
    self.computer.medium_choice()
    assert self.computer.get_choice() in ["rock", "paper", "scissors", "gun"]


def test_hard_choice(self):
    """Test the hard_choice method."""
    self.computer.hard_choice()
    assert self.computer.get_choice() in ["rock", "paper", "scissors", "win"]
