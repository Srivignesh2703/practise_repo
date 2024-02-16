from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "sample code for github"


@app.route('/design')
def design():
    return "some design"


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("LinkedList: Empty")
        else:
            a = self.head
            while a is not None:
                print(a.data)
                a = a.next

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node.next
