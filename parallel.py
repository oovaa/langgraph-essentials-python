from langgraph.types import Command, interrupt
import operator
from typing import Annotated, List, Literal, TypedDict
from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    nlist: Annotated[List[str], operator.add]


def node_a(state: State) -> State:
    print(f'Adding "A" to {state["nlist"]}')
    return State(nlist=["A"])


def node_b(state: State) -> State:
    print(f'Bdding "B" to {state["nlist"]}')
    return State(nlist=["B"])


def node_c(state: State) -> State:
    print(f'Adding "C" to {state["nlist"]}')
    return State(nlist=["C"])


def node_d(state: State) -> State:
    print(f'Adding "D" to {state["nlist"]}')
    return State(nlist=["D"])


def node_BB(state: State) -> State:
    print(f'Adding "BB" to {state["nlist"]}')
    return State(nlist=["BB"])


def node_CC(state: State) -> State:
    print(f'Adding "CC" to {state["nlist"]}')
    return State(nlist=["CC"])


builder = StateGraph(State)
# create nodes
builder.add_node("A", node_a)
builder.add_node("B", node_b)
builder.add_node("C", node_c)
builder.add_node("D", node_d)
builder.add_node("BB", node_BB)
builder.add_node("CC", node_CC)


# adding edges
builder.add_edge(START, "A")
builder.add_edge("A", "B")
builder.add_edge("A", "C")
builder.add_edge("B", "BB")
builder.add_edge("C", "CC")
builder.add_edge("BB", END)
builder.add_edge("CC", END)
# builder.add_edge("C", END)
# builder.add_edge("D", END)

# export graph variable for use elsewhere

graph = builder.compile()

print(graph.get_graph().draw_ascii())


initial_state = State(nlist=["initial state"])

print(graph.invoke(initial_state))
