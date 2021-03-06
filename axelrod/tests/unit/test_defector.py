"""Tests for the Defector strategy."""

import axelrod
from .test_player import TestPlayer

C, D = axelrod.Actions.C, axelrod.Actions.D


class TestDefector(TestPlayer):

    name = "Defector"
    player = axelrod.Defector
    expected_classifier = {
        'memory_depth': 0,
        'stochastic': False,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_state': False,
        'manipulates_source': False
    }

    def test_strategy(self):
        # Test that always defects.
        self.first_play_test(D)
        self.second_play_test(D, D, D, D)


class TestTrickyDefector(TestPlayer):

    name = "Tricky Defector"
    player = axelrod.TrickyDefector
    expected_classifier = {
        'memory_depth': float('inf'),  # Long memory
        'stochastic': False,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        # Starts by defecting.
        self.first_play_test(D)
        self.second_play_test(D, D, D, D)
        # Test if strategy tries to trick opponent.
        self.responses_test([D], [C, C, C], [C, C, C])
        self.responses_test([D], [C, C, C, D, D], [C, C, C, C, D])
        history = [C, C, C, D, D] + [C] * 11
        opponent_history = [C, C, C, C, D] + [D] + [C] * 10
        self.responses_test([D], history, opponent_history)
