#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `greetings` package."""

import pytest

from click.testing import CliRunner

from greetings import greetings
from greetings import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_simple_hello_default():
    """Test valid string from default data."""
    assert 'Hello you!' in greetings.simple_hello()

def test_simple_hello_argument():
    """Test valid string from default data."""
    assert 'Hello Danny!' in greetings.simple_hello('Danny')


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'greetings.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
