import pytest
from . import circular_queue

@pytest.fixture
def cq():
    return circular_queue.CircularQueue(max_size=5)
    
def test_empty_queueSize(cq: circular_queue.CircularQueue):
    assert cq.queueSize() == 0

def test_enqueue(cq: circular_queue.CircularQueue):
    cq.enqueue('a')
    assert cq.queueSize() == 1
    assert cq.front == cq.rear == 0

def test_dequeue(cq: circular_queue.CircularQueue):
    cq.enqueue('b')
    q_size = cq.queueSize()
    assert cq.dequeue() == 'b'
    assert cq.queueSize() == q_size - 1

def test_max_enqueue(cq: circular_queue.CircularQueue):
    for i in range(4):
        cq.enqueue(i)
    cq.enqueue(5)
    assert cq.queueSize() == 5
    for i in range(4):
        assert cq.dequeue() == i
    assert cq.dequeue() == 5
    
def test_displayQueue(cq: circular_queue.CircularQueue, capsys: pytest.CaptureFixture[str]):
    cq.enqueue('a')
    cq.enqueue('b')
    assert cq.queueSize() == 2
    cq.displayQueue()
    capture = capsys.readouterr()
    assert capture.out == 'a b\n'