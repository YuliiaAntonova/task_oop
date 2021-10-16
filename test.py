import pytest
from time import sleep
from signers import Singer


signer = Singer("bibo", "bobo")


def test_pyjwt_encode():
    assert signer.pyjwt_encode({"a": 1})


def test_pyjwt_decode():
    token = signer.pyjwt_encode({"a": 777})
    assert signer.pyjwt_decode(token)


def test_its_encode():
    assert signer.its_encode({"a": 1})


def test_its_decode():
    token = signer.its_encode({"a": 777})
    assert signer.its_decode(token)
